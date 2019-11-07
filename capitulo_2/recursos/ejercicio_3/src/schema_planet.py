from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.connector import db_session
from database.planet_table import Planet as Planet_model
import graphene

class Planet(SQLAlchemyObjectType):

    class Meta:
        model = Planet_model
        interfaces = (graphene.relay.Node,)

class AddPlanet(graphene.Mutation):

    name = graphene.String()
    rotation_period = graphene.String()
    orbital_period = graphene.String()
    diameter = graphene.String()
    climate = graphene.String()
    gravity = graphene.String()
    terrain = graphene.String()
    surface_water = graphene.String()
    population = graphene.String()

    class Arguments:
        name = graphene.String()
        rotation_period = graphene.String()
        orbital_period = graphene.String()
        diameter = graphene.String()
        climate = graphene.String()
        gravity = graphene.String()
        terrain = graphene.String()
        surface_water = graphene.String()
        population = graphene.String()

    def mutate(self, info, id, name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population):

        planet = ModelPlanet()

        planet.name = name
        planet.rotation_period = rotation_period
        planet.orbital_period = orbital_period
        planet.diameter = diameter
        planet.climate = climate
        planet.gravity = gravity
        planet.terrain = terrain
        planet.surface_water = surface_water
        planet.population = population
        planet.created = datetime.utcnow()
        planet.updated = datetime.utcnow()

        db_session.add(planet)
        db_session.commit()

        return AddPlanet(id, name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population)


class UpdatePlanet(graphene.Mutation):

    id = graphene.ID()
    name = graphene.String()
    rotation_period = graphene.String()
    orbital_period = graphene.String()
    diameter = graphene.String()
    climate = graphene.String()
    gravity = graphene.String()
    terrain = graphene.String()
    surface_water = graphene.String()
    population = graphene.String()

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        rotation_period = graphene.String()
        orbital_period = graphene.String()
        diameter = graphene.String()
        climate = graphene.String()
        gravity = graphene.String()
        terrain = graphene.String()
        surface_water = graphene.String()
        population = graphene.String()


    def mutate(self, info, id, name=None, rotation_period=None, orbital_period=None, diameter=None, climate=None, gravity=None, terrain=None, surface_water=None, population=None):

        real_id = from_global_id(id)[1]

        planet = ModelPlanet.query.filter(ModelPlanet.id == real_id).first()

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

            planet.updated = datetime.utcnow()

            db_session.commit()

        return UpdatePlanet(id, name, rotation_period, orbital_period, diameter, climate, gravity, terrain, surface_water, population)


class DeletePlanet(graphene.Mutation):
    id = graphene.ID()


    class Arguments:
        id = graphene.ID()

    def mutate(self, info, id):

        real_id = from_global_id(id)[1]

        db_session.query(ModelPlanet).filter_by(id=real_id).delete()
        db_session.commit()

        return DeletePlanet(id=None)