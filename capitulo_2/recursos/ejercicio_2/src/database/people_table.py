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

from sqlalchemy import Column, Integer, String, ForeignKey
from .connector import Base


class People(Base):

    __tablename__ = 'people'

    id = Column('id', Integer, primary_key=True, doc="Id del personaje")
    name = Column('name', String, doc="Nombre")
    height = Column('height', String, doc="Altura")
    mass = Column('mass', String, doc="Masa")
    hair_color = Column('hair_color', String, doc="Color de pelo")
    skin_color = Column('skin_color', String, doc="Color de piel")
    eye_color = Column('eye_color', String, doc="Color de ojos")
    birth_year = Column('birth_year', String, doc="Fecha de nacimiento")
    gender = Column('gender', String, doc="Genero")
    planet_id = Column('planet_id', Integer, ForeignKey('planet.id'), doc="Id del planeta de donde el personaje procede")
    created = Column('created', String, doc="Fecha de creación")
    edited = Column('edited', String, doc="Fecha de actualización")