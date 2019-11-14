#!/usr/bin/env python3

import pandas as pd
import json
from pymongo import MongoClient

raw_data = pd.read_csv("../data/osc.csv", ',', header=0)

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




