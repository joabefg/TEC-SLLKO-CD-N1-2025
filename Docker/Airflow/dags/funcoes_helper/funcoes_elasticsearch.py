from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd
from airflow.hooks.base import BaseHook
from elasticsearch import Elasticsearch

def extrair_dados(ti):
    pg_hook = PostgresHook(postgres_conn_id = 'postgres_connection')
    conn = pg_hook.get_conn()
    try:
        dataframe = pd.read_sql("SELECT isbn, titulo, autor, publicacao, preco FROM livro;", conn)
        ti.xcom_push(key= 'livros_elastic', value =  dataframe.to_dict('records'))
    except Exception as e:
        print(f"Erro ao realizar query postgres {e}")
        raise
    finally:
        conn.close()

def carregar_dados(ti):
    # Cofigurar conexão
    es_hook = BaseHook.get_connection('elastic_connection')
    conn = Elasticsearch(
        hosts=[{
            'host': conn.host,
            'port': conn.port,
            'scheme': conn.schema
        }],
        http_auth=(conn.login, es_hook.password) if
        es_hook.login else None,
    )
    try:
        dados_livros_list = ti.xcom_pull(
            key = 'livros_elastic',
            task_ids = 'tarefa_extracao'
        )
        dataframe = pd.DataFrame(dados_livros_list)
        for i, r in dataframe.interrows():
            doc = r.to_dict()
            res  = conn.index(index="livro", documento = doc)
    except Exception as e:
        print(f"Erro durante indexação; {e}")
        raise