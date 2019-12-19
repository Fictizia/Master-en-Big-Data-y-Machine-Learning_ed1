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

from kafka import KafkaConsumer
import json
import requests

HOSTNAME = '172.20.1.3'  #Este valor dependerá del que hayamos incluido en nuestro fichero de despliegue (docker-compose)
PORT = 9092
URL = 'http://172.20.1.8:5005/fictizia/1.0/analysis'

def is_full(data):
    if len(data) == 12:
        return True
    return False

def add_data(data, value):
    for k, v in value.items():
        data[k] = v

def generate_url(url, data):
    url = url + '?'
    for k,v in data.items():
        url = url + str(k) + '=' + str(v) + '&'
    return url[:-1]


if __name__ == "__main__":

    topic_1 = 'fictizia'
    topic_2 = 'fictizia_dates'

    full_data = dict()

    try:

        consumer = KafkaConsumer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 auto_offset_reset='earliest',
                                 key_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 enable_auto_commit=True)
        
        consumer.subscribe([topic_1, topic_2])
        
        for message in consumer:

            data = message.value

            if data['id'] not in full_data:
                full_data[data['id']] = dict()
            add_data(full_data[data['id']], data)

            if is_full(full_data[data['id']]):
                url = generate_url(URL, full_data[data['id']])
                response = requests.post(url)
                if response.status_code == 400:
                    print(url)

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    finally:
        consumer.close()
    
    exit(0)