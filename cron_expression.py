# https://crontab.guru/

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args={
    'owner': 'Sara',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='my_first-dag',
    default_args=default_args,
    description='My first dag.',
    start_date=datetime(2022,8,1),
    schedule_interval='0 3 * * Tue,Fri' # on Tuesdays and Fridays at 3 AM
    ) as dag:
    
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo dag with cron expression"
    )
    
