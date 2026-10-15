from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="online_retail_batch_pipeline",
    default_args=default_args,
    description="Batch ETL pipeline for Online Retail data using S3, Python ETL, and Athena",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["aws", "airflow", "batch", "etl"],
) as dag:

    run_etl = BashOperator(
        task_id="run_online_retail_etl",
        bash_command="python /home/ec2-user/airflow/etl/online_retail_etl.py",
    )

    run_etl
