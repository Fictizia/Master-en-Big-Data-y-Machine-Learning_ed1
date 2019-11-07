from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_planet
import schema_people


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    people = graphene.relay.Node.Field(schema_people.People)
    peopleList = SQLAlchemyConnectionField(schema_people.People)

    planet = graphene.relay.Node.Field(schema_planet.Planet)
    planetList = SQLAlchemyConnectionField(schema_planet.Planet)


class Mutation(graphene.ObjectType):

    addPerson = schema_people.AddPerson.Field()
    updatePerson = schema_people.UpdatePerson.Field()
    deletePerson = schema_people.DeletePerson.Field()

    addPlanet = schema_planet.AddPlanet.Field()
    updatePlanet = schema_planet.UpdatePlanet.Field()
    deletePlanet = schema_planet.DeletePlanet.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
