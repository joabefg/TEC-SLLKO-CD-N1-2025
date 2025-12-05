from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import funcoes_helper.funcoes_elasticsearch as funcoes
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 12, 3),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': None
}

with DAG(
    dag_id = 'etl_elasticsearch',
    default_args = default_args,
    catchup = False,
) as dag:
    #1. Tarefa de Extração
    tarefa_extracao = PythonOperator(
        task_id = 'tarefa_extracao',
        python_callable = funcoes.extrair_dados
    )
    # 2. Tarefa de Carregamento 
    tarefa_carregamento = PythonOperator(
        task_id = 'tarefa_carregamento',
        python_callable = funcoes.carregar_dados
    )
    
    # Ordem de Dependência 
    tarefa_extracao >> tarefa_carregamento