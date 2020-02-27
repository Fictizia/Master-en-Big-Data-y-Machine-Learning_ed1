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
from joblib import dump
import sklearn.datasets as datasets
from google.cloud import storage

import pandas as pd
import numpy as np
import os

TRAINED_MODEL_PATH = '../../models'
TRAINED_MODEL_NAME = 'iris-trained'
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


raw_data = datasets.load_iris()

features_names = list()

for feature in raw_data['feature_names']:
    features_names.append(feature)

features_names.append('FEATURE')

data = pd.DataFrame(data=np.c_[raw_data['data'], raw_data['target']], columns=features_names)

X = np.array(data[["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]])
y = np.array(data['FEATURE'])

final_model = KMeans(n_clusters=3).fit(X)
centroids = final_model.cluster_centers_

file_name = TRAINED_MODEL_NAME + '.joblib'
file_local_path = os.path.join(TRAINED_MODEL_PATH, file_name)
file_remote_path = os.path.join(BLOB_FOLDER, file_name)

mode = 0o777

if not os.path.exists(TRAINED_MODEL_PATH):
    os.mkdir(TRAINED_MODEL_PATH, mode)

error = dump(final_model, file_local_path)

if error is not None:
    gcs_handler = GCSHandler('../../credentials/credentials.json')
    gcs_handler.load_bucket('fictizia')
    gcs_handler.upload_file(file_local_path, file_remote_path)
