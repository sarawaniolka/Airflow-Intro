from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

# MAX XCOM Size is 48KB

default_args={
    'owner': 'Sara',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# ti - task instance
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids="get_age", key="age")
    print(f"Hello World! My name is {first_name} {last_name}, "
          f"and I am {age} years old.")


def get_name(ti):
    ti.xcom_push(key='first_name', value='Sara')
    ti.xcom_push(key='last_name', value='Swan')

def get_age(ti):
    ti.xcom_push(key='age', value=24)

with DAG(
    dag_id='xcom-dag',
    default_args=default_args,
    description='My first dag using the python operator.',
    start_date=datetime(2022,8,1),
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
       # op_kwargs = {'age': 24}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )
    
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age,
    )
    
    [task2, task3] >> task1