from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'Yassine',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def greet(age, ti):
    name = ti.xcom_pull(task_ids='get_name') #task_instance
    print(f"Hello world! My name is {name}," f"and Im {age} years old")

def get_name():
    return "Amine"

with DAG(
    default_args=default_args,
    dag_id= "our_dag_with_python_operator_v04",
    description="Our first dag using python operator",
    start_date= datetime(2024, 7, 23),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        op_kwargs={'age': 22}
    )
    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name,
    )

    task2 >> task1