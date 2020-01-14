from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.gcs_download_operator import GoogleCloudStorageDownloadOperator
from kafka import KafkaProducer

import pandas as pd
import json

GLOBAL_PATH = '/data/download.data'

def produce_data():

    path = GLOBAL_PATH
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
        count = 0

        for document in data:
            producer.send(topic, document, document['id']) 
            count += 1
        producer.flush()
        print("Se han enviado " + str(count) + " mensajes")

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    
    finally:
        producer.close()
    
    return 1

dag = DAG('ejercicio_5', description='Ejercicio 5',
          schedule_interval='0 1 * * *',
          start_date=datetime(2020, 1, 1), 
          catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

download_operator = GoogleCloudStorageDownloadOperator(task_id='downloader', 
    bucket='fictizia',
    object='breast-cancer-wisconsin.data',
    google_cloud_storage_conn_id='google_cloud_default',
    filename=GLOBAL_PATH,
    dag=dag)  

producer_operator = PythonOperator(task_id='producer', python_callable=produce_data, dag=dag)

dummy_operator >> download_operator >> producer_operator


