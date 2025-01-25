from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Fonction : Extraction
def extract_data():
    print("Hello World: Extract")

# Fonction : Transformation
def transform_data():
    print("Hello World: Transform")

# Fonction : Chargement
def load_data():
    print("Hello World: Load")

# Définition du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='simple_etl_hello_world',
    default_args=default_args,
    description='A simple ETL pipeline with Hello World',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load_data,
    )

    # Définir les dépendances
    extract_task >> transform_task >> load_task