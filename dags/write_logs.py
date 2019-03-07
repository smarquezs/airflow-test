from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import logging
from datetime import datetime

def print_file():
    # raise Exception
    file = open('/tmp/file.txt', 'a')
    file.write('New line added!' + "\n")
    return None

def print_log():
    logging.info('File wrote')
    return None

dag = DAG('write_logs', description='Write a simple file',
          schedule_interval='* * * * *',
          start_date=datetime(2019, 3, 6), catchup=False)

write_file_operator = PythonOperator(task_id='write_file', python_callable=print_file, dag=dag)
print_log_operator = PythonOperator(task_id='print_log', python_callable=print_log, dag=dag)

write_file_operator >> print_log_operator
