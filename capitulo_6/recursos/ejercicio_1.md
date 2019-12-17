![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 6 - Ejercicio 01: Procesamiento de la información mediante Apache Airflow ##

El objetivo de este ejercicio consiste en desplegar un proceso de tratamiento de la información basado en Apache Airflow. Esta tecnología permite crear flujos de trabajo basados en tareas mediante la utiización de Directed Acyclic Graphs (DAGs). 

<img src="../img/fictizia_capitulo4_ejercicio_1.png" alt="Infraestructura" width="800"/>

### Recursos ###

Para el desarrollo de este ejercicio vamos a utilizar las diferentes tecnologías y recursos.

- [Python](https://www.python.org/) como lenguaje de programación para el desarrollo de nuestros procesos. 
- [Docker](https://docs.docker.com/) para construir el contenedor donde se desplegará nuestro servidor. 
- [Apache AirFlow](https://airflow.apache.org/) como sistema de orquestación de procesos.

Cómo en los anteriores ejercicios vamos a utilizar Docker como tecnología de creación de contenedores mediante la utilización de imágenes. Existen diferentes maneras de construir nuestra imagen basada en Apache Airflow: (1) mediante la utilización de  una imagen previamente desarrollada y almacenada en Docker Hub; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml). En este caso vamos a utilizar una imagen previamente construir que desplegaremos mediante un fichero de despliegue.

**Paso 1: Descargando la imagen de Apache Airflow**

En primer lugar vamos a descargar la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes disponibles en DockerHub para Apache [Airflow](https://hub.docker.com/r/apache/airflow). La imagenes disponibles han sido desarrolladas por el equipo de desarrolladores de Apache Airflow. 

```
$ docker pull apache/airflow:master-python3.7-ci
```

A continuación comprobaremos si la imagen se ha descargado correctamente y está disponible en nuestro repositorio local de imágenes, mediante el siguiente comando:

```
$ docker images 
```

Obteniendo la siguiente salida que nos indica que hemos descargado la imagen mongo en su versión (tag) 3.4.21-xenial hace 6 semanas. 

```
REPOSITORY                 TAG                 IMAGE ID            CREATED             SIZE
apache/airflow             master-python3.7-ci   d795259cd755        4 hours ago         3.24GB
```

Para el desarrollo de este tutorial vamos a utilizar una versión más ligera, que se encuentra almancenada en el siguiente repositorio de [Apache Airflow](https://hub.docker.com/r/puckel/docker-airflow/). Para ello tendremos que descargarla de forma similar a la anterior:

```
$ docker pull puckel/docker-airflow
```

**Paso 2: Desplegando Apache Airflow**

Una vez que hemos descargado la imagen podemos deplegarla mediante la utilización de docjer run con el objetivo de comprobar su correcto funcionamiento. 

```
$ docker run --name=airflow -d -p 8080:8080 puckel/docker-airflow webserver
```

**Paso 3: Creando nuestro fichero de despliegue**

Una vez que hemos descargado la imagen de nuestro servicio Apache Airflow, podemos crear los diferentes elementos en nuestro fichero de despliegue, por lo que es necesario crear un proyecto con la siguiente estructura

```
total 8
drwxrwxr-x 4 momartin momartin 4096 dic 10 06:31 .
drwxrwxr-x 3 momartin momartin 4096 dic 10 06:19 ..
-rw-rw-r-- 1 momartin momartin    0 dic 10 06:31 docker-compose.yml
```

Donde se deberán encontrar el fichero de compose donde se definirián los diferentes contenedores necesarios para la utilización de Apache airflow. Una vez construido nuestro proyecto podemos pasar a definir nuestro fichero de despligue mediante docker-compose. Para ello deberemos incluir primero la configuración de una red mediante el siguiente código:

```
version: '3.4'

networks:
  fictizia_airflow:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.30.1.0/24
```

A continuación vamos la configuración de nuestro contenedor Apache airflow. Para ello incluiremos un servicio 

```
services:
  airflow:
    restart: always
    container_name: airflow    
    image: 'puckel/docker-airflow'
    ports:
      - '8080:8080'
    volumes:
      - './dags:/usr/local/airflow/dag'
    networks:
      fictizia_airflow:
        ipv4_address: 172.30.1.3
```

Una vez construido nuestro fichero de despliegue podremos lanzar nuestro servidor kafka, mediante el siguiente comando:

```
docker-compose -f docker-compose.yml up --build -d
```

Si todo ha funcionado correctamente deberemos observar los siguiente contenedores al ejecutar el comando docker ps:

```
CONTAINER ID        IMAGE                   COMMAND                  CREATED              STATUS              PORTS                                        NAMES
7abce41677f9        puckel/docker-airflow   "/entrypoint.sh webs…"   About a minute ago   Up 9 seconds        5555/tcp, 8793/tcp, 0.0.0.0:8080->8080/tcp   airflow

```

**Paso 4: Creando nuestros ficheros DAGS**

Una vez que hemos desplegado nuestra arquitectura, podemos comenzar con la creación de nuestros workflows. Para ellos es necesario describir tres conceptos básicos de Airflow:

- Operador (Operators): Los operadores representan un proceso que realiza un conjunto de acciones, es decir se corresponde con un fragmento de código que se considera atómico. Específicamente, un operador representa una única tarea dentro del flujo de trabajo. Airflow proporciona muchas clases predefinidas que se pueden ejecutar como tareas. Esto incluye clases para tareas muy comunes, como BashOperator, PythonOperator, EmailOperator, OracleOperator, etc. Además de la multitud de clases de operadores disponibles, Airflow permite definir nuestras propios operadores. Como resultado, una tarea en su DAG puede hacer casi cualquier cosa que desee, y puede programarse y monitorizarse utilizando el core de Airflow.

- Tareas (Tasks): Una tarea es una instancia en ejecución de un operador. Durante la creación de instancias, puede definir parámetros específicos asociados con el operador y la tarea parametrizada se convierte en un nodo del workflow.

- DAGs (Directed Acyclic Graph (DAG)): Un DAG es una estructura de definición de tareas que está formada por las diferentes tareas que quieres ser ejecutadas, así como las relaciones y dependencias que existen entre las tareas. Los DAG se pueden representar visualmente mediante un gráfico con nodos y arcos, donde los nodos representan las tareas y los arcos representan dependencias entre las tareas (es decir, el orden en que deben ejecutarse las tareas). Esencialmente, los DAG representan el flujo de ejecución que desea orquestar y monitorizar emdiante Apache Airflow. Estos grafos deben Ser "acíclicos", es decir,  el gráfo __no tiene ciclos__; Esto significa que el flujo de trabajo deben tener un comienzo y un final (si hubiera un ciclo, el flujo de trabajo se atascaría en un bucle infinito y nunca finalizara).

```
from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello world!'

dag = DAG('hello_world', description='Simple tutorial DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

dummy_operator >> hello_operator
```

