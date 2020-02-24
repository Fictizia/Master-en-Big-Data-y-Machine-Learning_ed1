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
from sklearn.cluster import KMeans
from joblib import load

import json

MODEL = '../../trainer/models/iris-trained.joblib'

model = load(MODEL)

def predict(v, x, y, z):
    
    input = [v, x, y, z]

    result = dict()
    result['class'] = int(model.predict([input])[0])

    return json.dumps(result), 200
