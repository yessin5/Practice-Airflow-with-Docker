from datetime import datetime, timedelta

from airflow import DAG


default_args = {
    'owner':'Yassine',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}

with DAG(dag_id = 'dag_with_minio_s3_V01',
         default_args = default_args,
         start_date= datetime(2024, 8, 02),
         schedule_interval = '@daily'
         )as dag:
    task1 = PostgresOperator(
        task_id = 'create_postgres_table',
        postgres_conn_id = 'postgres_localhost',
        sql = """
            create table if not exists dag_runs (
            dt date,
            dag_id character varying,
            primary key(dt, dag_id)
            )
            """
    )