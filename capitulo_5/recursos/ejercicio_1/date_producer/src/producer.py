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

from kafka import KafkaProducer
import pandas as pd
import json
import datetime

FILE = '../data/breast-cancer-wisconsin.data'
HOSTNAME = '172.20.1.3'
PORT = 9092

if __name__ == "__main__":

    raw_data = pd.read_csv(FILE, ',', header=0)
    data = list()

    start_date = datetime.date(2019, 1, 1)
    day = 0

    for single_data in raw_data.id: 
        tmp = dict()
        tmp['id'] = single_data
        tmp['date'] = (start_date + datetime.timedelta(days=day)).strftime('%d/%m/%Y %h:%M:%s')
        day += 1
        data.append(tmp)

    topic = 'fictizia_dates'

    try:

        producer = KafkaProducer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 key_serializer=lambda m: json.dumps(m).encode('ascii'),
                                 value_serializer=lambda m: json.dumps(m).encode('ascii'),
                                 retries=3)
        count = 0

        for document in data:
            producer.send(topic, document) 
            count += 1
        
        producer.flush()
        
        print("Se han enviado " + str(count) + " mensajes")

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    
    finally:
        producer.close()
    exit(0)