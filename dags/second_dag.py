from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from etl_script import ETL


# Définition du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='second_dag_log',
    default_args=default_args,
    description='A simple ETL pipeline with Hello World',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:
    python_task = PythonOperator(
        task_id='python_task',
        python_callable=ETL().run,
    )

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command="python /opt/airflow/dags/etl_script.py"
    )
