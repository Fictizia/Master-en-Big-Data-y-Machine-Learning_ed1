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
URL = 'http://172.20.1.7:5005/fictizia/1.0/analysis'


def generate_url(url, data):
    url = url + '?'
    for k,v in data.items():
        url = url + str(k) + '=' + str(v) + '&'
    return url[:-1]


if __name__ == "__main__":

    topic = 'fictizia'

    try:

        consumer = KafkaConsumer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 auto_offset_reset='earliest',
                                 key_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 enable_auto_commit=True)
        
        consumer.subscribe([topic])
        for message in consumer:
            url = generate_url(URL, message.value)
            response = requests.post(url)
            if response.status_code == 400:
                print(url)

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    
    exit(0)

