# > Importações
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
from airflow.providers.postgres.hooks.postgres import PostgresHook
import numpy as np

# > Argumentos
# DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 11, 25),
    'retries': 1,
    'catchup': False,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@daily'
}
dag = DAG(
    'livros_corrigido',
    default_args = default_args,
    description = 'ETL de dados do Mercado Livre'
)
# Requisição
headers = {
    "Referer": 'https://www.mercadolivre.com.br',
    "Sec-Ch-Ua": '"Not(A:Brand)";v="99", "Opera GX";v="118", "Chromium";v="133"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
}

# > Tarefas
# 1. Iniciar Pipeline
def iniciar_pipeline(ti):
    print(">> Debug: Pipeline e primeira tarefa configurada com sucesso!")
# 2. Importar Dados dos Livros do CSV
def obter_livros(ti):
    print(">>Debug: Importando os dados do csv")
    dataframe_livros = pd.read_csv(
        '/opt/airflow/dags/dados/books.csv',
        encoding='latin-1',
        sep=';'
    )
    PRECO_MINIMO = 25.00
    PRECO_MAXIMO = 150.00
    qtd_livros = len(dataframe_livros)
    precos_aleatorios = [
        round(random.uniform(PRECO_MINIMO, PRECO_MAXIMO), 2) 
        for _ in range(qtd_livros)
    ]
    dataframe_livros['Preco'] = precos_aleatorios
    print(dataframe_livros.head())
    dataframe_livros.drop_duplicates(subset='Book-Title', inplace=True)
    s_year_clean = dataframe_livros['Year-Of-Publication'].replace(0, np.nan)
    s_date_string = s_year_clean.astype(str).str.replace('.0', '', regex=False) + '-01-01'
    dataframe_livros['ano'] = pd.to_datetime(s_date_string, errors='coerce')
    dataframe_livros['ano'] = dataframe_livros['ano'].dt.strftime('%Y-%m-%d')
    dataframe_livros['ano'] = dataframe_livros['ano'].replace({np.nan: None})

    ti.xcom_push(key='livros_dados', value=dataframe_livros.to_dict('records'))
# 4. Salvar dados no banco de dados
def inserir_dados(ti):
    dados_livros = ti.xcom_pull(key='livros_dados', task_ids='tarefa_importar_dados_csv')
    if not dados_livros:
        raise ValueError("Nenhum livro encontrado")
    sql = """
    INSERT INTO livro (isbn, titulo, autor, publicacao, editora, imageurl, preco)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')
    for livro in dados_livros:
        print(livro['ISBN'])
        print(livro['ano'])
        #postgres_hook.run(sql, parameters=(livro['ISBN'], livro['Book-Title'], livro['Book-Author'], datetime(livro#['Year-Of-Publication'], 1, 1), livro['Publisher'], livro['Image-URL-S'], livro['Preco']))
        postgres_hook.run(sql, parameters=(livro['ISBN'], livro['Book-Title'], livro['Book-Author'], livro['ano'], livro['Publisher'], livro['Image-URL-S'], livro['Preco']))

# > Operadores
# 1. Iniciar Pipeline
tarefa_iniciar_pipeline = PythonOperator(
    task_id = 'tarefa_iniciar_pipeline',
    python_callable = iniciar_pipeline,
    dag = dag
)
# 2. Importar Dados dos Livros do CSV
tarefa_importar_dados_csv = PythonOperator(
    task_id = 'tarefa_importar_dados_csv',
    python_callable = obter_livros,
    dag = dag
)
# 3. Criar Tabela para armazenar os livros
criar_tabela_livro = SQLExecuteQueryOperator(
    task_id = 'criar_tabela_livro',
    conn_id = 'postgres_connection',
    sql = """
    CREATE TABLE IF NOT EXISTS livro (
        id SERIAL PRIMARY KEY,
        isbn VARCHAR(20) UNIQUE NOT NULL,
        titulo VARCHAR(255) NOT NULL,
        autor VARCHAR(255) NOT NULL,
        publicacao DATE,
        editora VARCHAR(100),
        imageurl VARCHAR(255),
        preco NUMERIC(6, 2) NOT NULL
    );
    """,
    dag = dag
)
# 4. Inserir dados no banco
inserir_dados_livros = PythonOperator(
    task_id='inserir_dados_livros',
    python_callable = inserir_dados,
    dag = dag
)

# > Ordem das Dependências
tarefa_iniciar_pipeline >> tarefa_importar_dados_csv >> criar_tabela_livro >> inserir_dados_livros