#!/usr/bin/env python3
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


import pandas as pd
import json
from pymongo import MongoClient

raw_data = pd.read_csv("../data/cancer.csv", ',', header=0)

tmp = raw_data.to_json(orient='records')
data = json.loads(tmp)

HOST = '172.18.1.3'
PORT = 27017
DATABASE = 'fictizia'
COLLECTION = 'data'

client = MongoClient(HOST, int(PORT))
database = client[DATABASE][COLLECTION]

for document in data:
    database.insert_one(document)

exit(0)




