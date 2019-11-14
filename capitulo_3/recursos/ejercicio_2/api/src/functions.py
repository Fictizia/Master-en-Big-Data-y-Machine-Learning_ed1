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

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson import json_util
from bson.objectid import ObjectId

import json

HOST = '172.18.1.3' #IP del servidor mongo
PORT = 27017
DATABASE = 'fictizia'
COLLECTION = 'data'

client = MongoClient(HOST, int(PORT))
database = client[DATABASE][COLLECTION]

def analysis():
    
    filter = {}
    projections = {}

    documents = database.find(filter)
    return json.loads(json_util.dumps(documents)), 200

def get_analysis(id):
    if id is not None:
        filter = {'id':id}
        projections = {}

        documents = database.find(filter)
        return json.loads(json_util.dumps(documents)), 200
    else:
        return {'No existe ningún registro con id' + str(id)}, 404
