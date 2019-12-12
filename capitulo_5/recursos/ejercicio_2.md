![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 5 - Ejercicio 02: Trabajando con colas de mensajes ##

El objetivo de este ejercicio es crear una aplicación que procese la información de uno o más ficheros de datos mediante la utilización de una cola de mensajes. Esta información será almacenada a continuación en un sistema de almacenamiento externo.  
Docker nos permite desplegar de forma sencilla contenedores utilizando imágenes previamente creadas, para aprender como reutilizar estas imágenes vamos a desplegar un servicio Kafka. Existen diferentes formas de construir nuestro contenedor Kafka, (1) mediante la utilización de la imagen; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml). En este caso vamos a realizarlo mediante un fichero de despliegue, ya que para desplegar nuestra cola kafka tenemos que desplegar también un servidor de Zookeeper. 

**Paso 1: Descargando la imagen de kafka**

En primer lugar vamos a descargar la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes del servidor [Spotify](https://hub.docker.com/r/spotify/kafka/dockerfile). Además de la imagen ofrecida por la empresa Bitnami, existen diferentes versiones de cola de mensajes que pueden ser utilizadas, accediendo al listado de imagenes desarrolladas por diferentes compañias [Kafka](https://registry.hub.docker.com/search?q=Kafka&type=image).

```
$ docker pull spotify/kafka:latest
```

A continuación comprobaremos si la imagen se ha descargado correctamente y está disponible en nuestro repositorio local de imágenes, mediante el siguiente comando:

```
$ docker images 
```


Obteniendo la siguiente salida que nos indica que hemos descargado la imagen mongo en su versión (tag) 3.4.21-xenial hace 6 semanas. 

```
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
spotify/kafka              latest              a9e0a5b8b15e        3 years ago         443MB
```

**Paso 2: Creando nuestro fichero de despliegue**

Una vez que hemos descargado la imagen de nuestro servicio kafka, podemos crear los diferentes elementos en nuestro fichero de despliegue, por lo que es necesario crear un proyecto con la siguiente estructura

```
total 16
drwxrwxr-x 4 momartin momartin 4096 dic 10 06:31 .
drwxrwxr-x 3 momartin momartin 4096 dic 10 06:19 ..
drwxrwxr-x 2 momartin momartin 4096 dic 10 06:31 consumer
-rw-rw-r-- 1 momartin momartin    0 dic 10 06:31 docker-compose.yml
drwxrwxr-x 2 momartin momartin 4096 dic 10 06:31 producer
```

Donde se deberán encontrar el fichero de compose donde se definirián los diferentes contenedores necesarios para la utilización de colas de mensajes mediante Kafka y los ficheros los dos carpetas, mediante las que crearemos nuestro productor y nuestro consumidor. Una vez construido nuestro proyecto podemos pasar a definir nuestro fichero de despligue mediante docker-compose. Para ello deberemos incluir primero la configuración de una red mediante el siguiente código:

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
  kafka:
    restart: always
    container_name: kafka    
    image: 'spotify/kafka:latest'
    hostname: kafka
    ports:
      - '9092:9092'
      - '2181:2181'
    volumes:
      - ./kafka-logs:/tmp/kafka-logs
    environment: 
      - ADVERTISED_PORT=9092
      - ADVERTISED_HOST=localhost
    networks:
      fictizia_kafka:
        ipv4_address: 172.20.1.3
```

Una vez construido nuestro fichero de despliegue podremos lanzar nuestro servidor kafka, mediante el siguiente comando:

```
docker-compose -f docker-compose.yml up --build -d
```

Si todo ha funcionado correctamente deberemos observar los siguiente contenedores al ejecutar el comando docker ps:

```
CONTAINER ID        IMAGE                  COMMAND             CREATED             STATUS              PORTS                                            NAMES
4466a40ff5c9        spotify/kafka:latest   "supervisord -n"    3 seconds ago       Up 2 seconds        0.0.0.0:2181->2181/tcp, 0.0.0.0:9092->9092/tcp   kafka
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

Donde se deberán encontrar el fichero de requistos del proyecto (requirements.txt), el directorio con el código fuente (src), el fichero de creación del contenedor (Dockerfile) y el directorio venv donde se almacenarar los diferentes directorios del entorno virtual. Una vez creados los diferentes elementos del entorno deberemos instalar los paquetes necesarios para la utilización de kafka mediante python utilizando el comando pip3. 

```
pip3 install kafka-python
```

**IMPORTANTE: Recondar que una vez instalados los diferentes paquetes es necesario ejecutar el siguiente comando para incluir los paquetes en el fichero de requisitos (requirements.txt).**

```
pip3 freeze > requirements.txt
```

Una vez instalados los paquetes necesarios podemos comenzar a introducir nuestro datos mediante la creación de nuestro consumidor, para ello tendremos que conectarnos a kafka de la siguiente manera. 

```
#!/usr/bin/env python3

from kafka import KafkaProducer

HOSTNAME = 'localhost'
PORT = 9092

if __name__ == "__main__":

    topic = 'test'

    try:

        producer = KafkaProducer(bootstrap_servers=HOSTNAME+':'+str(PORT))
        for i in range(100):
            message = 'mensaje ' + str(i)
            producer.send(topic, message.encode('ascii'))
            print(message + " enviado.")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    exit(0)
```

Mediante este fragmento de código hemos insertado 100 mensajes en nuestro topic __test__ los cuales se almacerán en la cola de mensajes hasta que sean eliminados. 

**Paso 4: Consumiento mis primeros mensajes**

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

Donde se deberán encontrar el fichero de requistos del proyecto (requirements.txt), el directorio con el código fuente (src), el fichero de creación del contenedor (Dockerfile) y el directorio venv donde se almacenarar los diferentes directorios del entorno virtual. Una vez creados los diferentes elementos del entorno deberemos instalar los paquetes necesarios para la utilización de kafka mediante python utilizando el comando pip3. 

```
pip3 install kafka-python
```

**IMPORTANTE: Recondar que una vez instalados los diferentes paquetes es necesario ejecutar el siguiente comando para incluir los paquetes en el fichero de requisitos (requirements.txt).**

```
pip3 freeze > requirements.txt
```

Una vez instalados los paquetes necesarios podemos comenzar a introducir nuestro datos mediante la creación de nuestro consumidor, para ello tendremos que conectarnos a kafka de la siguiente manera. 

```
#!/usr/bin/env python3

from kafka import KafkaConsumer
import json

HOSTNAME = 'localhost'
PORT = 9092


if __name__ == "__main__":

    topic = 'test'

    try:

        consumer = KafkaConsumer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True)
        consumer.subscribe([topic])
        for message in consumer:
            message = message.value.decode("utf-8")
            print(message + " recibido")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    exit(0)
```

Mediante este fragmento de código podemos recibir los mensajes asignados a un conjunto de topics. Los consumidores se deben suscribir a un conjunto de topics que se expresan como un array. 

**Paso 5: Creando nuestro sistema de ingestión a un sistema de almacenamiento**
