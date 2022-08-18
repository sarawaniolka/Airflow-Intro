# prints simple messages

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'Sara',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='my_first-dag',
    default_args=default_args,
    description='My first dag.',
    start_date=datetime(2022,8,1),
    schedule_interval='@daily'
    ) as dag:
    
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task"
    )
    
    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo 2nd task, running after the 1st one"
    )
    
    task1 >> task2
    