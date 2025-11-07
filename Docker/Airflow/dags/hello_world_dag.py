from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='01_hello_world_test',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily',
    catchup=False,  # Não roda para períodos passados
    default_args={
        'owner': 'airflow',
    }
) as dag:
    # Task 1: Imprime uma mensagem simples no log
    hello_task = BashOperator(
        task_id='imprimir_hello',
        bash_command='echo "Airflow funcionando! Olá, Mundo!"',
    )
    
    # Task 2: Imprime a data de execução
    date_task = BashOperator(
        task_id='imprimir_data',
        bash_command='echo "A data de execução é: {{ ds }}"',
    )

    # Definindo a dependência: ambas rodam em paralelo
    hello_task 
    date_task