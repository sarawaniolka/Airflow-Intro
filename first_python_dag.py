from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator


default_args={
    'owner': 'Sara',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

def greet(name, age):
    print(f"Hello World! My name is {name}, "
          f"and I am {age} years old.")


with DAG(
    dag_id='my_first-python-dag',
    default_args=default_args,
    description='My first dag using the python operator.',
    start_date=datetime(2022,8,1),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs = {'name': 'Sara', 'age': 24}
    )
    
    