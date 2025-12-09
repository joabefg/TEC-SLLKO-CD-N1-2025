# > Importações
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
import funcoes_helper.funcoes_postgres as post
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
with DAG(
    'etl_livros_postgres',
    default_args = default_args,
    description = 'ETL de dados do Mercado Livre'
)as dag:
    # > Operadores
    # 1. Iniciar Pipeline
    tarefa_iniciar_pipeline = PythonOperator(
        task_id = 'tarefa_iniciar_pipeline',
        python_callable = post.iniciar_pipeline
    )
    # 2. Importar Dados dos Livros do CSV
    tarefa_importar_dados_csv = PythonOperator(
        task_id = 'tarefa_importar_dados_csv',
        python_callable = post.obter_livros
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
        """
    )
    # 4. Inserir dados no banco
    inserir_dados_livros = PythonOperator(
        task_id='inserir_dados_livros',
        python_callable = post.inserir_dados
    )
    # > Ordem das Dependências
    tarefa_iniciar_pipeline >> tarefa_importar_dados_csv >> criar_tabela_livro >> inserir_dados_livros