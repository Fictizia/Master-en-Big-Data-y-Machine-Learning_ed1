![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 6 - Ejercicio 04: Tratamiento y manipulación de la información en Cloud DataFlow ##

El objetivo de este ejercicio consiste en realizar diferentes procesos de tratamiento y manipulación de la información sobre diferentes conectores de entrada y salida. 

<img src="../img/fictizia_capitulo4_ejercicio_1.png" alt="Infraestructura" width="800"/>

### Recursos ###

Para el desarrollo de este ejercicio vamos a utilizar las diferentes tecnologías y recursos.

- [Introducción a Cloud DataFlow](https://airflow.apache.org/docs/stable/)
- [Guía de uso rápido de Cloud DataFlow para Python](
https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python?hl=es-419)
- [Guía de uso rápido de Cloud DataFlow para Java](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-java-maven?hl=es-419)
- [QuickLabs Cloud DataFlow](https://www.qwiklabs.com/focuses/1100?locale=es&parent=catalog)
- [Instalación de Cloud DataFlow mediante Pypi - Python](https://pypi.org/project/google-cloud-dataflow/)
- [Página oficial del proyecto Apache Beam](https://beam.apache.org/)
- [Documentación oficial del proyecto Apache Beam](https://beam.apache.org/documentation/)
- [Guía de inicio sobre Apache Beam](https://beam.apache.org/get-started/beam-overview/)

Cómo en los anteriores ejercicios vamos a utilizar Docker como tecnología de creación de contenedores mediante la utilización de imágenes. Existen diferentes maneras de construir nuestra imagen basada en Apache Airflow: (1) mediante la utilización de  una imagen previamente desarrollada y almacenada en Docker Hub; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml). En este caso vamos a utilizar una imagen previamente construir que desplegaremos mediante un fichero de despliegue.

**Paso 1: Activación de DataFlow**

Para comenzar con la realización de este tutorial necesitamos utilizar Cloud Dataflow, para ello tendremos que acceder a la consola de GCP y activar el servicio de Cloud Dataflow. Para ellos podremos buscar a través de nuestro buscador __Dataflow__ y activar el servicio como se puede observar en la siguiente imagen:

<img src="../img/dataflow_1.png" alt="Activación de dataflow" width="800"/>

**Paso 2: Generación de credenciales básicos**

Para poder acceder a los recursos de Google Cloud DataFlow (GCD) es necesario generar unos credenciales de acceso que serán utilizados por el driver de acceso para python que utilizaremos en el ejercicio. Para ello, deberemos acceder en nuestra consola de Google Cloud Platform y acceder a la sección de APIs & Servicios y proceder a crear unas credenciales de tipo Services account Key. Una vez hayamos accedido deberemos crear una nueva cuenta de servicio como se muestra en la siguiente imagen:

<img src="../img/dataflow_2.png" alt="Credenciales 1" width="800"/>

Para ello, seleccionaremos como rol para la cuenta de servicio el rol de __Administrador de DataFlow__ con el fin de tener permisos para acceder a todos los recursos disponibles. Cuando se crea una cuenta de credenciales es obligatorio asignar los persimos específicos para los procesos, pero al ser un ejercicio en un entorno controlado vamos a concederle todos los permisos que tenemos disponibles mediante la utilización del rol de __administrador__. Una vez definidos los roles de nuestra cuenta de servicio tenemos que decidir el formato de nuestros credenciales, que en este caso seránn de tipo JSON, como se observa en la siguiente imagen.
En primer lugar vamos a descargar la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes disponibles en DockerHub para Apache [Airflow](https://hub.docker.com/r/apache/airflow). La imagenes disponibles han sido desarrolladas por el equipo de desarrolladores de Apache Airflow. 

<img src="../img/dataflow_3.png" alt="Credenciales 2" width="800"/>

**Paso 3: Preparando el proyecto de Dataflow**

Para poder trabajar con Google DataFlow podemos utilizar diferentes lenguajes de programación. En este caso vamos a utilizar el conector de python que se puede descargar en el siguiente [enlace](https://pypi.org/project/google-cloud-dataflow). Para ellos vamos a crear un nuevo proyecto que contendrá los siguiente elementos:

```
total 20
drwxrwxr-x 5 momartin momartin 4096 ene 28 11:15 .
drwxrwxr-x 6 momartin momartin 4096 ene 28 11:06 ..
drwxrwxr-x 2 momartin momartin 4096 ene 28 11:15 credentials
-rw-r--r-- 1 momartin momartin    0 ene 28 11:06 Dockerfile
drwxrwxr-x 2 momartin momartin 4096 ene 28 11:06 src
drwxrwxr-x 5 momartin momartin 4096 ene 28 11:08 venv
```

Este proyecto se va a preparar para poder ser dockerizado pero inicialmente vamos a trabajar sobre el host. Para ello vamos a necesitas un carpeta para almacenar los diferentes credenciales, un archivo Dockerfile por si es necesario desplegar los componentes en un contenedor, una carpeta para el almacenamiento de los diferentes archivos que utilizaremos para desplegar procesos y una carpeta para el entorno virtual. Una vez definidos los diferentes componentes de proyecto, podemos comenzar a instalar la librería para python mediante el siguiente comando:

```
pip3 install apache-beam[gcp]
```

Una vez que hemos realizado la instalación de Apache Bean sobre el entorno gcp vamos a comprobar si ha funcionado correctamente. Para ello ejecutaremos el siguiente comando:

```
python3 -m apache_beam.examples.wordcount --output outputs
```

Si ha funcionado correctamente deberemos obtener como resultados los siguientes valores:

```
INFO:root:number of empty lines: 1663
INFO:root:average word length: 4
```

A continuación vamos a utilizar el código del contador de palabras disponibles en el repositorio de [https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/wordcount.py](Apache Bean). Crearemos un fichero, en el directorio src, denominado __ejercicio_1.py__ el cual contendrá el código fuente del contador de palabras. A continuación ejecutaremos el código mediante el siguiente comando para obtener el mismo resultado.  

```
python3 ejercicio_1.py --output outputs
```

Tras analizar el archivo observamos que además de la opción --output, también posee una opción denominada --input que nos permite indicar el fichero de entrada que utilizaremos para contar palabras. En esta caso vamos a utilizar un fichero público de nuestro propio Google Cloud storage. Para permitir que uno de nuestro fichero sea público es necesario modificar los permisos del archivo incluyendo una nueva entidad con el nombre __allUser__ y con el rol de __lector (Reader)__ como se observa en la siguiente imagen.

<img src="../img/dataflow_4.png" alt="Credenciales 2" width="800"/>

Una vez que hemos permitido el accedo a nuestro fichero de forma pública podremos utilizarlo como entrada para nuestro ejercio. Para ello utilizaremos el siguiente comando:

```
python3 ejercicio_1.py --input gs://fictizia/movies_metadata.csv --output outputs_fictizia
```

En este caso el resultado que obtendremos al ejecutar nuestro proceso de conteo de palabras detectará que la media de palabras por lineas es de 5 y que no existe ninguna linea en blanco. 

```
INFO:root:average word length: 5
```

**Paso 4: Conectando con nuestro Google Cloud Storage**

A continuación vamos a modificar el ejercicio anterior para que pueda conectarse a los ficheros privados almacenados en nuestros buckets. Para ello deberemos utilizar los credenciales que generamos anteriormente y almacenamos en la carpeta de credenciales en formato json y definir la variable __GOOGLE_APPLICATION_CREDENTIALS__. Esta variable de entorno nos permite definir de forma genérica los credenciales que utilizarán nuestras aplicaciones de google cloud. Para ello utilizaremos el siguiente comando:

```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```

Si la variable ha sido definida de manera correcta, tendremos que obtener el valor introducido anteriomente mediante el comando echo, de la siguiente manera:

```
echo $GOOGLE_APPLICATION_CREDENTIALS
```

Una vez definidos nuestros credenciales tendremos que ejecutar de nuevo nuestro ejercicio 2 utilizando uno de los ficheros privados que tenemos almacenados en nuestro storage, con el fin de ver si los credenciales han sido cargados de forma correcta:

```
python3 ejercicio_2.py --input gs://fictizia/breast-cancer-wisconsin.data --output outputs_fictizia
```

Para comprobar esto debemos analizar la traza de información generada por la ejecución de Apache Bean y observar que ya no aparece la siguiente alerta:

```
WARNING:root:Unable to find default credentials to use: The Application Default Credentials are not available. They are available if running in Google Compute Engine. Otherwise, the environment variable GOOGLE_APPLICATION_CREDENTIALS must be defined pointing to a file defining the credentials. See https://developers.google.com/accounts/docs/application-default-credentials for more information.
```

Para comprobar si nuestro script de conteo de palabras funciona correctamente vamos a utilizar otro fichero. Para ello vamos a descargar una versión en texto plano de __Don Quijote de la Mancha__ de Miguel de Cervantes en la siguiente [https://gist.github.com/jsdario/6d6c69398cb0c73111e49f1218960f79](link) y lo vamos a almacenar en nuestro Storage de forma privada. A continuación ejecutaremos de nuevo nuestro código de la siguiente manera:

```
python3 ejercicio_2.py --input gs://fictizia/el_quijote.txt --output outputs_fictizia
```

Obteniéndose el siguiente resultado:

```
INFO:root:number of empty lines: 1
INFO:root:average word length: 3
```

**Paso 5: Modificando nuestro Pipeline**

Una vez que hemos definido nuestro credenciales y hemos comenzado ha utilizar los elementos de nuestro cloud podemos utilizar nuestras credenciales para almacenar nuestra información de salida en storage. Para ellos modificaremos el fichero de salida de la siguiente manera:

```
python3 ejercicio_2.py --input gs://fictizia/el_quijote.txt --output gs://fictizia/salida
```

Esto almacenerá la salida en nuestro google cloud storage. Pero es posible modificar más elementos de nuestro sistema o pipeline para ello deberemos modificar las opciones de nuestro __pipeline__ 

```
pipeline_options = PipelineOptions()

gcloud_options = pipeline_options.view_as(beam.options.pipeline_options.GoogleCloudOptions)
gcloud_options.job_name = 'ejercicio-3-fictizia'
gcloud_options.project = 'fictizia-259518' 
gcloud_options.staging_location = 'gs://fictizia/staging'
gcloud_options.temp_location = 'gs://fictizia/temp2'
gcloud_options.region = 'europe-west1'

pipeline_options.view_as(beam.options.pipeline_options.StandardOptions).runner = 'DataflowRunner'

p = beam.Pipeline(options=pipeline_options)
```

**Paso 6: Connectando con Google Big Query**

