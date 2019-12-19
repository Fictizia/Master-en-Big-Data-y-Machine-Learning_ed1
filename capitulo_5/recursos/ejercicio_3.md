![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 5 - Ejercicio 03: Trabajando con Scraper ##

En este ejercicio vamos a construir un scraper con el fin de construir un sistema de recolección activo, que sea capaz 
de recoger información de diferentes páginas web. Para ello vamos a utilizar el sistema de generación de scrapers para python denominado scrapy.  

**Paso 1: Creación del proyecto**

El primer paso consistirá en la creación de los diferentes elementos en nuestro proyecto con el fin de almacenar nuestros diferentes scrapers. 

```
total 16
drwxrwxr-x 5 momartin momartin 4096 dic 19 15:39 .
drwxrwxr-x 5 momartin momartin 4096 dic 19 15:26 ..
-rw-rw-r-- 1 momartin momartin    0 dic 19 15:39 docker-compose.yml
drwxrwxr-x 2 momartin momartin 4096 dic 19 15:39 kafka-logs
drwxrwxr-x 4 momartin momartin 4096 dic 19 15:27 scrapers
```

En este caso crearemos dos carpetas: (1) scrapers donde se almacenarán nuestro scrapers; 7 (2) Kafka donde se almacenará la információn de nuestro contenedor kafka (dentro de esta carpeta se guarda la información referente a los datos almacenados en kafka. 


**Paso 2: Creación del entorno**

Una vez que hemos definido la estructura del nuestro entorno de trabajo, vamos a instalar el entorno de ejecución y todas las librerias necesario. En primer lugar tenemos que crear el entorno virtual para python dentro de la carpeta scrapers, que almacenaremos en la carpeta venv, con el fin de que pueda ser detectado por los diferentes ides de programación. Para su generación utilizaremos el siguiente comando. 

```
$ virtualenv venv
```

Una vez generado nuestro entorno lo activaremos mediante el siguiente comando:

```
$ source ./venv/bin/activate
```

Ahora podemos instalar los diferente paquetes que utilizaremos a lo largo de este ejercicio mediante el siguiente comando:

```
$ pip3 install Scrapy kafka-python
```

**Paso 3: Despliegue de scrapy**

Una vez tras desplegar nuestro entorno e instalar todas las librerias podemos comenzar con el despligue de nuestro sistemas de scrapeo. Para ello, deberemos ejecutar el siguiente comando para que se genere la infraestructura necesaria para la creación de scraper en nuestro directorio src

```
$ scrapy startproject scrapers
```

Tras la ejecución del comando se ha generado nuestro proyecto en la carpeta __scrapers__ por lo que podremos comenzar a generar nuestras arañas de scrapeo. Para ello, deberemos acceder al directorio del proyecto, que en este caso es __scrapers__ y ejecutar el siguiente comando: 

```
scrapy genspider fictizia fictizia.com
```

Una vez ejecutados ambos comandos habremos creado una estructura de directorios como la siguiente:

```
├── scrapy.cfg                # Fichero de configuración
└── scrapers                  # Carpeta del proyecto
    ├── __init__.py
    ├── items.py              # Fichero de definición de items
    ├── middlewares.py        # Fichero de definición de middlewares
    ├── pipelines.py          # Fichero de definición de pipelines
    ├── settings.py           # Fichero de configuración del proyecto
    └── spiders               # Carpeta que almacena las diferentes arañas
        ├── __init__.py
        └── fictizia.py        # Fichero de la araña
```

El sistema de generación de arañas puede ser configurado de diferente maneras, para obtener más información utilizar el comando -h que mostrará las diferentes opciones disponibles:

```
scrapy genspider [options] <name> <domain>

Generate new spider using pre-defined templates

Options
=======
--help, -h              show this help message and exit
--list, -l              List available templates
--edit, -e              Edit spider after creating it
--dump=TEMPLATE, -d TEMPLATE
                        Dump template to standard output
--template=TEMPLATE, -t TEMPLATE
                        Uses a custom template.
--force                 If the spider already exists, overwrite it with the
                        template

Global Options
--------------
--logfile=FILE          log file. if omitted stderr will be used
--loglevel=LEVEL, -L LEVEL
                        log level (default: DEBUG)
--nolog                 disable logging completely
--profile=FILE          write python cProfile stats to FILE
--pidfile=FILE          write process ID to FILE
--set=NAME=VALUE, -s NAME=VALUE
                        set/override setting (may be repeated)
--pdb                   enable pdb on failure
```

**Paso 4: Creando nuestra primera araña**

Tras la generación del proyecto y de la araña, podemos comenzar a incluir código para la obtención de información mediante nuestra araña. Para ello deberemos editar nuestro fichero python y al abrirnos nos encontraremos algo como esto:

```
import scrapy


class FictiziaSpider(scrapy.Spider):
    name = 'fictizia'
    allowed_domains = ['fictizia.com']
    start_urls = ['http://fictizia.com/']

    def parse(self, response):
        pass
```

Como se puede observar nuestro fichero está formado por cuatro elementos principales:

- name: Es el nombre de la araña. Este valor debe ser único dentro de cada proyecto.
- start_urls: Es la lista de URL a las que se debe acceder. La araña comenzará crawleando estas url.
- allowed_domains: Es la lista de dominios aceptados. Aquellas URL cuyo dominio no se corresponden con los dominios almacenados en esta lista sern ignoradas.
- parse: Es el método que se ejecutará para cada una de nuestro llamadas a una URL. Es decir, es el método que analizará el respuesta de cada petición que realicemos. 

