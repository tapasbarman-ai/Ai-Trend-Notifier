from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.langgraph.graph import run_pipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ai_trend_pipeline',
    default_args=default_args,
    description='Daily AI trend analysis pipeline',
    schedule_interval='0 9 * * *',  # Daily at 9 AM
    catchup=False
)

def execute_pipeline():
    run_pipeline()

task = PythonOperator(
    task_id='run_ai_trend_pipeline',
    python_callable=execute_pipeline,
    dag=dag
)
