from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd

def convert_data():

    path = '/data/breast-cancer-wisconsin.data'

    columns = [
        'id', 
        'clump_thickness', 
        'uni_cell_size',
        'cell_shape',
        'marginal_adhesion',
        'cell_size',
        'bare_nuclei',
        'bland_chromatin',
        'normal_nucleoli',
        'mitoses',
        'class_value']

    raw_data = pd.read_csv(path, ',', names=columns)
    raw_data.to_json(orient='records', path_or_buf='/data/outputs')
    
    return 1

dag = DAG('ejercicio_1', description='Ejercicio 1',
          schedule_interval='0 1 * * *',
          start_date=datetime(2020, 1, 1),
          catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

operator_conversor = PythonOperator(task_id='conversor', python_callable=convert_data, dag=dag)

dummy_operator >> operator_conversor



