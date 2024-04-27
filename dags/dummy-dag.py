from airflow import DAG
from airflow.operators import BashOperator
from airflow.operators import PythonOperator
from datetime import datetime

args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 8, 1),
    'provide_content': True
}

with DAG(
    dag_id='dag_python_operator',
    schedule_interval='*/1 * * * *',
    default_args=args,
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello world from task 1"'
    )

    task2 = BashOperator(
        task_id='task_2',
        bash_command='echo "Hello world from task 2"'
    )

    task1 >> task2
