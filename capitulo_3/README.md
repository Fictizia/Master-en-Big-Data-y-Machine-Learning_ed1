![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

# Capitulo 5: Ingestión de datos

En general el proceso de recolección de información es considerada como una fases más importantes y complejas del ciclo de vida de los datos. Además muchas de las aplicaciones que se desarrollan actualmente tiene una acuciante necesidad de información para funcionar de manera correcta lo cual incrementa aún más la importancia del proceso de recolección. Existe múltiples formas de recolectar información para nuestras aplicaciones, pero en este tema sólo vamos a hablar de aquellas más comunes. 

**Métodos tradicionales**

Los métodos activos de recolección de información son aquellos que son utilizados de manera general y se corresponde con la utilización de archivos de logs, formulario o funcionalidades básicas para la recogida de la información. Este es la forma más común y suele funcionar perfectamente en aplicaciones que no tienen una necesidad de datos para funcionar correctamente, pero que una vez que los han recogido pueden ser utilizados para mejorar la experiencia de los usuarios u ofrecerles nuevas funcionalidades. 

**Métodos activos - Web scraping**

El web scraping es un técnica de obtención de la información mediante la extracción del contenido de páginas web. Este tipo de técnica consiste en simular el proceso de navegación de un humano en una página web mediante un sistema automático, denominado robot, que descarga todo el contenido de cada una de la páginas web y a continuación utiliza los diferentes enlaces dentro del contenido para cargar nuevas páginas. Se puede considerar como un proceso recursivo dentro de cada dominio donde se comienzo por la página principal (home) y se va navegando a través de los diferentes enlaces internos (links) de la página web de forma similar a como funcionaría un algoritmo de búsqueda donde el nodo raíz sería la página principal y los diferentes nodos sucesores serían los links de cada página. El proceso de web scraping está íntimamente relacionado por los sistema de indexación de contenidos utilizado por lo motores de búsqueda[] que realizan un proceso de crawling mediante la utilización de robots, denominados arañas, que recopilan información referentes a los enlaces presenten en las páginas webs.

- [Ingestión de datos mediante mediante scrapers](./clase_1.md)

**Métodos pasivos - Colas de mensajes**

El crecimiento exponencial del uso de ciertas aplicaciones hicieron aparecer problemas en su rendimiento a la hora de procesar y almacenar la información introducida por los usuarios, ya que los servicios de inserción en las bases de datos no eran capaces de soportar el número de peticiones por segundos producidas por los usuarios. Con el fin de solventar este problema se desarrollaron las colas de mensajes, que son un sistema de comunicación de información asíncrona entre servicios (productor y consumidor) que se usa en arquitecturas de microservicios en las que no existe un servidor principal con el fin de evitar los posible cuellos de botellas. Este tipo de sistemas de comunicación utilizan dos tipos de microservicios: un productor que inserta mensajes en la cola y un consumir que extrae y/o eliminar mensaje de cola. De forma que los mensajes son almacenados en la cola de manera temporal hasta que son consumidos y/o eliminados.

- [Ingestión de datos mediante colas de mensajes](./clase_2.md)
