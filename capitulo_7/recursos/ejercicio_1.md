![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 7 - Ejercicio 01: Creando nuestra regresión lineal ##

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
$ docker-compose -f docker_compose.yml up --build -


