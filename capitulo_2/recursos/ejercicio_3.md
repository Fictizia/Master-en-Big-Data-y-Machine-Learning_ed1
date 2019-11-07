 
![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 2 - Ejercicio 03: Creación de un API basada en GraphQL de planetas y personajes ##

El objetivo de este ejercicio es crear una API basada en GraphQL para acceder a los datos referentes a personajes y planetas de la saga de StarWars de manera que nuestro "grafo" estará formado por nodos de personajes y de planetas. Para ellos vamos a utilizar un dataset de datos y vamos a construir las diferentes funciones para el acceso y manipulación de la información. 

![Interfaz de usuario web de la API basada en graphQL](../img/ejercicio_3/resultado_ejercicio_3.png)

IMPORTANTE: A la hora de crear una API basada en GraphQL para una entorno real es necesario analizar el número de peticiones y el grado extress que sufrirá nuestro sistema con el fin de utilizar el sistema de servicio que más se adapte a sus necesidades. Este es sólo un ejercicio para comprender los fundamentos básicos de construcción de una API basada en GraphQL. 

### Recursos ###

Para el desarrollo de este ejercicio vamos a utilizar las diferentes tecnologías y recursos. En este vamos a utilizar una micro Base de Datos mediante la utilización de sql Alchemy, que nos permite crear un interfaz de acceso a diferentes tipos de Bases de Datos de forma muy sencilla. 

- [Python](https://www.python.org/) como lenguaje de programación para el desarrollo de nuestra API. 
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) como servidor de aplicaciones para desplegar nuestra API.
- [Docker](https://docs.docker.com/) para construir el contenedor donde se desplegará nuestro servidor. 
- [SQL Alchemy](https://www.sqlalchemy.org/) para el almacenamiento y manipulación de la información. 
- [Datasets de información](./ejercicio_2/src/data) donde se encuentra la información que utilizaremos para cargar la información inicial. 
- [Graphene](https://graphene-python.org/) para la construcción de graphQL sobre python
- [Graphene + SQLLAlchemy](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/) para la conexión de graphene con SQL Alchemy.

### Solución paso a paso ###

**Paso 1: Creación del proyecto**

Para la creación del proyecto se recomienda crear una nueva carpeta denominado ejercicio_1 que deberá contener los siguientes archivos y directorios.

```
drwxr-xr-x 7 momartin momartin 4096 nov  1 11:55 .
drwxr-xr-x 8 momartin momartin 4096 nov  1 11:55 ..
drwxrwxr-x 2 momartin momartin 4096 nov  1 11:54 bin
-rw-r--r-- 1 momartin momartin  288 oct 31 21:30 Dockerfile
drwxrwxr-x 2 momartin momartin 4096 nov  1 11:53 include
drwxrwxr-x 3 momartin momartin 4096 nov  1 11:53 lib
drwxrwxr-x 2 momartin momartin 4096 nov  1 11:53 local
-rw-r--r-- 1 momartin momartin  612 oct 31 21:11 requirements.txt
drwxr-xr-x 4 momartin momartin 4096 nov  1 12:56 src
```

Donde se deberán encontrar el fichero de requistos del proyecto (requirements.txt), la carpeta con el código fuente (src), el fichero de creación del contenedor (Dockerfile) y los diferentes directorios del entorno virtual. Dentro de la carperta src deberemos crear los siguientes ficheros:

```
drwxr-xr-x 5 momartin momartin 4096 nov  6 23:05 .
drwxr-xr-x 7 momartin momartin 4096 nov  6 15:03 ..
drwxrwxr-x 2 momartin momartin 4096 nov  3 12:24 data
drwxr-xr-x 4 momartin momartin 4096 nov  6 23:06 database
-rw-r--r-- 1 momartin momartin 2904 nov  6 23:05 schema_people.py
-rw-r--r-- 1 momartin momartin 2362 nov  6 23:05 schema_planet.py
-rw-r--r-- 1 momartin momartin  804 nov  6 16:28 schema.py
-rw-r--r-- 1 momartin momartin 1346 nov  6 15:48 server.py
```

Los ficheros del la carpeta src se corresponden con el servidor (server.py), las funciones con la lógica de los diferentes métodos que ofrecerá la api (schema_people.py y schema_planet.py), la configuración de los diferentes puntos de acceso (schema.py donde se definen los métodos disponibles para consulta y mutación) y los datos (data) que utilizaremos para realizar la carga inicial. La carpeta database contiene el interfaz de configuración de la "Base de datos" y los ficheros de definición de las diferentes tablas. Los diferentes ficheros que se utilizan para insertar los datos inicial se encuentra en la carpeta data. 

**Paso 2: Configuración del servidor I**

El primer paso consiste en desarrollar el código de nuestro servidor para ellos vamos a utilizar [Flask](https://flask.palletsprojects.com/en/1.1.x/) que es un paquete de python que nos permite desplegar servidor web de forma sencilla y rápida. 

__Documentación y recursos__

- [Projecto Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Documentación Flask](https://flask.palletsprojects.com/en/1.1.x/api/)
- [Projecto Swagger](https://swagger.io/)
- [Documentación Swagger](https://swagger.io/solutions/api-documentation/)
- [Construcción de APIs](https://swagger.io/solutions/api-development/)
- [Documentación SQL Alchemy](https://docs.sqlalchemy.org/en/13/)
- [Consultas con SQL Alchemy](https://docs.sqlalchemy.org/en/13/orm/query.html)

Para ellos deberemos instalar algunos paquetes utilizando pip3. 

```
pip3 install Flask flask_graphql SQLAlchemy graphene-sqlalchemy 
```

Una vez instalados estos paquetes podemos comenzar con la configuración de los diferentes elementos de nuestro servidor. 

**Paso 3: Inicializando nuestra "Base de datos"**

Para la creación de nuestra "Base de datos" tenemos que crear un fichero denominado __connector.py__ en la carpeta database en la cual se define el formato y el nombre del fichero que almacenará la información. 

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

DB_NAME = 'fictizia_ejercicio_2.db'
DB_PATH = os.path.join(os.path.dirname(__file__), DB_NAME)
DB_URI = 'sqlite:///{}'.format(DB_PATH)

engine = create_engine(DB_URI, convert_unicode=True)

Base = declarative_base()
Base.metadata.bind = engine 

db_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
Base.query = db_session.query_property() 
```



**Paso 4: Creación de tablas**

Una vez que hemos definido la base da datos debemos definir la estructura de las diferentes tablas. Para ello vamos a construir un archivo python por cada una de las tablas que vamos a utilizar, comenzaremos por la tabla planeta (planet), creando el archivo __people.py__ en la carpeta database utilizando el siguiente código:

```
from sqlalchemy import Column, Integer, String, ForeignKey
from .connector import Base
from .planet_table import Planet

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

   
    @staticmethod
    def get_dict(input):
        tmp = dict()
        for key in input:
            if key[-2:] == 'id' and input[key] != 'unknown':
                input[key] = from_global_id(input[key])[1]
            tmp[key] = input[key]
        return tmp
    
```

Para la creación de una tabla mediante SQL Alchemy debemos extender la clase Base e incluir la variable ____tablename____ indicando el nombre en SQL de la tabla, a continuación es necesario crear cada uno de los atributos como columnas (Column) indicando su nombre y tipo. Además, vamos a crear un método de tipo estático que nos permita transformar los datos que obtendremos de la entrada de las consultas de la API en un diccionario en python con el fin de poder crear, actualizar o visualizar los datos. 

**Paso 5: Configuración del servidor II **

Una vez que hemos definido todos los elementos del sistema de almacenamiento, es decir de nuestra base de datos. Pasamos a la definición del método principal del servidor, para ello hemos desarrollado el siguiente código:

```
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
```

1. Para construir nuestra API basada en GraphQL utilizaremos el paquete flask_graphql, para ello tendremos que importar el paquete y a continuación crear un objeto para nuestra aplicación (server). 
2. A continuación debemos crear una función de carga para cargar los datos de los diferentes ficheros json que almacenan la información que contendrá la base de datos. Para ello insertaremos cada uno de los elementos del fichero como objetos de tipo Planer o People en su respectiva tabla.
3. A continuación deberemos definir los recursos de nuestra API, para ello utilizaremos el archivo __schema.py__ donde describiremos los diferentes recursos que ofrecerá la API para planetas y para personajes. Además indicaremos cual será la estructura de las URI de acceso a nuestra API indicando el nombre del servicio __fictizia__, la versión __1.0__ y el recurso será el esquema utilizado por el recurso mediante la variable schema donde deberá cargarse un objeto de tipo schema. Con el fin de facilitar el uso de la API activaremos el intefaz web que ofrece el paquete flask_graphql  mediante la opción graphiql cuando se ejecuta la función add_url_rule.  
4. Para finalizar debemos arrancar nuestra aplicación mediante el método run de nuestro de nuestro objeto server indicando el puesto a través del cual se desplegará nuestra aplicación. En este caso hemos elegido el puerto 5005. 

**Paso 6: Realización de consultas**

Para la realización de consultas con el fin de obtener información tenemos que construir los métodos necesarios en el fichero __schema_people.py__ en la carpeta src. En esta caso tenemos que crear la clase que define el elemento del grafo del grafo que se utilizará para acceder y manipular la información de los personajes. Esta clase se construye extendiendo la clase SQLAlchemyObjectType, donde se debe configurar la clase Meta indicando el modelo de datos (ModelPeople es la denominación que hemos dato a la clase People de nuestro fichero people_table.py) y el interfaz de acceso a los datos que en este caso será un nodo para ello utilizaremos la clase graphene.relay.Node. 

```
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.people_table import People as ModelPeople

class People(SQLAlchemyObjectType):

    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node,)
```

Después de crear los diferentes elementos que define el esquema de acceso a los datos tenemos que definir los métodos del esquema general para ello tenemos que crear el fichero __schema.py__ en la carpeta src. En este archivo se definirán los diferentes tipos de consultas y mutaciones que podremos realizar sobre nuestra base de datos. Inicialmente debemos definir la clase __Query__ que extiende la clase graphene.ObjectType incluyendose dentre de ella todos los tipos de elementos (nodos) que tendremos disponibles para la realización de consultas. En este caso vamos a definir tres tipos de elementos:

- node que se corresponde con el nodo general del grafo.
- people que se corresponde con el nodo de acceso a la información de los personajes y es de tipo Field. 
- peopleList que corresponde con una lista de elementos de tipo people. 

Una vez definidos los elementos de la clase Query, tenemos que incluir nuestra clase al esquema creando un objeto de tipo Schema (Este objeto se corresponde con el esquema que seleccionamos al crear el recursos en el archivo server.py) e incluyendo la clase Query como el conjunto de queries ofrecidas. 

```
from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_people

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()

    people = graphene.relay.Node.Field(schema_people.People)
    peopleList = SQLAlchemyConnectionField(schema_people.People)
    
schema = graphene.Schema(query=Query)
    
```

Una vez definido el esquema podemos probar nuestra primera versión de la API. Ejecutando el siguiente comando:

```
python3 server.py
```

Una vez levantado el servidor podremos acceder a nuestra URI (http://localhost:5000/fictizia/1.0/graphql) y probar su funcionamiento realizando algunas consultas. Por ejemplo la siguiente consulta nos devolverá la lista de todos los personajes utilizando el nodo peopleList, además para cada personaje sólo obtendremos el id y el nombre:

```
query Personajes {
  peopleList{edges {
    node {
      id
      name
    }
  }}
}
```

Siendo el resultado parcial de la consulta es el siguiente (Cómo se puede observar graphql sustitiuye el id de la tabla y crea un nuevo id alfabético para los diferentes nodos, ya que cada uno de nuestros instancias de la tabla son un nodo): 

```
{
  "data": {
    "peopleList": {
      "edges": [
        {
          "node": {
            "id": "UGVvcGxlOjE=",
            "name": "Luke Skywalker",
          }
        },
        {
          "node": {
            "id": "UGVvcGxlOjI=",
            "name": "C-3PO",
          }
        },
        .......
      ]
    }
  }
}
```

Si quisieramos obtener la información de un único personaje deberíamos utilizar el campo id, para ellos deberíamos realizar una consulta como la siguiente, que nos devolvería un determinado número de campos referente al personaje con id "UGVvcGxlOjE=":

```
query Personaje {
	people(id:"UGVvcGxlOjE="){
    name hairColor birthYear
  }  
}
```

En este caso obtendríamos el siguiente resultado:

```
{
  "data": {
    "people": {
      "name": "Luke Skywalker",
      "hairColor": "blond",
      "birthYear": "19BBY"
    }
  }
}
```

Existe un amplio número de posible opciones para la construcción de consultas para la obtención de información mediante el sistema de query que ofrece graphQL que no van a ser descritas en este tutorial, pero se puede consultar la guía de utilización de [queries de graphql](https://graphql.org/learn/queries/) que también utiliza ejemplos de StarWars por lo que será más facil la construcción de queries. 

**Paso 7: Moficando la información**

Normalmente las API se suelen utilizar para la obtención de información, aúnque al igual que hicimos en el ejemplo anterior vamos a ofrece un método para la inserción, modificación y eliminación de información. Para la realización de estas operaciones es recomenzable la utilización de mutaciones. Una mutación es una cambio en la estructura de la información, por lo que este cambio se puede definir como una inserción, una actualización o una eliminación. A continuación vamos a describir como se realizará una actualización. 

En primer lugar es necesario construir un conjunto de nuevas clases en nuestro schema, por lo que modificaremos el fichero __schema_people.py__. En este caso tendremos que añadir una clase nueva denominada __UpdatePerson__ en el esquema de personas. 
```
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

```

La clase UpdatePerson será la que ejecute toda la lógica del proceso de actualización. Una vez definida la clase es necesario añadir la mutación en el esquema global de la API. Para ello es necesario modicar el archivo __schema.py__ incluyendo una nueva clase denominado mutation. 

```
from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_people

class Mutation(graphene.ObjectType):

    updatePerson = schema_people.UpdatePerson.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)  
```

Una vez definido el nuevo esquema podemos probar nuestra nueva versión de la API ejecutando el siguiente comando:

```
python3 server.py
```

Una vez levantado el servidor podremos acceder a nuestra URI (http://localhost:5000/fictizia/1.0/graphql) y realizar mutaciones de la siguiente manera. 

```
mutation ActualizarPersonaje{
  updatePerson(
    id:"UGVvcGxlOjE="
    name:"Luke Solo"
  ){
    name
  }
}
```

Obteniendo como resultado:

```
{
  "data": {
    "updatePerson": {
      "name": "Luke Solo"
    }
  }
}
```

**Paso 8: Creación del resto de operaciones**

Ahora es tu turno de finalizar el ejercicio creando los métodos de creación y eliminación de personajes y todos los métodos para los planetas. 

**Paso 9: Creación del contenedor**

Una vez que hemos creado nuestra API REST, es necesario preparla para poder ser desplegada en un contenedor, para ellos tenemos que crear el archivo de creación de la imagen mediante un Dockerfile, aunque antes es necesario congelar el estado de nuestras librerias en python con el fin de poder instalarlas correctamente en nuestro contenedor. Para ellos es necesario ejecutar el siguiente comando:

```
pip3 freeze > instructions.txt
```

A continuación debemos crear el fichero __Dockerfile__ con los siguientes comandos:

```
FROM ubuntu:18.04
MAINTAINER Moisés <moises@fictizia.com>

RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN mkdir /src
COPY src /src
WORKDIR /src
RUN pip3 install -r requirements.txt
EXPOSE 5005
CMD ["python3", "server.py"]
```

Ahora es momento de construir nuestro contenedor y ejecutarlo. Una vez seguidos estos pasos, hemos creado una sencilla API REST que se despliega en un contenedor docker. 

El código fuente de todo el ejercicio se encuentra en el siguiente [enlace](https://github.com/Fictizia/Master-en-Big-Data-y-Machine-Learning_ed1/edit/master/capitulo_2/recursos/ejercicio_3/)


