from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import random
from airflow.providers.postgres.hooks.postgres import PostgresHook

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
    publicacao_limpa = dataframe_livros['Year-Of-Publication'].replace(0, np.nan)
    publicacao_concatenada = publicacao_limpa.astype(str).str.replace('.0', '', regex=False)+'-01-01'
    dataframe_livros['ano'] = pd.to_datetime(publicacao_concatenada, errors='coerce')
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
        postgres_hook.run(sql, parameters=(livro['ISBN'], livro['Book-Title'], livro['Book-Author'], livro['ano'], livro['Publisher'], livro['Image-URL-S'], livro['Preco']))