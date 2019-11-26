![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 3 - Ejercicio 02: Manipulación de bases de datos en grafo ##

El objetivo de este ejercicio es crear un contenedor que contenga una base de datos no sólo relacion con el fin de explotar el funcionamiento de este tipo de bases de datos. En este ejercicio vamos a explorar el funcionamiento de las bases de datos en grafo. 


### Desplegando nuestro contenedor MongoDb

Docker nos permite desplegar de forma sencilla contenedores utilizando imágenes previamente creadas, para aprender como reutilizar estas imágenes vamos a desplegar un servidor de bases de datos Neo4j. Existen diferentes formas de construir nuestro contenedor Neo4J, (1) mediante la utilización de la imagen; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml)

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
