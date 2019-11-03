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

import connexion
from ast import literal_eval
from sqlalchemy.sql import text
from database.people_table import People
from database.planet_table import Planet
from database import connector
from sqlalchemy import inspect
import sys
import os


def load_database():

    connector.Base.metadata.create_all(connector.engine)

    if os.path.exists(connector.DB_PATH):

        with open('./data/planets.json', 'r') as file:
            data = literal_eval(file.read())
            for record in data:
                planet = Planet(**record)
                connector.db_session.add(planet)
            connector.db_session.commit()

        with open('./data/people.json', 'r') as file:
            data = literal_eval(file.read())
            for record in data:
                person = People(**record)
                connector.db_session.add(person)
            connector.db_session.commit()

server = connexion.App(__name__,
    options= {"swagger_ui": True})

server.add_api('api.json', 
    base_path='/fictizia/1.0')

if __name__ == "__main__":

    db = load_database()
    server.run(port=5005)
    exit(0)
