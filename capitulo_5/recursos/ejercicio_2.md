![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 5 - Ejercicio 02: Trabajando con colas de mensajes (RabbitMQ) ##

El objetivo de este ejercicio es crear una aplicación que procese la información de uno o más ficheros de datos mediante la utilización de una cola de mensajes. Esta información será almacenada a continuación en un sistema de almacenamiento externo.  
Docker nos permite desplegar de forma sencilla contenedores utilizando imágenes previamente creadas, para aprender como reutilizar estas imágenes vamos a desplegar un servicio RabbitMQ. Existen diferentes formas de construir nuestro contenedor RabbitMQ, (1) mediante la utilización de la imagen; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml). En este caso vamos a realizarlo mediante un fichero de despliegue.

**Paso 1: Descargando la imagen de RabbitMQ**

En primer lugar vamos a descargar la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes del servidor [RabbitMQ](hhttps://hub.docker.com/_/rabbitmq). En este caso, la propia compañia que desarrollado la cola de mensajes tiene un conjunto de imágenes disponibles. Para este ejercicio vamos a utilizar la versión 3.8 de tipo gestionada (rabbitmq:3.8-management). 

```
$ docker pull rabbitmq:3.8-management
```

A continuación comprobaremos si la imagen se ha descargado correctamente y está disponible en nuestro repositorio local de imágenes, mediante el siguiente comando:

```
$ docker images 
```


Obteniendo la siguiente salida que nos indica que hemos descargado la imagen mongo en su versión (tag) 3.4.21-xenial hace 6 semanas. 

```
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
rabbitmq                   3.8-management      6bd1749b8197        5 days ago          181MB
```

**Paso 2: Creando nuestro fichero de despliegue**

Una vez que hemos descargado la imagen de nuestro sistema de colas basado en RabbitMQ, podemos crear los diferentes elementos en nuestro fichero de despliegue, por lo que es necesario crear un proyecto con la siguiente estructura

```
total 32
drwxr-xr-x 10 momartin momartin 4096 dic 12 09:28 .
drwxrwxr-x  4 momartin momartin 4096 dic 11 07:30 ..
drwxrwxr-x  6 momartin momartin 4096 nov 14 17:33 api
drwxr-xr-x  2 momartin momartin 4096 dic 11 07:36 config
drwxrwxr-x  4 momartin momartin 4096 dic 11 07:53 consumer
-rw-rw-r--  1 momartin momartin 1463 dic 11 10:49 docker-compose.yml
drwxr-xr-x  4 momartin momartin 4096 dic 11 14:33 mongoData
drwxrwxr-x  5 momartin momartin 4096 dic 11 07:43 producer
drwxr-xr-x  5 momartin momartin 4096 dic 11 07:36 rabbitmq
```

Donde se deberán encontrar el fichero de compose donde se definirián los diferentes contenedores necesarios para la utilización de colas de mensajes mediante RabbitMQ y los ficheros los dos carpetas, mediante las que crearemos nuestro productor y nuestro consumidor. Una vez construido nuestro proyecto podemos pasar a definir nuestro fichero de despligue mediante docker-compose. Para ello deberemos incluir primero la configuración de una red mediante el siguiente código:

```
version: '3.4'

networks:
  fictizia_kafka:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.20.1.0/24
```

A continuación vamos la configuración de nuestro contenedor kafka. Para ello incluiremos un servicio 

```
services:
  rabbit:
    restart: always
    container_name: rabbitmq    
    image: 'rabbitmq:3-management'
    hostname: rabbitmq
    ports:
      - '15672:15672'
      - '5672:5672'
      - '5671:5671'
      - '25672:25672'
    volumes:
      - ./rabbitmq:/var/lib/rabbitmq
      - ./config:/etc/rabbitmq/rabbitmq.config
    environment: 
      - RABBITMQ_DEFAULT_USER=user
      - RABBITMQ_DEFAULT_PASS=password 
    networks:
      fictizia_kafka:
        ipv4_address: 172.20.1.3
```

Una vez construido nuestro fichero de despliegue podremos lanzar nuestro servidor de colas de mensaje RabbitMq, mediante el siguiente comando:

```
docker-compose -f docker-compose.yml up --build -d
```

Si todo ha funcionado correctamente deberemos observar los siguiente contenedores al ejecutar el comando docker ps:

```
CONTAINER ID        IMAGE                         COMMAND                  CREATED             STATUS              PORTS                                                                                                       NAMES
806eadf7a02d        rabbitmq:3-management         "docker-entrypoint.s…"   5 seconds ago       Up 2 seconds        4369/tcp, 0.0.0.0:5671-5672->5671-5672/tcp, 0.0.0.0:15672->15672/tcp, 15671/tcp, 0.0.0.0:25672->25672/tcp   rabbitmq
```

**Paso 3: Produciendo mis primeros mensajes**

Una vez que hemos desplegado nuestro servicio de colas de mensajes, deberemos construir nuestro productor con el objetivo de comenzar a ingestar información en nuestra cola de mensajes. Para ellos deberemos añadir una serie de archivos en nuestra carpeta producer. 

```
total 16
drwxrwxr-x 4 momartin momartin 4096 dic 10 06:53 .
drwxrwxr-x 4 momartin momartin 4096 dic 10 06:49 ..
-rw-rw-r-- 1 momartin momartin    0 dic 10 06:53 Dockerfile
-rw-rw-r-- 1 momartin momartin    0 dic 10 06:53 requirements.txt
drwxrwxr-x 2 momartin momartin 4096 dic 10 06:53 src
drwxrwxr-x 5 momartin momartin 4096 dic 10 06:53 venv
```

Donde se deberán encontrar el fichero de requistos del proyecto (requirements.txt), el directorio con el código fuente (src), el fichero de creación del contenedor (Dockerfile) y el directorio venv donde se almacenarar los diferentes directorios del entorno virtual. Una vez creados los diferentes elementos del entorno deberemos instalar los paquetes necesarios para la utilización de RabbitMQ mediante python utilizando el comando pip3. 

```
pip3 install pika
```

**IMPORTANTE: Recordar que una vez instalados los diferentes paquetes es necesario ejecutar el siguiente comando para incluir los paquetes en el fichero de requisitos (requirements.txt).**

```
pip3 freeze > requirements.txt
```

Una vez instalados los paquetes necesarios podemos comenzar a introducir nuestro datos mediante la creación de nuestro productor, para ello tendremos que conectarnos a RabbitMQ a través del puerto 5672, de la siguiente manera. 

```
#!/usr/bin/env python3

import pika

HOSTNAME = 'localhost'
PORT = 5672

if __name__ == "__main__":

    topic = 'fictizia'

    try:

        credentials = pika.PlainCredentials('user', 'password')
        parameters = pika.ConnectionParameters(HOSTNAME,
                                               PORT,
                                               '/',
                                               credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=topic)
        
        for i in range(100):
            message = 'mensaje ' + str(i)
            channel.basic_publish(exchange='', routing_key=topic, body=message)
            print(message + " enviado.")
        connection.close()
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    exit(0)

```

Mediante este fragmento de código hemos insertado 100 mensajes en nuestro topic __test__ los cuales se almacerán en la cola de mensajes hasta que sean eliminados. 

**Paso 4: Consumiendo mis primeros mensajes**

Una vez que hemos comenzado a producir mensajes, deberemos construir nuestro consumir con el objetivo de comenzar a consumir la información que contiene nuestra cola de mensajes. Para ello deberemos añadir una serie de archivos en nuestra carpeta consumer. 

```
total 16
drwxrwxr-x 4 momartin momartin 4096 dic 10 06:53 .
drwxrwxr-x 4 momartin momartin 4096 dic 10 06:49 ..
-rw-rw-r-- 1 momartin momartin    0 dic 10 06:53 Dockerfile
-rw-rw-r-- 1 momartin momartin    0 dic 10 06:53 requirements.txt
drwxrwxr-x 2 momartin momartin 4096 dic 10 06:53 src
drwxrwxr-x 5 momartin momartin 4096 dic 10 06:53 venv
```

Donde se deberán encontrar el fichero de requistos del proyecto (requirements.txt), el directorio con el código fuente (src), el fichero de creación del contenedor (Dockerfile) y el directorio venv donde se almacenarar los diferentes directorios del entorno virtual. Una vez creados los diferentes elementos del entorno deberemos instalar los paquetes necesarios para la utilización de rabbitMQ mediante python utilizando el comando pip3. 

```
pip3 install pika
```

**IMPORTANTE: Recondar que una vez instalados los diferentes paquetes es necesario ejecutar el siguiente comando para incluir los paquetes en el fichero de requisitos (requirements.txt).**

```
pip3 freeze > requirements.txt
```

Una vez instalados los paquetes necesarios podemos comenzar a recolectar nuestro datos mediante la creación de nuestro consumidor, para ello tendremos que conectarnos a kafka de la siguiente manera. 

```
#!/usr/bin/env python3

import pika
import json

HOSTNAME = 'localhost'
PORT = 5672

def procesar_mensaje(ch, method, properties, body):
    print("mensaje [%r] recibido" % body)


if __name__ == "__main__":

    topic = 'fictizia'

    try:

        credentials = pika.PlainCredentials('user', 'password')
        parameters = pika.ConnectionParameters(HOSTNAME,
                                               PORT,
                                               '/',
                                               credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel() 
        channel.queue_declare(queue=topic)
        channel.basic_consume(queue=topic, auto_ack=True, on_message_callback=procesar_mensaje)
        channel.start_consuming()

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    exit(0)

```

Mediante este fragmento de código podemos recibir los mensajes asignados a un conjunto de topics. Los consumidores se deben suscribir a un conjunto de topics que se expresan como un array. 

**Paso 5: Creando nuestro sistema de ingestión a un sistema de almacenamiento**

Una vez que hemos conseguido crear nuestro sistema de producción y consumición vamos a utilizarlo para insertar información en una de los sistemas de almacenamiento que hemos visto anteriormente durante el máster. Para ellos vamos a utilizar una base de datos no sólo relacional de tipo documental (MongoDB). 

**Paso 6: Dockerizando nuestro proceso de producción de datos**

Para ello vamos a incluir en nuestro fichero de despligue, una variación del proceso de ingesta que creamos anteriormente. La nueva versión leerá un fichero de datos produciendo un conjunto de mensajes en nuestro topic. Para ello añadiremos un nuevo servicio en nuestra infraestructura de contenedores que se denominará __producer__ y cargará los datos en un determinado topic. Para ello deberemos crear una nuevo servicio de la siguiente manera:

```
  producer:
    restart: on-failure
    build: ./producer
    container_name: producer
    depends_on:
      - rabbit
    networks:
      fictizia_kafka:
        ipv4_address: 172.20.1.5
```

Una vez que hemos actualizar nuestro fichero de despligue (docker-compose) tenemos que instalar en nuestro entornos algunos paquetes o libreras de python que son necesarias para el los diferentes funcionalidades que queremos implementar. Para ello tendremos que instalas los paquetes pandas y wget mediante el siguiente comando:

```
pip3 install wget pandas
```

A continuación es necesario actualizar nuestro fichero de requisitos, ya que sino lo hacemos no podremos ejecutar nuestro sistemas de ingestión mediante productores dentro del contenedor. Para ello es necesario ejecutar el siguiente comando:

```
pip3 freeze > requirements.txt
```

Una vez instalados los diferentes paquetes y actualizado nuestro fichero de requisitos, es necesario implementar una serie de variaciones en el código fuente de nuestro productor. En primer lugar es necesario descargar el (fichero)[https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data] con la información que insertaremos en la cola e incluir el siguiente código para procesarlo y cargar cada uno de los registros (lineas) en nuestra cola de mensajes:

```
import pika
import pandas as pd
import json

FILE = '../data/breast-cancer-wisconsin.data'
HOSTNAME = 'localhost'
PORT = 5672

if __name__ == "__main__":

    topic = 'fictizia'

    try:

        credentials = pika.PlainCredentials('user', 'password')
        parameters = pika.ConnectionParameters(HOSTNAME,
                                               PORT,
                                               '/',
                                               credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=topic)
        count = 1

        for document in data:
            message = document.encode('utf-8')
            channel.basic_publish(exchange='', routing_key=topic, body=message)
            print(message + " enviado.")
            count += 1
        
        print("Se han enviado " + str(count) + " mensajes")

    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    
    exit(0)

```

Para el correcto funcionamiento del código fuente hemos creada una carpeta data donde hemos descargado el fichero de datos que vamos a utilizar en este ejercicio. Aunque también es posible descargarlo directamente de la fuente en cada ejecución utilizando el siguiente código:

```
URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
FILE = '../data/breast-cancer-wisconsin.data'

if not path.exists(FILE):
    FILE = wget.download(URL)

```

Una vez realizados todos estos cambios es posible desplegar de nuevo nuestro productor utilizando nuestro fichero de despliegue mediante el siguiente comando:

```
$ docker-compose -f docker_compose.yml up --build -d 
```

**Paso 7: Descargando MongoDB**

A continuación es necesario desplegar nuestro sistema de almacenamiento. Para ellos vamos a utilizar el contenedor que utilizamos en el ejercicio 2 del capítulo 3. Comenzaremos por el despligue de MongoDB para ello vamos a descargar la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes del servidor [MongoDB](https://hub.docker.com/_/mongo) disponibles en dockerhub. 

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

En este ejercicio vamos a centrarnos en desplegar nuestro contendores mediante nuestro fichero de despligue (docker-compose). Para ello incluiremos nuestro contenedor mongo a los contenedores desplegados anteriomente mediante la siguiente configuración: 

```
  mongo:
    restart: always
    image: mongo:latest
    container_name: mongo_db  
    ports:
      - "27017:27017"
    volumes:
      - ./mongoData:/data/db
    networks:
      fictizia_kafka:
        ipv4_address: 172.20.1.6
```

Una vez añadir podemos lanzar nuestro fichero de despliegue mediante el siguiente comando:

```
$ docker-compose -f docker_compose.yml up --build -d 
```

**Paso 8: Desplegando nuestra API sobre Mongo**

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

**Paso 9: Configuración del servidor**

El primer paso consiste en desarrollar el código de nuestro servidor para ellos vamos a utilizar [Flask](https://flask.palletsprojects.com/en/1.1.x/) que es un paquete de python que nos permite desplegar servidor web de forma sencilla y rápido. 

__Documentación y recursos__

- [Projecto Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Documentación Flask](https://flask.palletsprojects.com/en/1.1.x/api/)
- [Projecto Swagger](https://swagger.io/)
- [Documentación Swagger](https://swagger.io/solutions/api-documentation/)
- [Construcción de APIs](https://swagger.io/solutions/api-development/)

Para ello deberemos instalar algunos paquetes () utilizando pip3 si estamos trabajando en un sistema operativo Linux

```
pip3 install Flask connexion connexion[swagger-ui]
```

En caso de esta desarrollando nuestras aplicaciones en un sistema operativo MAC tendremos que sustituir el paquete __connexion[swagger-ui]__ por el paquete __swagger-ui-bundle__ de la siguiente manera:

```
pip3 install Flask connexion swagger-ui-bundle
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

**Paso 9: Construyendo mi API REST**

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
        "title": "API REST Capitulo 5 - Kafka"
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
```

Una vez definidos los elementos básicos, tendremos que tener al menos la función de insercción de datos mediante __Post__. Esta función debe obtener los diferentes parámetros de nuestro análisis e insertarlo en mongo. La función deberías tener el siguiente código:

```
def add_analysis(id,
                   clump_thickness,
                   unif_cell_size,
                   unif_cell_shape,
                   marg_adhesion,
                   single_epith_cell_size,
                   bare_nuclei,
                   bland_chrom,
                   norm_nucleoli,
                   mitoses,
                   class_value):
    
    result = database.find_one({'id':id})

    if result is None:
        document = dict()

        document['id'] = id
        document['unif_cell_size'] = unif_cell_size
        document['unif_cell_shape'] = unif_cell_shape
        document['marg_adhesion'] = marg_adhesion
        document['single_epith_cell_size'] = single_epith_cell_size
        document['bare_nuclei'] = bare_nuclei
        document['bland_chrom'] = bland_chrom
        document['norm_nucleoli'] = norm_nucleoli
        document['mitoses'] = mitoses
        document['class'] = class_value

        result = database.insert_one(document)
        document = database.find_one({'_id':result.inserted_id})

        return json.loads(json_util.dumps(document)), 200
    else:
        return 'Existe un registro con el id ' + str(id) + '.', 404

```

Esta función devuelve un código 200, si se ha realizado una insercción correcta y 404 si ya existe un registro con el mismo id. Además es necesario incluir la configuración del método __Post__ en el fichero api.json mediante el siguiente fragmento de código:

```
"post": {
    "operationId": "functions.add_analysis",
    "tags": [
      "Analisis"
    ],
    "parameters": [
      {
        "name": "id",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "clump_thickness",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "unif_cell_size",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "unif_cell_shape",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "marg_adhesion",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "single_epith_cell_size",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "bare_nuclei",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "bland_chrom",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "norm_nucleoli",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "mitoses",
        "in": "query",
        "required": true,
        "type": "integer"
      },
      {
        "name": "class_value",
        "in": "query",
        "required": true,
        "type": "integer"
      }
    ],
    "responses": {
      "200": {
        "description": "Se ha procesado la petición correctamente",
        "schema": {
          "type": "object"
        }
      }
    }
  }
}

```
Una vez configurada nuestra API, podemos deplegar nuestro entorno de nuevo mediante el siguiente comando:

```
$ docker-compose -f docker_compose.yml up -d 
```

**Paso 10: Creando mi comsumidor **

Para la insercción de nuestro nuevo consumir vamos a incluir en nuestro fichero de despligue, una variación del proceso de consumición que creamos en los primeros paso de este ejercicio. La nueva versión consumirá los mensajes de un topic e insertará cada uno de ellos en una colección dentro de nuestro mongo DB. Para ello añadiremos un nuevo servicio en nuestra infraestructura de contenedores que se denominará __consumer__. Para ello deberemos crear una nuevo servicio de la siguiente manera:

```
  consumer:
    restart: always
    build: ./consumer
    container_name: consumer
    depends_on:
      - rabbit
    networks:
      fictizia_kafka:
        ipv4_address: 172.20.1.4
```

Una vez que hemos actualizar nuestro fichero de despligue (docker-compose) tenemos que instalar en nuestro entornos algunos paquetes o libreras de python que son necesarias para el los diferentes funcionalidades que queremos implementar. Para ello tendremos que instalas los paquetes pandas y wget mediante el siguiente comando:

```
pip3 install requests
```

A continuación es necesario actualizar nuestro fichero de requisitos, ya que sino lo hacemos no podremos ejecutar nuestro sistemas de ingestión mediante productores dentro del contenedor. Para ello es necesario ejecutar el siguiente comando:

```
pip3 freeze > requirements.txt
```

Una vez instalados los diferentes paquetes y actualizado nuestro fichero de requisitos, es necesario implementar una serie de variaciones en el código fuente de nuestro consumidor. Para ello incluiremos las siguiente lineas de código:

```
import pika
import json
import requests

HOSTNAME = 'localhost'
PORT = 5672
URL = 'http://172.20.1.7:5005/fictizia/1.0/analysis'

def procesar_mensaje(ch, method, properties, body):
    def generate_url(url, data):
        url = url + '?'
        for k,v in data.items():
            url = url + str(k) + '=' + str(v) + '&'
        return url

    url = generate_url(URL, message.value.decode('utf-8'))
    response = requests.post(url)
    if response.status_code == 400:
        print(url)
  

if __name__ == "__main__":

    topic = 'test'

    try:

        credentials = pika.PlainCredentials('user', 'password')
        parameters = pika.ConnectionParameters(HOSTNAME,
                                               PORT,
                                               '/',
                                               credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel() 
        channel.queue_declare(queue=topic)
        channel.basic_consume(queue=topic, auto_ack=True, on_message_callback=procesar_mensaje)
        channel.start_consuming()
  
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    exit(0)
    
```

Una vez realizados todos estos cambios es posible desplegar de nuevo nuestro productor utilizando nuestro fichero de despliegue mediante el siguiente comando:

```
$ docker-compose -f docker_compose.yml up --build -d 
```
