from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Yassine',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='our_first_dag_v3',
    default_args=default_args,
    description='This is my first dag to write',
    start_date=datetime(2024, 7, 23),
    schedule_interval='@daily'
) as dag:

    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo hello world!'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo hey! Im task2 and i will be running after task1!'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo hey! Im task3 and i will be running after task1! at the same time with task 2'
    )

    task1 >> task2
    task1 >> task3 # or task1 >> [task2, task3]