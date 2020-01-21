from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.gcs_download_operator import GoogleCloudStorageDownloadOperator
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
from kafka import KafkaProducer
from kafka import KafkaConsumer
from imgaug import augmenters as iaa
from google.cloud import storage

import imageio
import numpy
import os
import pandas as pd
import json

numpy.random.bit_generator = numpy.random._bit_generator

IMAGE_INPUT_PATH = '/data/'
IMAGE_OUTPUT_PATH = '/new_data/'
CREDENTIALS_PATH = '/credentials/gcs.json'
GS_PATH = 'fictizia'
TOPIC = 'fictizia'
HOSTNAME = '172.30.1.4'
PORT = 9092

class GCS_handler():

    def __init__(self, credentials_file):
        self.__client = storage.Client.from_service_account_json(credentials_file)

    def get_bucket(self, name):
        return self.__client.get_bucket(name)

    def get_blob(self, bucket, path):
        return bucket.blob(path)

class Augmentations:

    def __init__(self, rotations = [15], scales=[25]):

        self.__output = IMAGE_OUTPUT_PATH
        self.__filters = dict()

        for value in rotations:
             self.__filters['rotation_' + str(value)] = iaa.Affine(rotate=value)

        for value in scales:
             self.__filters['scale_' + str(value)] = iaa.Affine(scale=value)
    
        self.__filters['grey'] = iaa.Grayscale(alpha=1.0)
        self.__filters['half_grey'] = iaa.Grayscale(alpha=0.5)
        self.__filters['flip_h'] = iaa.Fliplr(1.0)
        self.__filters['flip_v'] = iaa.Flipud(1.0)

    @property
    def output_folder(self):
        return self.__output

    def get_filters(self):
        return self.__filters.items()


def data_augmentation():

    augs = Augmentations([15, 30, 45, 60, 75, 90], [0.25, 0.50, 0.75])

    for base, dirs, files in os.walk(IMAGE_INPUT_PATH):
        for file in files:
            image = imageio.imread(base + '/' +  file)

            name = file.split('.')[0]
            ext = file.split('.')[1]

            for id, filter in augs.get_filters():
                image_augmented = filter.augment_images([image])[0]
                imageio.imwrite(augs.output_folder + name + '_' + id + '.' + ext, image_augmented)

def data_uploader():

    connector = GCS_handler(CREDENTIALS_PATH)

    bucket = connector.get_bucket(GS_PATH)

    for base, dirs, files in os.walk(IMAGE_OUTPUT_PATH):
        for file in files:
            blob = connector.get_blob(bucket, 'images/' + file)
            blob.upload_from_filename(base + file)
            

dag = DAG('ejercicio_2', description='Ejercicio 2 - clase 2',
          schedule_interval='0 1 * * *',
          start_date=datetime(2020, 1, 1),
          catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

augmented_operator = PythonOperator(task_id='augmentation', python_callable=data_augmentation, dag=dag)

file_updloader_operator = PythonOperator(task_id='uploader', python_callable=data_uploader, dag=dag)

dummy_operator > augmented_operator > file_updloader_operator