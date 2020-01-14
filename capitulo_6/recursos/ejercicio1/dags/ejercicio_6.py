from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.gcs_download_operator import GoogleCloudStorageDownloadOperator
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
from kafka import KafkaProducer
from kafka import KafkaConsumer

import pandas as pd
import json

GLOBAL_PATH = '/data/download.data'
GLOBAL_OUTPUT_PATH = '/data/upload.json'
TOPIC = 'fictizia'
HOSTNAME = '172.30.1.4'
PORT = 9092

def produce_data():

    path = GLOBAL_PATH

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

    try:
        producer = KafkaProducer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 key_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                 value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                 retries=3)
        count = 0

        for document in data:
            producer.send(TOPIC, document, document['id']) 
            count += 1
        producer.flush()
        print("Se han enviado " + str(count) + " mensajes")

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    
    finally:
        producer.close()
    
    return 1

def consume_data():

    try:

        output = GLOBAL_OUTPUT_PATH

        consumer = KafkaConsumer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True)
        consumer.subscribe([TOPIC])
        
        f = open(output, "w")
        messages = 0

        for message in consumer:

            m = message.value.decode("utf-8")
            print(m + '\n')
            f.write(m)
            messages+=1

            if messages > 650:
                break

        f.close()
    
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex)) 

    return 2


dag = DAG('ejercicio_6', description='Ejercicio 6',
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

load_operator = FileToGoogleCloudStorageOperator(task_id='uploader', 
    bucket='fictizia',
    src=GLOBAL_OUTPUT_PATH,
    dst='my_file.json',
    google_cloud_storage_conn_id='google_cloud_default',
    dag=dag)  

producer_operator = PythonOperator(task_id='producer', python_callable=produce_data, dag=dag)
consumer_operator = PythonOperator(task_id='consumer', python_callable=consume_data, dag=dag)


download_operator >> producer_operator >> consumer_operator >> load_operator


