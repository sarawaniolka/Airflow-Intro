from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args={
    'owner': 'Sara',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_catchup',
    default_args=default_args,
    start_date=datetime(2022,8,1),
    schedule_interval='@daily',
    catchup = True
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a sample bash command!'
    )