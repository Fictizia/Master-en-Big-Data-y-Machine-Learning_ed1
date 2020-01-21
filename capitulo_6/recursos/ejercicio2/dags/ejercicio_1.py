#/bin/env python3
# ==============================================================================
# Copyright (c) Moises Martinez by Fictizia. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.gcs_download_operator import GoogleCloudStorageDownloadOperator
from airflow.contrib.operators.file_to_gcs import FileToGoogleCloudStorageOperator
from kafka import KafkaProducer
from kafka import KafkaConsumer
from imgaug import augmenters as iaa

import imageio
import numpy
import os
import pandas as pd
import json

GLOBAL_PATH = '/data/download.data'
IMAGE_INPUT_PATH = '/data'
IMAGE_OUTPUT_PATH = '/augmneted_data/'
GLOBAL_OUTPUT_PATH = '/data/upload.json'
TOPIC = 'fictizia'
HOSTNAME = '172.30.1.4'
PORT = 9092

def data_augmentation():
    print('hola')


dag = DAG('ejercicio_1', description='Ejercicio 1 - clase 2',
          schedule_interval='0 1 * * *',
          start_date=datetime(2020, 1, 1),
          catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

augmented_operator = PythonOperator(task_id='augmentation', python_callable=data_augmentation, dag=dag)
