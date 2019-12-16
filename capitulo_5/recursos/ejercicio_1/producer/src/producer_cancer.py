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

FILE = '../data/breast-cancer-wisconsin.data'
HOSTNAME = '172.20.1.3'
PORT = 9092

if __name__ == "__main__":

    raw_data = pd.read_csv(FILE, ',', header=0)

    tmp = raw_data.to_json(orient='records')
    data = json.loads(tmp)

    topic = 'fictizia'

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
        consumer.close()
    
    exit(0)


