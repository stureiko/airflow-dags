from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

args = {
    'owner': 'airflow'
}

def hello():
    print('Hello World!')

# with DAG(dag_id="simple_dag_python_operator", schedule_interval='*/1 * * * *',
#     start_date=datetime(2022, 8, 1), default_args=args, catchup=False) as dag:

#     task1 = PythonOperator(
#         task_id='task_1',
#         python_callable=hello)

#     task1

dag = DAG(
    dag_id="btc_analytics",
    default_args=args,
    description='DAG btc_analytics - Task 2 Otus DE',
    start_date=datetime(2021, 7, 1),
    schedule_interval='*/1 * * * *',
    catchup=False,
)

start = DummyOperator(task_id="start", dag=dag)