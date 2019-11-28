#/bin/env python3
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

from google.cloud import storage
import pandas as pd
import os
import requests

URL = ''
client = storage.Client.from_service_account_json('../../credentials/gcs.json')


def get_bucket(name):
    return client.get_bucket(name)


def get_blob(bucket, path):
    return bucket.get_blob(path)


def download_file(path, blob):

    destination = '{}{}'.format(path, blob.name)
    blob.download_to_filename(destination)
    return destination

def generate_params(data):
    return None

if __name__ == "__main__":

    my_bucket = get_bucket("fictizia")
    my_blob = get_blob(my_bucket, 'movies_metadata.csv')
    my_file = download_file('./', my_blob)

    data = pd.read_csv(my_file, low_memory=False)
    columns = ['homepage', 'id', 'release_date', 'tagline', 'title']
    useful_data = pd.DataFrame(data, columns=columns)

    for i in range(1, useful_data.shape[0]):

        params = generate_params(useful_data.iloc[i])
        req = requests.put(URL, params=params)

        if req.status_code != 200:
            print("error inserting movie " + useful_data.iloc[i]['title'])

    exit(0)
