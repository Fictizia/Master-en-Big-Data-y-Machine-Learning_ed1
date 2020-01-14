from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from kafka import KafkaProducer

import pandas as pd
import json


def convert_data():

    path = '/data/breast-cancer-wisconsin.data'
    hostname = '172.30.1.4'
    port = 9092

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
    tmp = raw_data.to_json(orient='records')
    data = json.loads(tmp)

    topic = 'fictizia'

    try:
        producer = KafkaProducer(bootstrap_servers=hostname+':'+str(port),
                                 key_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                 value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                 retries=3)

        for document in data:
            producer.send(topic, document, document['id']) 
        producer.flush()

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    
    return 1

dag = DAG('ejercicio_2', description='Ejercicio 2',
          schedule_interval='0 1 * * *',
          start_date=datetime(2020, 1, 1), 
          catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

conversor_operator = PythonOperator(task_id='conversor', python_callable=convert_data, dag=dag)

dummy_operator >> conversor_operator



