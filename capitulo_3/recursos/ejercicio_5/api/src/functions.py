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

from neo4j import GraphDatabase

import json

HOST = 'localhost' #IP del servidor NEO4J
PORT = 7687
URI = 'bolt://' + HOST + ':' + str(PORT)
USER = ''
PASSWORD = ''

client = GraphDatabase.driver(URI)


def get_all_movies(tx):

    data = list()
    query = "MATCH (m:Movie) RETURN m.title as title, m.released as released, m.tagline as tagline"

    for record in tx.run(query):

        r = dict()
        r['title'] = record['title']
        r['tagline'] = record['tagline']
        r['released'] = record['released']
        data.append(r)

    return data


def movies():

    with client.session() as session:
        json_data = session.read_transaction(get_all_movies)

    return json_data, 200


def get_movie_by_title(tx, title):

    data = list()

    query = "MATCH (m:Movie)-[r:DIRECTED]->(p:Person) WHERE m.title = '" + title + "' RETURN m.title as title, m.released as released, m.tagline as tagline"

    for record in tx.run(query):

        r = dict()
        r['title'] = record['title']
        r['tagline'] = record['tagline']
        r['released'] = record['released']
        data.append(r)

    return data


def get_directors(id):
    if id is not None:
        with client.session() as session:
            json_data = session.read_transaction(get_directors_by_movie, id)
        return json_data, 200
    else:
        return {'Se debe indicar un nombre de película'}, 404


def get_directors_by_movie(tx, title):

    data = list()

    query = "MATCH (m:Movie)<-[:DIRECTED]-(p:Person) WHERE (m.title='" + title + "') RETURN p.name as name"

    for record in tx.run(query):
        r = dict()
        r['name'] = record['name']
        data.append(r)

    return data

def get_actors(id):
    if id is not None:
        with client.session() as session:
            json_data = session.read_transaction(get_actors_by_movie, id)
        return json_data, 200
    else:
        return {'Se debe indicar un nombre de película'}, 404


def get_actors_by_movie(tx, title):

    data = list()

    query = "MATCH (m:Movie)<-[a:ACTED_IN]-(p:Person) WHERE (m.title='" + title + "') RETURN p.name as name, a.roles as roles"

    for record in tx.run(query):

        print(record)

        r = dict()
        r['name'] = record['name']
        r['roles'] = record['roles']
        data.append(r)

    return data


def get_movie(id):
    if id is not None:
        with client.session() as session:
            json_data = session.read_transaction(get_movie_by_title, id)
        return json_data, 200
    else:
        return {'Se debe indicar un nombre de película'}, 404




def add_movie(id,
              tagline,
              released,):
    return {}, 200

def delete_movie(id):
    return {}, 200

def update_movie(id):
    return {}, 200
