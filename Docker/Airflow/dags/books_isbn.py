import pendulum
import requests
import json
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook

# Nome da sua conexão Airflow que aponta para o Postgres (você a criará no Passo 2)
POSTGRES_CONN_ID = "postgres_conn" 
BOOK_ISBN = "9781449339739"  # ISBN de exemplo (Use 'data analysis with python')

# Função para buscar e processar os dados da API
def fetch_and_process_book_data(isbn: str, **context) -> dict:
    """Busca dados na Google Books API e extrai ISBN-10, ISBN-13, Título e Autor."""
    
    base_url = "https://www.googleapis.com/books/v1/volumes"
    query = f"isbn:{isbn}"
    url = f"{base_url}?q={query}"
    
    print(f"Buscando URL: {url}")
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    if data.get('totalItems', 0) == 0:
        raise ValueError(f"Livro com ISBN {isbn} não encontrado.")

    volume = data['items'][0]['volumeInfo']
    
    # Extração de Título e Autor (pode ser uma lista)
    title = volume.get('title', 'N/A')
    authors = ", ".join(volume.get('authors', ['Autor Desconhecido']))

    # Inicializa ISBNs com N/A
    isbn_10 = 'N/A'
    isbn_13 = 'N/A'

    # Busca por ISBN-10 e ISBN-13 nos identificadores
    for identifier in volume.get('industryIdentifiers', []):
        if identifier['type'] == 'ISBN_10':
            isbn_10 = identifier['identifier']
        elif identifier['type'] == 'ISBN_13':
            isbn_13 = identifier['identifier']
            
    book_info = {
        "isbn_10": isbn_10,
        "isbn_13": isbn_13,
        "title": title,
        "authors": authors
    }
    
    print(f"Dados extraídos: {json.dumps(book_info, indent=2)}")
    
    # Envia os dados para o XCom para a próxima tarefa
    return book_info

# Função para salvar os dados no PostgreSQL
def save_to_postgres(**context):
    """Cria a tabela (se não existir) e insere os dados do XCom no PostgreSQL."""
    
    # Recupera os dados retornados pela tarefa anterior
    book_info = context['ti'].xcom_pull(task_ids='fetch_book_details')
    
    if not book_info:
        raise ValueError("Não foi possível recuperar os dados do livro de XCom.")
        
    isbn_10 = book_info['isbn_10']
    isbn_13 = book_info['isbn_13']
    title = book_info['title'].replace("'", "''") # Escapa aspas para SQL
    authors = book_info['authors'].replace("'", "''")
    
    # 1. Cria o Hook e a conexão com o banco
    pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)

    # 2. SQL para criar a tabela (se não existir)
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS public.livros_api (
        isbn_13 VARCHAR(20) PRIMARY KEY,
        isbn_10 VARCHAR(20),
        titulo VARCHAR(255),
        autor VARCHAR(255),
        data_insercao TIMESTAMP DEFAULT NOW()
    );
    """
    pg_hook.run(create_table_sql)
    print("Tabela 'livros_api' verificada/criada.")

    # 3. SQL para inserir os dados (ON CONFLICT para evitar erro se já existir)
    insert_sql = f"""
    INSERT INTO public.livros_api (isbn_13, isbn_10, titulo, autor)
    VALUES ('{isbn_13}', '{isbn_10}', '{title}', '{authors}')
    ON CONFLICT (isbn_13) DO UPDATE 
    SET titulo = EXCLUDED.titulo, 
        autor = EXCLUDED.autor,
        data_insercao = NOW();
    """
    pg_hook.run(insert_sql)
    print(f"Dados do livro '{title}' inseridos/atualizados no banco de dados.")

# Definição do DAG
with DAG(
    dag_id='02_book_data_to_postgres',
    start_date=pendulum.datetime(2025, 10, 31, tz="UTC"),
    schedule=None,
    catchup=False,
    tags=['api', 'postgres'],
) as dag:
    
    # Tarefa 1: Busca os dados da API
    fetch_task = PythonOperator(
        task_id='fetch_book_details',
        python_callable=fetch_and_process_book_data,
        op_kwargs={'isbn': BOOK_ISBN}, # Passa o ISBN como argumento
    )
    
    # Tarefa 2: Salva os dados no Postgres
    save_task = PythonOperator(
        task_id='save_to_database',
        python_callable=save_to_postgres,
    )

    # Definição da ordem de execução
    fetch_task >> save_task