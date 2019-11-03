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
from database.people_table import People
from database import connector
from datetime import datetime


def get_record(person):
    tmp = dict()

    tmp['id'] = person.id
    tmp['name'] = person.name
    tmp['height'] = person.height
    tmp['mass'] = person.mass
    tmp['hair_color'] = person.hair_color
    tmp['skin_color'] = person.skin_color
    tmp['eye_color'] = person.eye_color
    tmp['birth_year'] = person.birth_year
    tmp['gender'] = person.gender
    tmp['planet_id'] = person.planet_id
    tmp['created'] = person.created
    tmp['edited'] = person.edited

    return tmp


def get_all():
    result = dict()

    for person in People.query.all():
        result[person.id] = get_record(person)

    return result, 200


def add_person(name,
               height,
               mass,
               hair_color,
               skin_color,
               eye_color,
               birth_year,
               gender,
               planet_id):

    person = People()

    person.name = name
    person.height = height
    person.mass = mass
    person.hair_color = hair_color
    person.skin_color = skin_color
    person.eye_color = eye_color
    person.birth_year = birth_year
    person.gender = gender
    person.planet_id = planet_id
    person.created = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    connector.db_session.add(person)
    result = connector.db_session.commit()

    if result is None:
        return get_record(person), 200
    else:
        return {'message': 'No se ha podido crear el nuevo planera ' + str(name)}, 404


def get_person(id):

    person = People.query.filter(People.id == id).first()

    if person is None:
        return {'message': 'No existe ningún personaje con id ' + str(id)}, 404
    else:
        return get_record(person), 200


def delete_person(id):

    person = People.query.filter(People.id == id).delete()
    result = connector.db_session.commit()

    if result is None:
        return {'message': 'Se ha eliminado el personaje con id ' + str(id)}, 200
    else:
        return {'message': 'No existe ningún personaje con id ' + str(id)}, 404

def update_person(id,
                  name=None,
                  height=None,
                  mass=None,
                  hair_color=None,
                  skin_color=None,
                  eye_color=None,
                  birth_year=None,
                  gender=None,
                  planet_id=None):

    person = People.query.filter(People.id == id).first()

    if person is not None:

        if name is not None:
            person.name = name
        if height is not None:
            person.height = height
        if mass is not None:
            person.mass = mass
        if hair_color is not None:
            person.hair_color = hair_color
        if skin_color is not None:
            person.skin_color = skin_color
        if eye_color is not None:
            person.eye_color = eye_color
        if birth_year is not None:
            person.birth_year = birth_year
        if gender is not None:
            person.gender = gender
        if planet_id is not None:
            person.planet_id = planet_id

        person.updated = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        connector.db_session.commit()

        return get_record(person), 200
    else:
        return {'message': 'No existe ningún personaje con id ' + str(id)}, 404

