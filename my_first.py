from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator


def hello():
    print("helllo!!!!")

with DAG(dag_id="recentdag",
    start_date=datetime(2024,1,22),
    schedule_interval="*/5 * * * *",
    catchup=False) as dag:

    first_task = PythonOperator(
        task_id = "first_task",
        python_callable = hello
    )

first_task

