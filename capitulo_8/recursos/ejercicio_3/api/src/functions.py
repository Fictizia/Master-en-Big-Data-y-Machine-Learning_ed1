# /bin/env python3
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn.cluster import KMeans
from joblib import load
from google.cloud import storage

import os

TRAINED_MODEL_PATH = '../models'
TRAINED_MODEL_NAME = 'iris-trained'
DOWNLOADED_MODEL_NAME = 'iris-loaded'
BLOB_FOLDER = 'kmeans_models'

PATH = os.path.join(os.getcwd())


class GCSHandler:

    def __init__(self, credentials_file):
        self.__client = storage.Client.from_service_account_json(credentials_file)
        self.__bucket_name_loaded = None
        self.__bucket = None

    def load_bucket(self, name):
        if name != self.__bucket_name_loaded:
            self.__bucket_name_loaded == name
            self.__bucket = self.__client.get_bucket(name)

    def get_bucket(self):
        return self.__bucket

    def download_file(self, local_path, blob_path):
        blob = self.__bucket.get_blob(blob_path)
        return blob.download_to_filename(local_path)

    def upload_file(self, local_path, blob_path):
        blob = self.__bucket.get_blob(blob_path)
        return blob.upload_from_filename(local_path)


remote_file_name = TRAINED_MODEL_NAME + '.joblib'
local_file_name = DOWNLOADED_MODEL_NAME + '.joblib'
file_local_path = os.path.join(TRAINED_MODEL_PATH, local_file_name)
file_remote_path = os.path.join(BLOB_FOLDER, remote_file_name)


if os.path.exists(file_local_path):
    os.remove(file_local_path)

gcs_handler = GCSHandler('../../credentials/credentials.json')
gcs_handler.load_bucket('fictizia')
gcs_handler.download_file(file_local_path, file_remote_path)


def predict(field_1: float, field_2: float, field_3: float, field_4: float):

    input = [[field_1, field_2, field_3, field_4]]
    output = dict()

    model: KMeans = load(file_local_path)

    try:
        output['class'] = int(model.predict(input)[0])
        return output, 200
    except Exception as e:
        return str(e), 300
