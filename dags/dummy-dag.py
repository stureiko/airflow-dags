from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

args = {
    'owner': 'airflow'
}

dag = DAG(
    dag_id="btc_analytics",
    default_args=args,
    description='DAG btc_analytics - Task 2 Otus DE',
    start_date=datetime(2021, 7, 1),
    schedule_interval='*/1 * * * *',
    catchup=False,
)

start = DummyOperator(task_id="start", dag=dag)