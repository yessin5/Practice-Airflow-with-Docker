from airflow.decorators import dag, task 
from datetime import datetime, timedelta


default_args = {
    'owner': 'Yassine',
    'retries': 5,
    'retry_delay':timedelta(minutes = 5)
}

@dag(dag_id="dag_with_taskflowapi_v01",
     default_args=default_args,
     start_date=datetime(2024, 7, 25),
     schedule_interval='@daily')

def hello_world_etl():
    


    @task()
    def get_name():
        return "Yessin"
    @task()
    def get_age():
        return 22
    @task()
    def greet(name, age):
        print(f"Hello world, Im {name} " f"and Im {age} years old")
    
    name = get_name()
    age = get_age()
    greet(name=name, age=age)

greet_dag = hello_world_etl()