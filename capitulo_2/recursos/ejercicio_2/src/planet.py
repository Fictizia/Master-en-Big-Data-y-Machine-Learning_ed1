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
from database.planet_table import Planet
from database import connector
from datetime import datetime


def get_record(planet):
    tmp = dict()

    tmp['id'] = planet.id
    tmp['name'] = planet.name
    tmp['rotation_period'] = planet.rotation_period
    tmp['orbital_period'] = planet.orbital_period
    tmp['diameter'] = planet.diameter
    tmp['climate'] = planet.climate
    tmp['gravity'] = planet.gravity
    tmp['terrain'] = planet.terrain
    tmp['surface_water'] = planet.surface_water
    tmp['population'] = planet.population
    tmp['created'] = planet.created
    tmp['edited'] = planet.edited

    return tmp


def get_all():
    result = dict()

    for planet in Planet.query.all():
        result[planet.id] = get_record(planet)

    return result, 200


def add_planet(id,
               name,
               rotation_period,
               orbital_period,
               diameter,
               climate,
               gravity,
               terrain,
               surface_water,
               population):

    planet = Planet()

    planet.name = name
    planet.rotation_period = rotation_period
    planet.orbital_period = orbital_period
    planet.diameter = diameter
    planet.climate = climate
    planet.gravity = gravity
    planet.terrain = terrain
    planet.surface_water = surface_water
    planet.population = population
    planet.created = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    connector.db_session.add(planet)
    result = connector.db_session.commit()

    if result is None:
        return get_record(planet), 200
    else:
        return {'message': 'No se ha podido crear el nuevo planeta ' + str(name)}, 404


def get_planet(id):
    planet = Planet.query.filter(Planet.id == id).first()

    if planet is None:
        return {'message': 'No existe ningún planeta con id ' + str(id)}, 404
    else:
        return get_record(planet), 200


def delete_person(id):

    Planet.query.filter(Planet.id == id).delete()
    result = connector.db_session.commit()

    if result is None:
        return {'message': 'Se ha eliminado el planeta con id ' + str(id)}, 200
    else:
        return {'message': 'No existe ningún planeta con id ' + str(id)}, 404


def update_planet(id,
                  name=None,
                  rotation_period=None,
                  orbital_period=None,
                  diameter=None,
                  climate=None,
                  gravity=None,
                  terrain=None,
                  surface_water=None,
                  population=None):

    planet = Planet.query.filter(Planet.id == id).first()

    if planet is not None:

        if name is not None:
            planet.name = name
        if rotation_period is not None:
            planet.rotation_period = rotation_period
        if orbital_period is not None:
            planet.orbital_period = orbital_period
        if diameter is not None:
            planet.diameter = diameter
        if climate is not None:
            planet.climate = climate
        if gravity is not None:
            planet.gravity = gravity
        if terrain is not None:
            planet.terrain = terrain
        if surface_water is not None:
            planet.surface_water = surface_water
        if population is not None:
            planet.population = population

        planet.updated = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        connector.db_session.commit()

        return get_record(planet), 200
    else:
        return {'message': 'No existe ningún planeta con id ' + str(id)}, 404

    return {'No existe ningún planeta con id' + str(id)}, 404
