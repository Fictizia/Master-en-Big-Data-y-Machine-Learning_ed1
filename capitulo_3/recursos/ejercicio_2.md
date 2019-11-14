![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 3 - Ejercicio 02: Manipulación de bases de datos documentales ##

El objetivo de este ejercicio es crear un contenedor que contenga una base de datos no sólo relacion con el fin de explotar el funcionamiento de este tipo de bases de datos. En este primer ejercicio vamos a explorar el funcionamiento de las bases de datos documentales. 


### Desplegando nuestro contenedor MongoDb

Docker nos permite desplegar de forma sencilla contenedores utilizando imágenes previamente creadas, para aprender como reutilizar estas imágenes vamos a desplegar un servidor de bases de datos MongoDB. Existe diferente formas de construir nuestro contenedor Mongo, (1) mediante la utilización de la imagen; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml)

**Paso 1.1: Descargando la imagen**

En primer lugar vamos a descarga la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes del servidor [MongoDB](https://hub.docker.com/_/mongo) disponibles en dockerhub. 

```
$ docker pull mongo:3.4-xenial
```

En este caso vamos a descargar la imagen instalada en xenial en su versión 3.4 para ello utilizamos el tag "3.4-xenial". Si no nos importa la versión o el sistema operativo que queremos instalar podemos indicar simplemente que queremos descargar mongo. 

```
$ docker pull mongo
```

A continuación comprobaremos si la imagen se ha descargado correctamente y está disponible en nuestro repositorio local de imágenes, mediante el siguiente comando:

```
$ docker images 
```


Obteniendo la siguiente salida que nos indica que hemos descargado la imagen mongo en su versión (tag) 3.4.21-xenial hace 6 semanas. 

```
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
mongo                     3.4.21-xenial       e73a2394fcf4        3 months ago        428MB
```

**Paso 1.2: Desplegandando la imagen **

Una vez que hemos descargado la imagen podemos deplegarla para levantas nuestro servidor MongoDB, mediante el siguiente comando:

```
$ docker run --name=mongo_db -p 27017:27017 -v $(pwd)/mongo_data:/data/db -d mongo
```

**Paso 2: Desplegandando la imagen mediante compose**

La otra alternativa a la creación de nuestro contenedor por linea de comando, es crear nuestro contenedor mediante un fichero de despliegue, para ello tenemos que crear nuestro fichero docker-compose.yml. Además incluiremos la configuración de red necesario para desplegar nuestro contenedor dentro de una futura red de contenedores. 

```
version: '3.4'
services:
  
  mongo:
    restart: always
    image: mongo:3.6
    container_name: mongo_db  
    ports:
      - "27017:27017"
    volumes:
      - ./mongoData:/data/db
    networks:
      fictizia:
        ipv4_address: 172.18.1.3

networks:
  fictizia:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.18.1.0/24
```

Una vez construido nuestro fichero de despliegue podemos lanzar nuestro fichero de despliegue mediante el siguiente comando:

```
$ docker-compose -f docker_compose.yml up --build -d 
```

**Paso 3: Construyendo nuestra semilla mediante fichero csv**

Una vez que hemos desplegado nuestro servidor MongoDB, tenemos que construir el sistema de carga de datos que puedes ser construido mediante un archivo csv. Para ello hay que crear un nuevo proyecto en python que debe tener la siguiente estructuctura:

```
drwxrwxr-x 9 momartin momartin 4096 nov 14 16:18 .
drwxrwxr-x 6 momartin momartin 4096 nov 14 10:58 ..
drwxrwxr-x 2 momartin momartin 4096 nov 14 16:18 bin
drwxr-xr-x 2 momartin momartin 4096 nov 14 10:02 data
-rw-rw-r-- 1 momartin momartin  250 nov 14 15:56 Dockerfile
drwxrwxr-x 2 momartin momartin 4096 nov 14 16:18 include
drwxrwxr-x 3 momartin momartin 4096 nov 14 16:18 lib
-rw-rw-r-- 1 momartin momartin   92 nov 14 16:19 requirements.txt
drwxrwxr-x 2 momartin momartin 4096 nov 14 15:35 src
```

Donde se deberán encontrar el fichero de requistos del proyecto (requirements.txt), la carpeta con el código fuente (src), el fichero de creación del contenedor (Dockerfile) y el fichero csv almacenado en la carpeta data y los diferentes directorios del entorno virtual. Dentro de la carpeta src deberemos crear nuestro fichero de semilla:

```
drwxrwxr-x 2 momartin momartin     4096 nov 14 15:35 .
drwxrwxr-x 9 momartin momartin     4096 nov 14 16:18 ..
-rwxrwxrwx 1 momartin momartin      436 nov 14 15:35 seed.py
```

El fichero seed deberá contener el código para la carga de los datos almacenados en el archivo csv. En este caso se presenta un fragmento de código python que se corresponde con un script donde los diferentes elementos de configuración podrían incluirse cómo parámetros. Además la ejecución del archivo __seed.py__ debe realizarse desde dentro de la carpeta src. 

```
#!/usr/bin/env python3

import pandas as pd
import json
from pymongo import MongoClient

raw_data = pd.read_csv("../data/cancer.csv", ',', header=0)

tmp = raw_data.to_json(orient='records')
data = json.loads(tmp)

HOST = '172.18.1.3' #IP del servidor mongo
PORT = 27017
DATABASE = 'fictizia'
COLLECTION = 'data'

client = MongoClient(HOST, int(PORT))
database = client[DATABASE][COLLECTION]

for document in data:
    database.insert_one(document)

exit(0)

```

Una vez definido nuestro script de carga, es necesario crear el fichero de construcción del contenedor que deberá incluir las siguientes acciones:

```
FROM ubuntu:18.04
RUN apt update
RUN apt install python3 python3-pip -y
RUN mkdir /app
RUN mkdir /data
RUN mkdir /app/src
COPY ./data /app/data
COPY ./requirements.txt /app
COPY ./src /app/src
WORKDIR /app
RUN pip3 install -r requirements.txt
WORKDIR /app/src
CMD ["python3", "seed.py"]
```

A continuación es necesario modificar el fichero de compose que construimos anteriormente, incluyendo la información de la máquina semilla. 

```
version: '3.4'
services:
  
  mongo:
    restart: always
    image: mongo:3.6
    container_name: mongo_db  
    ports:
      - "27017:27017"
    volumes:
      - ./mongoData:/data/db
    networks:
      fictizia:
        ipv4_address: 172.18.1.3

  mongo_seed:
    restart: on-failure
    build: ./mongo_seed_1
    container_name: mongo_seed  
    networks:
      fictizia:
        ipv4_address: 172.18.1.4

networks:
  fictizia:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.18.1.0/24
```

En este caso hemos incluido el contenedor mongo_seed la política de reinicio on-failure (en caso de fallo), que indica que el contenedor no se reiniciará una vez finalizada su ejecución a no ser que se produzca un error de ejecución. Es decir, que devuelva como resultado un valor diferente a 0. Debido a esto incluimos en el código en python la instrucción exit(0) que finaliza la ejecución del script en python con 0 sino se ha producido ningún error (Existe más información acerca de las políticas de reinicio de los contenedores en el (capitulo 2)[../../capitulo_2/clase_1.md]. Tras el despligue de nuestro fichero de compose, podemos comprobar el resultado de nuestro despligue de contenedores mediante el siguiente comando:

```
$ docker ps -a 
```

obteniéndose la siguiente salida:

```
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS             PORTS                      NAMES
0466618af434        capitulo3_mongo_seed   "python3 seed.py"        2 minutes ago       Exited (0) About a minute ago mongo_seed
52f3fe7a562c        mongo:3.6              "docker-entrypoint.s…"   22 minutes ago      Up 22 minutes                   0.0.0.0:27017->27017/tcp   mongo_db
```

Como se puede observar nuestra máquina semilla ha finalizado con existe el proceso de insercción de datos y ha finalizado su ejecución con 0. 


**Paso 4: Construyendo nuestra semilla mediante fichero json**

Cómo indicamos anteriormente es posible construir nuestro contenedor de semilla mongo utilizando las diferentes funcionalidades que ofrece MongoDB, para ello es necesario crear un fichero de despliegue que instalará una versión de mongoDB desde el repositorio de mongo. Para ello hay que crear un nuevo proyecto en python que debe tener la siguiente estructuctura:

```
drwxrwxr-x 9 momartin momartin 4096 nov 14 16:18 .
drwxrwxr-x 6 momartin momartin 4096 nov 14 10:58 ..
drwxr-xr-x 2 momartin momartin 4096 nov 14 10:02 data
-rw-rw-r-- 1 momartin momartin  250 nov 14 15:56 Dockerfile
```

Donde se deberán encontrar el fichero de creación del contenedor (Dockerfile) y el fichero json almacenado en la carpeta data. A continuación es necesario crear un script de carga utilizando el comando __mongoimport__ que se denominará __script.sh__ y constendrá el siguiente código:

```
#!/bin/bash

mongoimport --host 172.18.1.4 --port 27017 --db fictizia --collection data --drop --file /data/data.json --jsonArray
```

Una vez definido nuestro proyecto es necesario crear el fichero de construcción del contenedor que deberá incluir las siguientes acciones:

```
FROM ubuntu:16.04
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0xd68fa50fea312927
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list
RUN apt update
RUN apt install maven mongodb-org default-jdk -y
RUN mkdir /app
RUN mkdir /app/data
COPY ./data /app/data
COPY ./script.sh /app
WORKDIR /app 
CMD ["sh", "script.sh"]
```

A continuación podemos volver a utilizar nuestro fichero de desplique para desplegar los diferentes contenedores de nuestra red. Este archivo deberá contener el siguiente código:

```
version: '3.4'
services:
  
  mongo:
    restart: always
    image: mongo:3.6
    container_name: mongo_db  
    ports:
      - "27017:27017"
    volumes:
      - ./mongoData:/data/db
    networks:
      fictizia:
        ipv4_address: 172.18.1.3

  mongo_seed:
    restart: on-failure
    build: ./mongo_seed_2
    container_name: mongo_seed  
    networks:
      fictizia:
        ipv4_address: 172.18.1.4

networks:
  fictizia:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.18.1.0/24
```

**Paso 5: Accediendo a nuestros datos mediante un API REST**

Una vez que hemos definido nuestros contenedores de carga, vamos a construir una API REST para acceder a los datos de nuestra base de datos mongo, construyendo una API REST con dos métodos de acceso. Para ello es necesario crear un nuevo proyecto la creación del proyecto se recomienda crear una nueva carpeta denominado __api__ que deberá contener los siguientes archivos y directorios. 

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
drwxr-xr-x 4 momartin momartin 4096 nov  1 12:56 .
drwxr-xr-x 7 momartin momartin 4096 nov  1 11:55 ..
-rw-r--r-- 1 momartin momartin 8576 nov  1 12:38 api.json
-rw-r--r-- 1 momartin momartin 2910 nov  1 12:56 functions.py
-rw-r--r-- 1 momartin momartin  924 nov  1 12:56 server.py
```

Los ficheros del la carpeta src se corresponde con el servidor (server.py), las funciones con la lógica de los diferentes recursos, la configuración de la API REST.

**Paso 6: Configuración del servidor**

El primer paso consiste en desarrollar el código de nuestro servidor para ellos vamos a utilizar [Flask](https://flask.palletsprojects.com/en/1.1.x/) que es un paquete de python que nos permite desplegar servidor web de forma sencilla y rápido. 

__Documentación y recursos__

- [Projecto Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Documentación Flask](https://flask.palletsprojects.com/en/1.1.x/api/)
- [Projecto Swagger](https://swagger.io/)
- [Documentación Swagger](https://swagger.io/solutions/api-documentation/)
- [Construcción de APIs](https://swagger.io/solutions/api-development/)

Para ellos deberemos instalar algunos paquetes utilizando pip3. 

```
pip3 install Flask connexion connexion[swagger-ui]
```

Una vez instalados estos paquetes podemos comenzar con la configuración de nuestro servidor en el fichero server.py. Si no los creastes en el paso anterior, es momento de crear este archivo y seguir los siguientes pasos:

```
import connexion

server = connexion.App(__name__, options= {"swagger_ui": True})
server.add_api('api.json', base_path='/fictizia/1.0')

if __name__ == "__main__":
    server.run(port=5005)
    exit(0)
```

1. Para construir nuestra API REST utilizaremos el paquete connexion, para ello tendremos que importar el paquete y a continuación crear un objeto para nuestra aplicación (server) indicando que se debe activar el interfaz de usuario mediante la opción swagger_ui. 
2. A continuación deberemos definir nuestra API, para ello utilizaremos el archivo __api.json__ donde describiremos los diferentes recursos de nuestra API y además indicaremos cual será la estructura de las URI de acceso a nuestra API indicando el nombre del servicio __fictizia__ y la versión __1.0__. 
3. Para finalizar debemos arrancar nuestra aplicación mediante el método run de nuestro de nuestro objeto server indicando el puesto a través del cual se desplegará nuestra aplicación. En este caso hemos elegido el puerto 5005. 

**Paso 7: Visualización de los resultados**

Una vez construido los elementos básicos de nuestro servidor vamos a comenzar con la construcción de la API REST. Para ellos vamos a construir el recursos analisis, cuya URI será la siguiente:

```
http://localhost:5005/fictizia/1.0/analisis
```

Para construir el recurso, primero debemos crear la descripción del recursos en fichero api.json mediante el siguiente framento de código:

```
{
    "swagger": "2.0",
    "info": {
        "description": "Mi tercera api",
        "version": "1.0",
        "title": "API REST Capitulo 2"
    },
    "paths":{
        "/analysis": {
            "get": {
                "operationId": "functions.analysis",
                "tags": ["Experiments"], 
                "responses": {
                    "200": {
                        "description": "Se ha procesado la petición correctamente",
                        "schema": {
                            "type": "object"
                        }
                    },
                } 
            }
        }
    }
}
```

Este fragmento de json define la estructura básica de la API (descripción, versión, title) y la estructura de los diferentes recursos como elementos de path. En ese caso hemos creado un recurso al que se accede a través de __experiments__ en la URI mediante una operación get y utilizando para generar el contenido de la respuesta el método experiments del fichero functions.py. Siendo el código de este fichero el siguiente:

```
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson import json_util
from bson.objectid import ObjectId

import json

HOST = '172.18.1.3' #IP del servidor mongo
PORT = 27017
DATABASE = 'fictizia'
COLLECTION = 'data'

client = MongoClient(HOST, int(PORT))
database = client[DATABASE][COLLECTION]

def analysis():
    
    filter = {}
    projections = {}

    documents = database.find(filter)
    return json.loads(json_util.dumps(documents)), 200
```

Esta función devuelve el contenido de la variable DATA con un código 200. 

**Paso 8: Visualización del resultado de un análisis**

A continuación vamos a construir el recursos que nos permitirá obtener la información de un determinado análisis utilizando su Id, donde la URI será la siguiente:

```
http://localhost:5005/fictizia/1.0/experiments/1002025
```

Para construir el recurso, primero debemos crear la descripción del recursos en fichero api.json mediante el siguiente framento de código:

```
"/analisis/{id}": {
    "get": {
        "operationId": "functions.get_analysis",
        "tags": ["Análisis"], 
        "parameters":[
            {   
                "name": "id",
                "in": "path",
                "required": true,
                "type": "integer",
                "default": 23456
            }
        ],
        "responses": {
            "200": {
                "description": "Se ha procesado la petición correctamente",
                "schema": {
                    "type": "object"
                }
            },
            "404": {
                "description": "Error",
                "schema": {
                    "type": "object"
                }
            }
        } 
    }
}
```

En este caso hemos construido un nuevo recursos incluyendo un parametro que se incluye el la URI. Este parámetro se corresponde con el id, para ello hemos incluio la descripción del parámetro en el array de parámetros indicando sus caractersticas básicas, siendo las más importantes la forma de entrada del parámetro a partir de la URI definiéndolo mediante la opción __in__ con el valor __patch__ y la obligatoriedad del parámetro mediante la opción __required__. Además en este caso hemos definido dos posible respuestas: (1) 200 cuando existe el resultado; y (2) 404 cuando no exista el resultado con el id indicado como parámetro. En este caso el código desarrollado para la generación de las diferentes respuestas es el siguiente:

```
def get_analysis(id):
    if id is not None:
        filter = {'id':id}
        projections = {}

        documents = database.find(filter)
        return json.loads(json_util.dumps(documents)), 200
    else:
        return {'No existe ningún registro con id' + str(id)}, 404
```

**Paso 9: Actualización del fichero de despliegue**

Una vez finalizada la API REST es necesario incluir la información de despliegue en el fichero docker-compose.yml.

```
version: '3.4'
services:
  
  mongo:
    restart: always
    image: mongo:3.6
    container_name: mongo_db  
    ports:
      - "27017:27017"
    volumes:
      - ./mongoData:/data/db
    networks:
      fictizia:
        ipv4_address: 172.18.1.3

  mongo_seed:
    restart: on-failure
    build: ./mongo_seed_1
    container_name: mongo_seed  
    networks:
      fictizia:
        ipv4_address: 172.18.1.4

  mongo_api:
    restart: always
    build: ./api
    container_name: api 
    ports:
      - "5005:5005" 
    networks:
      fictizia:
        ipv4_address: 172.18.1.5

networks:
  fictizia:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.18.1.0/24
```
