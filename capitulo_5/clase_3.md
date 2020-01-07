![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

# Capitulo 5: Clase 3 - Web Scraping

### ¿Cómo extraemos información de Internet?

Internet está lleno de información. Esta información puede ser utilizada para simplicar el proceso de búsqueda de información como han demostrado los buscadores web que almacenan la información de las páginas web con el fin de facilitar el proceso de búsqueda o el acceso a la información sin conexión

**Recursos**

### ¿Qué es un web robot?

Los robot web (tambien denominados Web Wanderers) son programas que navegan por la web automáticamente la web. Este tipo de programas son comunmente utilizados por los navegadores web como Google o Bing para la indexación de contenido o por los sistema de spam para la detección de direcciones de correo electrónico. El modo de funcinamiento de los robots web puede ser configurado mediante la utilización del fichero robots.txt que puede ser incluido en cualquier aplicación web.    


Los propietarios de sitios web pueden crear un archivo denominado __robots.txt__ que permite dar instrucciones a los robots web acerca de las acciones que pueden realizar sobre la web. La utilización de este tipo de archivo se denomina protocolo de exclusión de robots, ya que permiten minimizar las acciones que pueden realizar este tipo de programas. Por ejemplom si un robot quisiera acceder a la página web __https://fictizia-example.com__ debería acceder primer a la url __https://fictizia-example.com/robots.txt__ donde encontraría la siguiente información: 

Funciona así: un robot quiere visitar la URL de un sitio web, por ejemplo, http://www.example.com/welcome.html. Antes de hacerlo, primero comprueba http://www.example.com/robots.txt y encuentra la siguiente información:

```
User-agent: *
Disallow: /
```

En este caso el fichero de robots contiene dos directivas: (1) la primera se corresponde con el "User-agent" que indica que lo que aparece a continuación se aplica a cualquier robot que intente acceder a la página web; y la segunda __Disallow: /__ indica al robot que puede acceder a ninguna página web del sitio. 

**Recursos**

- [Introduction to robots.txt - Google](https://support.google.com/webmasters/answer/6062608?hl=en)
- [Cómo Crear el Archivo Robots.txt Perfecto Para SEO - Neil Patel](https://neilpatel.com/es/blog/robots-txt-seo/)
- [The web robot page - Everything about robots.txt](https://www.robotstxt.org/)
- [How to Address Security Risks with Robots.txt Files](https://www.searchenginejournal.com/robots-txt-security-risks/289719/)

### ¿Qué es un web Crawler?

Un Web Crawler (también denominado Web Spider) es un programa diseñado para el análisis de páginas web de forma automática. El modo de funcionamiento estandar de este tipo de programas, consiste en definir un conjunto de direcciones web iniciales que son almacenadas en una estructura de datos (posiblemente una cola), de manera que el web crawler descarga el contenido de cada una de las direcciones, analizando el contenido en busca de enlaces a páginas nuevas. Los diferentes enlaces descubiertos son insertados en la "cola de enlaces" de manera que estos nuevos enlaces sean analizados, y así sucesivamente hasta que no existan nuevas enlaces o el proceso finalice.

### ¿Qué es un web Scraper?

Un Web Scraper es un programa diseñado para la extracción de información de páginas web de forma automática. El modo de funcionamiento es similar al de una web crawler con la diferencia de que un web scraper extrae información específica de la página web y no sólo enlaces. Por ejemplo, además de enlaces a otras páginas, puede extraer imágenes, títulos de páginas, descripciones, etc.

**Recursos**

### Diferencias entre un web crawler y un web scraper


