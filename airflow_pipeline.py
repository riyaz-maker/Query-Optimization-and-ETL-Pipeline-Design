from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'dev',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email': ['riyazshaik.147@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Initialize the DAG
dag = DAG(
    'etl_pipeline_dag',
    default_args=default_args,
    description='Orchestrates ETL pipeline for SQL Query Optimization & ETL Pipeline Design project',
    schedule=timedelta(days=1),
    catchup=False
)

# Task 1: Data extraction & loading
def extract_and_load():
    subprocess.run(["python", "data_preprocessing.py"], check=True)

t1 = PythonOperator(
    task_id='extract_and_load',
    python_callable=extract_and_load,
    dag=dag,
)

# Task 2: Data transformation
def transform_data():
    subprocess.run(["python", "data_transformation.py"], check=True)

t2 = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

# Task 3: Data quality checks
def quality_checks():
    subprocess.run(["python", "data_quality_check.py"], check=True)

t3 = PythonOperator(
    task_id='quality_checks',
    python_callable=quality_checks,
    dag=dag,
)

# Task 4: Dashboard update
def update_dashboard():
    print("Dashboard is up-to-date!")

t4 = PythonOperator(
    task_id='update_dashboard',
    python_callable=update_dashboard,
    dag=dag,
)

t1 >> t2 >> t3 >> t4
