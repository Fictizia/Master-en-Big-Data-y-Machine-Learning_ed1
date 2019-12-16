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

HOST = '172.20.1.6' #IP del servidor mongo
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
    
def add_analysis(id,
                   clump_thickness,
                   unif_cell_size,
                   unif_cell_shape,
                   marg_adhesion,
                   single_epith_cell_size,
                   bare_nuclei,
                   bland_chrom,
                   norm_nucleoli,
                   mitoses,
                   class_value):
    
    result = database.find_one({'id':id})

    if result is None:
        document = dict()

        document['id'] = id
        document['unif_cell_size'] = unif_cell_size
        document['unif_cell_shape'] = unif_cell_shape
        document['marg_adhesion'] = marg_adhesion
        document['single_epith_cell_size'] = single_epith_cell_size
        document['bare_nuclei'] = bare_nuclei
        document['bland_chrom'] = bland_chrom
        document['norm_nucleoli'] = norm_nucleoli
        document['mitoses'] = mitoses
        document['class'] = class_value

        result = database.insert_one(document)
        document = database.find_one({'_id':result.inserted_id})

        return json.loads(json_util.dumps(document)), 200
    else:
        return 'Existe un registro con el id ' + str(id) + '.', 404

def delete_analysis(id):
    
    document = database.find_one({'id':id})

    if document is not None:
        result = database.delete_one({'id':id})
        return 'El análisis con id ' + id + ' se ha eliminado correctamente.', 200
    else:
        return 'No existe un registro con el id ' + id + '.', 404

def update_analysis(id):   
    return {}, 200
