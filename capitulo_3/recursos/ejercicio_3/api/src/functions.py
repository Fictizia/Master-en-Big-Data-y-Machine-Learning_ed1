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

from google.cloud import bigquery

import json

client = bigquery.Client.from_service_account_json("./credentials/fictizia.json")

def get_row(row):

    tmp = dict()
    tmp['id'] = row.id
    tmp['clump_thickness'] = row.clump_thickness
    tmp['cell_size'] = row.cell_size
    tmp['cell_shape'] = row.cell_shape
    tmp['marg_adhesion'] = row.marginal_adhesion
    tmp['epithelial_cell_size'] = row.epithelial_cell_size
    tmp['bare_nuclei'] = row.bare_nuclei
    tmp['bland_chromatin'] = row.bland_chromatin
    tmp['norm_nucleoli'] = row.normal_nucleoli
    tmp['mitoses'] = row.mitoses
    tmp['output_class'] = row.output_class

    return tmp

def analysis():

    query = client.query("SELECT * FROM cancer.exps ORDER BY id")
    documents = query.result()

    result = list()

    for row in documents:
        result.append(get_row(row))
    return result, 200


def get_analysis(id):

    documents = client.query("SELECT * FROM cancer.exps WHERE id = " + str(id))

    result = None
    count = 0

    for row in documents:
        result = get_row(row)
        count += 1
   
    if result is None or count != 1:
        return {"message":"No existe ningún registro con id: " + str(id)}, 404
    else:
        return result, 200


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
    
    documents = client.query("SELECT id FROM cancer.exps WHERE id = " + str(id))

    found = False

    for row in documents:
        found = True

    if not found:
        query = "INSERT INTO cancer.exps (id, clump_thickness, cell_size, cell_shape, marginal_adhesion, epithelial_cell_size, bare_nuclei, bland_chromatin, normal_nucleoli, mitoses, output_class) VALUES (" + str(id) + "," + str(clump_thickness) + "," + str(unif_cell_size) + "," + str(unif_cell_shape) + "," + str(marg_adhesion) + "," + str(single_epith_cell_size) + "," + str(bare_nuclei) + "," + str(bland_chrom) + "," + str(norm_nucleoli) + "," + str(mitoses) + "," + str(class_value) + ")"
        result = client.query(query)
        result.result()

        documents = client.query("SELECT * FROM cancer.exps WHERE id = " + str(id))
        
        for row in documents:
            if row.id == id:
                found = True
            else:
                found = False

        if found:
            return get_row(row), 200
        else:
            return {"message":"No se ha podido insertar con exito el registro con id: " + str(id)}, 404
    else:
        return {"message":"Ya existe un registro con id: " + str(id)}, 404

def delete_analysis(id):

    documents = client.query("SELECT id FROM cancer.exps WHERE id = " + str(id))
    count = 0

    for row in documents:
        count += 1
        error = client.query("DELETE FROM cancer.exps WHERE id = " + str(row.id))

    if count == 1:
        return {"message":"Se ha borrado con existo el registro con id: " + str(id)}, 200
    else:
        return {"message":"No existe ningún registro con id: " + str(id)}, 404

def update_analysis(id):   
    return {}, 200