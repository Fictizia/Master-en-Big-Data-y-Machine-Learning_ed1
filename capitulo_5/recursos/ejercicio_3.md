![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 5 - Ejercicio 03: Trabajando con Scrapers ##

En este ejercicio vamos a construir un scrapers con el fin de construir un sistema de recolección activo, que sea capaz 
de recoger información de diferentes páginas web. Para ello vamos a utilizar el sistema de generación de scrapers para python denominado scrapy.  

**Paso 1: Creación del proyecto**

El primer paso consistirá en la creación de los diferentes elementos en nuestro proyecto con el fin de almacenar nuestros diferentes scrapers. 

```
total 20
drwxrwxr-x 5 momartin momartin 4096 dic 19 15:39 .
drwxrwxr-x 5 momartin momartin 4096 dic 19 15:26 ..
-rw-rw-r-- 1 momartin momartin    0 dic 19 15:39 docker-compose.yml
drwxrwxr-x 2 momartin momartin 4096 dic 19 15:39 kafka-logs
drwxrwxr-x 4 momartin momartin 4096 dic 19 15:27 scrapers
drwxrwxr-x 2 momartin momartin 4096 dic 19 15:40 tools
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

**Paso 5: Resolviendo los problemas de dinamismo**

Uno de los principales problemas de los proceso de scraping o crawling es que muchas páginas no sirven datos estáticos, por lo que es necesario utilizar sistemas que nos permitan acceder a los datos dinámicos que se generan cuando se realizan las consultas a la página. Para resolver este problema vamos a combinar scrapy con selenium. Para ello es necesario instalar el paquete de selenium de la siguiente manera. 

```
$ pip3 install selenium
```

Una vez que hayamos descargado selenium deberemos instalar unos de los diferentes web drivers que simulan un navegador desde nuestro sistema de scrapers. Para este ejercicio vamos a utilizar __ChromeDriver__. ChromeDriver es una servidor que implementa el protocolo __wire__ (punto a punto) para Chromium con objetivo de testear de manera automática las aplicaciones web utilizando múltiples plataformas (navegadores). Para poder descargarlo tendremos que utilizar el siguiente comando:

```
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
```

Una vez que hayamos descargado el chromedriver debemos instalarlo. Es posible desplagarlo en una carpeta local, como por ejemplo la carpeta __tools__ que hemos creado para la realización de este ejercicio. 

```
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

**Paso 6: Reconfigurando nuestra araña**

Una vez que hayamos instalado nuestro web driver podremos modificar nuestro método parse de la siguiente manera. Primero añadiremos la configuración del agente (cabeceras) que vamos a utilizar para acceder a las páginas web:

```
self.header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
```

A continuación configuraremos nuestro web driver añadiendo una serie de opciones:

```
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-extensions")
options.add_argument(" --disable-gpu")
options.add_argument(" --disable-infobars")
options.add_argument(" -–disable-web-security")
options.add_argument("--no-sandbox")
```

Una vez definido el tipo de agente y las opciones, vamos a crear nuestro agente para acceder a página dinámicas

```
capabilities = options.to_capabilities()
self.driver = webdriver.Chrome('/usr/bin/chromedriver', desired_capabilities=capabilities)
self.driver.get('https://www.fictizia.es/')
```

**Paso 7: Obteniendo datos de las web**

Una vez que hemos configurado correctamente nuestro agente, vamos a recoger datos de la web, para ello vamos a utilizar una web donde exista información con paginación. Para ello vamos a utilizar la funcionalidad de __xpath__ que nos ofrece selenium. En la página web de [selenium](https://selenium-python.readthedocs.io/locating-elements.html) podemos encontrar los métodos que podemos utilizar para acceder a la información. Xpath, nos permite acceder a los elementos de DOM, de manera indivial o de forma agrupada:

- find_element_by_id
- find_element_by_name
- find_element_by_xpath
- find_element_by_link_text
- find_element_by_partial_link_text
- find_element_by_tag_name
- find_element_by_class_name
- find_element_by_css_selector
- find_elements_by_name
- find_elements_by_xpath
- find_elements_by_link_text
- find_elements_by_partial_link_text
- find_elements_by_tag_name
- find_elements_by_class_name
- find_elements_by_css_selector

Para ellos vamos a seleccionar elementos mediante el nombre de la clase que utilizan en el código html. Por ejemplo, si por ejemplo quisieramos seleccionar todos los elementos cuya clase es __vacio__ deberíamos utilizar el siguiente código:

```
self.driver.find_elements_by_class_name('vacio')
```
Este método nos devolvera una lista de objetos sobre los que podremos volver a aplicar de nuevo uno de los métodos descritos anteriormente. 
