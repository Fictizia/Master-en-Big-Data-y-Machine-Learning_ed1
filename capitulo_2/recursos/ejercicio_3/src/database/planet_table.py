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

from sqlalchemy import Column, Integer, String
from .connector import Base


class Planet(Base):

    __tablename__ = 'planet'

    id = Column('id', Integer, primary_key=True, doc="Id del planeta")
    name = Column('name', String, doc="Nombre")
    rotation_period = Column('rotation_period', String, doc="Periodo de rotación")
    orbital_period = Column('orbital_period', String, doc="Periodo orbital")
    diameter = Column('diameter', String, doc="Diametro")
    climate = Column('climate', String, doc="Clima")
    gravity = Column('gravity', String, doc="Gravedad")
    terrain = Column('terrain', String, doc="Tipo de terreno")
    surface_water = Column('surface_water', String, doc="Superficie de agua")
    population = Column('population', String, doc="Población")
    created = Column('created', String, doc="Fecha de creación")
    edited = Column('edited', String, doc="Fecha de actualización")

    @staticmethod
    def get_json(data):

        tmp = dict()

        tmp['id'] = data.id
        tmp['name'] = data.name
        tmp['rotation_period'] = data.rotation_period
        tmp['orbital_period'] = data.orbital_period
        tmp['diameter'] = data.diameter
        tmp['climate'] = data.climate
        tmp['gravity'] = data.gravity
        tmp['terrain'] = data.terrain
        tmp['surface_water'] = data.surface_water
        tmp['population'] = data.population
        tmp['created'] = data.created
        tmp['edited'] = data.edited

        return tmp
