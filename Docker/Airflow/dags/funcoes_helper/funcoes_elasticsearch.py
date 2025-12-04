from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd

def extrair_dados(ti):
    pg_hook = PostgresHook(postgres_conn_id = 'postgres_connection')
    conn = pg_hook.get_conn()
    try:
        dataframe = pd.read_sql("SELECT isbn, titulo, autor, publicacao, preco FROM livro;", conn)
        ti.xcom_push(key = 'livros_elastic', value = dataframe.to_dict('records'))
    except Exception as e:
        print(f"Erro ao realizar query postgres: {e}")
        raise
    finally:
        conn.close()