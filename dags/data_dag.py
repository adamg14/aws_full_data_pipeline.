from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys

print("hello world")

# get the absolute directory path of this file, and get the directory which it is stored in
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

default_args = {
    "owner": "Adam Worede",
    "start_date": datetime(2025, 6, 12),
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "data engineering", "etl", "reddit"]
)

# extract data from source
extract_data = PythonOperator(
    task_id = "data_extraction",
    python_callable=data_extraction,
    op_kwargs = {
        "file_name": f"reddit_{file_postfix}"
        "subreddit": "dataengineering",
        "time_filter": "day",
        "limit": 100
    }
)
# upload extracted to data to AWS s3 bucket
