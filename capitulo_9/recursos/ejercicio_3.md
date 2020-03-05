![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 9 - Ejercicio 3: Visualización de datos en la web ##

El objetivo de este ejercicio consiste en desarrollar de un sistema de visualización mediante un aplicación web, para ellos vamos a utilizar uno de los sistemas de visualización existentes para python el cual nos permitirá de forma sencilla visualizar información. 

### Construyendo nuestro servidor de visualización

Mediante este ejercicio vamos a aprender a construir aplicaciones web para visualización utilizando el sistema __bokeh__. (Bokeh)[] es una herramienta  inspirado en los conceptos descritos en __The Grammar of Graphics__. Este sistema permite desplegar componentes superpuestos con el objetivo de crear una gráfica. Por ejemplo, se puede comenzar con los ejes, e ir agregando puntos, líneas, etiquetas, ventanas con información etc.

Una de las grandes ventajas de este sistema es que los gráficos se pueden generar como objetos JSON, documentos HTML o aplicaciones web interactivas. Bokeh hace un buen trabajo a los usuarios manipulen datos en el navegador, con controles deslizantes y menús desplegables para el filtrado.

Existen otras tecnologías similares a Bokeh:

- [mpld3](http://mpld3.github.io/)
- [pygal](http://www.pygal.org/en/latest/index.html)
- [Bokeh](http://bokeh.pydata.org/en/latest/)
- [HoloViews](http://holoviews.org/)
- [Plotly](https://plot.ly/python/)

**Paso 1: Descargo nuestro conjunto de datos**

El primer paso consiste en descargar el conjunto de datos que vamos a utilizar. Para este último ejercicio vamos a crear un sistema de visualización mediante la utilización de los datos disponibles acerca de la epidemia de coronavirus. Para ellos utilizaremos los datos disponibles en Kaggler sobre el [Coronavirus](https://www.kaggle.com/kimjihoo/coronavirusdataset).

Aunque realmente vamos a utilizar un conjunto de datos de los vuelos de 2018 que han despegado del aeropuerto JFk de New York:

- [Información acerca de los vuelos](https://storage.googleapis.com/fictizia/flights_data/flights.csv)
- [Información acerca de los vuelos en el mapa](https://storage.googleapis.com/fictizia/flights_data/flights_map.csv)

**Paso 2: Almacenamiento de datos en Google Cloud Storage**

Una vez que hemos descargado nuestros datos os tendremos que subir en nuestro Google Cloud Storage. 
