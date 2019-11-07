from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.connector import db_session
from database.people_table import People as ModelPeople
from graphql_relay.node.node import from_global_id
import graphene


class People(SQLAlchemyObjectType):

    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node,)


class AddPerson(graphene.Mutation):
    name = graphene.String()
    height = graphene.String()
    mass = graphene.String()
    hair_color = graphene.String()
    skin_color = graphene.String()
    eye_color = graphene.String()
    birth_year = graphene.String()
    gender = graphene.String()
    planet_id = graphene.ID()

    class Arguments:
        name = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()
        planet_id = graphene.ID()

    def mutate(self, info, id, name, height, mass, hair_color, eye_color, skin_color, birth_year, gender, planet_id):

        person = ModelPeople()

        person.name = name
        person.height = height
        person.mass = mass
        person.hair_color = hair_color
        person.eye_color = eye_color
        person.skin_color = skin_color
        person.birth_year = birth_year
        person.gender = gender
        person.planet_id = planet_id
        person.created = datetime.utcnow()
        person.updated = datetime.utcnow()

        db_session.add(person)
        db_session.commit()

        return AddPerson(id, name, height, mass, hair_color, eye_color, skin_color, birth_year, gender, planet_id)


class UpdatePerson(graphene.Mutation):

    id = graphene.ID()
    name = graphene.String()
    height = graphene.String()
    mass = graphene.String()
    hair_color = graphene.String()
    skin_color = graphene.String()
    eye_color = graphene.String()
    birth_year = graphene.String()
    gender = graphene.String()
    planet_id = graphene.ID()

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()
        planet_id = graphene.ID()

    def mutate(self, info, id, name=None, height=None, mass=None, hair_color=None, eye_color=None, skin_color=None, birth_year=None, gender=None, planet_id=None):

        real_id = from_global_id(id)[1]

        person = ModelPeople.query.filter(ModelPeople.id == real_id).first()

        if person is not None:

            if name is not None:
                person.name = name
            if height is not None:
                person.height = height
            if mass is not None:
                person.mass = mass
            if hair_color is not None:
                person.hair_color = hair_color
            if eye_color is not None:
                person.eye_color = eye_color
            if birth_year is not None:
                person.birth_year = birth_year
            if planet_id is not None:
                person.planet_id = planet_id

            person.updated = datetime.utcnow()

            db_session.commit()

        return UpdatePerson(id, name, height, mass, hair_color, eye_color, skin_color, birth_year, gender, planet_id)


class DeletePerson(graphene.Mutation):
    id = graphene.ID()


    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):

        real_id = from_global_id(id)[1]

        db_session.query(ModelPeople).filter_by(id=real_id).delete()
        db_session.commit()

        return DeletePerson(id=None)
