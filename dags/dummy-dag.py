from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

args = {
    'owner': 'airflow'
}

with DAG(dag_id="simple_dag_python_operator", schedule_interval='*/1 * * * *',
    start_date=datetime(2022, 8, 1), default_args=args, catchup=False) as dag:
    
    task1 = PythonOperator(
        task_id='XXXXX',
        python_callable=lambda: print('Hello World!'))

    task1
