from ast import literal_eval
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from database import connector
from database.people_table import People
from database.planet_table import Planet

import os

server = Flask(__name__)

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

@server.teardown_appcontext
def shutdown_session(exception=None):
    connector.db_session.remove()


if __name__ == '__main__':

    load_database()

    server.add_url_rule('/fictizia/1.0/graphql',
                     view_func=GraphQLView.as_view('graphql',
                                                   schema=schema,
                                                   graphiql=True))
    server.run(port=5005, threaded=True)
