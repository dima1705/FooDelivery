import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

burger_dag = DAG('burger_dag', start_date=datetime.datetime.now())

t1 = BashOperator(
    task_id='print_dirs',
    bash_command='ls -la',
    dag=burger_dag
)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    dag=burger_dag
)

t3 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=burger_dag
)

t1 >> t2 >> t3