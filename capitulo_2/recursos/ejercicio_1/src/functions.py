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

import json


def load_data(file_name):

    tmp_data = dict()

    with open(file_name, 'r') as data_file:
        raw_data = json.load(data_file)

        for instance in raw_data:
            tmp_data[instance['id']] = instance
    
    return tmp_data


DATA = load_data('./data/data.json')


def experiments():
    if len(DATA) == 0:
        init()   
    return DATA, 200


def add_experiment(id,
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

    DATA[id] = {
        "id": id,
        "clump_thickness": clump_thickness,
        "unif_cell_size": unif_cell_size,
        "unif_cell_shape": unif_cell_shape,
        "marg_adhesion": marg_adhesion,
        "single_epith_cell_size": single_epith_cell_size,
        "bare_nuclei": bare_nuclei,
        "bland_chrom": bland_chrom,
        "norm_nucleoli": norm_nucleoli,
        "mitoses": mitoses,
        "class": class_value
    }
    
    return DATA[id], 200


def get_experiment(id):
    if id in DATA.keys():
        return DATA[id], 200
    else:
        return {'No existe ningún registro con id' + str(id)}, 404


def delete_experiment(id):
    if id in DATA.keys():
        del DATA[id]
        return {}, 204
    else:
        return {'No existe ningún registro con id' + str(id)}, 404


def update_experiment(id,
                      clump_thickness=None,
                      unif_cell_size=None,
                      unif_cell_shape=None,
                      marg_adhesion=None,
                      single_epith_cell_size=None,
                      bare_nuclei=None,
                      bland_chrom=None,
                      norm_nucleoli=None,
                      mitoses=None,
                      class_value=None
                      ):
    if id in DATA.keys():
        DATA[id]['class'] = class_value
        return DATA[id], 200
    else:
        return {'No existe ningún registro con id' + str(id)}, 404
