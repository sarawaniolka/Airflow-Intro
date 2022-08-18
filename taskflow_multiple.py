from email.policy import default
from airflow import DAG
from datetime import datetime, timedelta
from airflow.decorators import dag, task


defaults_args={
    'owner': 'Sara',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


# a dag decorator
@dag(dag_id='dag_with_taskflow',
     defaults_args=defaults_args,
     start_date=datetime(2022,8,1),
     schedule_interval='@daily')

def hello_world_etl():
    
    
    @task(multiple_outputs=True)
    def get_name():
        return {'first_name' = 'Sara',
                'last_name' = 'Swan'}
    
    @task()
    def get_age():
        return 24
    
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello, my name is {first_name} {last_name}"
              f" and I am {age} yo.")
        
    
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'], last_name=name_dict['last_name'], age=age)
    
greet_dag = hello_world_etl()