![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

# Capitulo 5: Almacenamiento y manipulación de la información

La información que se obtiene a través de diferentes tipos de sistemas y/o dispositivos puede clasificarse de diferentes manera en base a como estos son almacenados. Es decir, si los datos son almacenados en base a algún tipo de estructura o significado preciso que permite identificar su contenido de forma precisa. Es decir que la separación entre los tipos de datos se basa en parte en su significado o etiquetado. 

**Datos estructurados**

El concepto de datos estructurados se refiere a aquel conjunto de datos que tienen una estructura, formato y longitud definida, siendo el formato más común de este tipo de datos una cadena de caracteres alfanuméricos, cómo por ejemplo, el nombre completo de un cliente o su dirección de facturación. Es decir, el significado preciso de cada dato ha sido correctamente definido por un humano y siempre guardan una estructura precisa. Es decir, la información del perfil de los usuarios de una página web, siempre está compuesta por un determinado número de campos, los cuales están siempre etiquetados con un determinado significado. Este tipo de datos han sido almacenados por las empresas desde la aparición de los primeros sistemas de almacenamiento y comúnmente se encuentra almacenados mediante la utilización de algún tipo de base de datos normalmente de tipo relacional. Se considera que este tipo de datos se corresponde con un 20% de la totalidad de datos que actualmente se tienen almacenados. Dependiendo del proceso que su utilice para su generación se pueden diferenciar dos tipos de datos estructurados.

***Datos generados por computador***

Los datos generados por computador son aquellos datos estructurados generados mediante una máquina sin ningún tipo de intervención humana. Algunos ejemplos de este tipo de datos estructurados son:

- Datos de funcionamiento o log: son los diferentes datos de funcionamiento o actividad generados por los diferentes servicios, aplicaciones, redes, etc. Este tipo de información es almacenada en fichero de log que suelen ser almacenados a nivel local en los dispositivos donde se ejecutan los servicios o aplicaciones. La información de log suele contener ingentes cantidades de información lo que suele suponer un coste muy elevado para los organizaciones debido a los cuales suele ser eliminar tras un periodo de tiempo. A pesar de todo es una información muy útil que puede ser utilizada para identificar violaciones de seguridad o errores de ejecución. 
-  Datos de sensores: son datos generados por diferentes tipos de sensores (Acelerómetros, giroscopios, sistemas de identificación por radiofrecuencia, sistema de posición global, etc) los cuales suelen incluir información referente al tipo de sensor y a la información obtenida por ellos. Por ejemplo, uno de los sensores más populares que se están utilizando actualmente son los dispositivos de identificación por radiofrecuencia (Radio Frequency Identification, RFID en sus siglas en inglés) los cuales permiten almancenar información mediante la utilización de etiquetas o tarjetas que utilizan transpondedores RFID. En la siguiente imágen se presenta una ejemplo de una etiqueta RFID la cual está formada por un pequeño microchip que almacena la información del dispositivo y una antena transmisora que permite rastrear el dispositivo y extraer la información que ha sido obtenida por él. Además este tipo de etiquetas puede incluir otro tipo de sensores que permitan recolar más información. 

Figura 3: Ejemplo de un etiqueta RFID

***Datos generados por humanos***

Los datos generados por humanos son aquellos datos generados mediante la utilización de algún tipo de dispositivo y normalmente se corresponde con datos específicos por los usuarios, como por ejemplo sus datos personales, datos bancarios, etc. Algunos ejemplos de este tipo de datos estructurados son:

- Datos de entrada: este tipo de dato se corresponde con aquellos datos que son introducidos mediante algún tipo de interfaz. El ejemplo más típico de datos estructuras son aquellos recogido mediante los diferentes formularios de las aplicaciones móviles o web. 
- Datos de transmisión de clics: este tipo de datos se generan cada vez que hace clic en un enlace en un sitio web. Durante muchos años han sido utilizados para identificar el comportamiento de los usuarios a la hora de interactuar con las aplicaciones y aplicar ciertos cambios con el fin de conseguir un mayor número de usuarios o cambiar el funcionamiento de las aplicaciones. 
- Datos de ejecución en juegos: este tipo de datos se corresponde con acciones realizadas por los jugadores en los videojuegos online, con el fin de conocer la forma en la que jugamos los humanos y generar comportamientos más complejos para los agentes del juego. 

**Datos no estructurados**

El concepto de datos no estructurados se refiere a aquel conjunto de datos que no siguen ningún formato específico, pero tienen algún de realización debido a su formato de almacenamiento o proceso de recolección. Los datos no estructurados más comunes son las imágenes las cuales pueden representar cualquier tipo de contenido, pero son identificadas en base a su formato. Este tipo de datos pueden ser almacenados de diferentes formas, desde una base de datos hasta un conjunto de archivos en un directorio. Se considera que este tipo de datos se corresponde con un 80% de la totalidad de datos que actualmente se tienen almacenados. Muchas personas creen que el término datos no estructurado es un concepto erróneamente utilizado debido a que muchas veces los documento utilizados para generar este tipo de datos tienen una estructura. Por ejemplo, un documento de texto es considerado como un tipo de dato no estructura, pero posee una estructura bien definida está dividido en secciones que a su vez contienen párrafos que están formados por palabras que contienen letras. Pero realmente no sabemos cual es el significado de esos párrafos, o secciones o palabras. Es decir, no sabemos si se corresponden con una canción, un diálogo, un cuento, un comentario o cualquier otro cosa lo que los convierte en datos sin estructura sin significado preciso. Son los datos más comunes y los más difíciles de analizar ya que son datos de tipo general que normalmente no tienen una clasificación o etiquetado. Al igual que los datos de tipo estructurados estos pueden clasificarse en dos grupos dependiendo de si son recogidos mediante un máquina o un humano. 

***Datos generados por computador***

Los datos generados por computador son aquellos datos de tipo no estructurado generados mediante una máquina sin ningún tipo de intervención humana. Algunos ejemplos de este tipo de datos no estructurados son:

- Imágenes de alta resolución: Esto tipo de datos se corresponde con imágenes recogidas por sistema de alta resolución como satélites meteorológicos o satélites  de vigilancia militar. Este tipo de sistemas genera cientos de millones de imágenes, cada una de las cuales tiene un conjunto de información diferentes la cual es difícil de extraer y normalmente ha sido siempre analizada de forma manual por humanos. 
- Imágenes de baja resolución: Este tipo de imágenes se corresponde con información obtenida mediante sistema de seguridad tradicional, como cámaras de video vigilancia que permiten captar imágenes y videos. 
- Datos científicos: Este tipo de datos se corresponde con el conjunto de datos referentes a magnitudes físicas que son recogidos por algún dispositivo de manera directa como pueden ser datos atmosféricos, física de alta energía, etc. 
- Datos de radar o sonar: Esto se corresponde con información global mediante vehículos que no son recogidos mediante ningún tipo de aplicación, datos de tipo meteorológico, datos de tipo sísmicos oceanográficos, etc. 

***Datos generados por humanos***

Los datos generados por humanos son aquellos datos no estructurados generados por humanos, esta información no debe ser generadas mediante ningún tipo de interfaz específico. Algunos ejemplos de este tipo de datos estructurados son:

- Datos de texto: Este tipo de datos se corresponde con toda la información contenida en documentos físicos y/o electrónicos dentro de una organización. Por ejemplo, toda la documentación en papel anterior a las máquinas, encuestas, documentos legales,  correos electrónicos, etc. Este tipo de información no sólo se encuentra almacenada en formato digital, sino también en formato físico, lo que está produciendo que muchas empresas comiencen a digitalizar todo esta información mediante sistemas de tipo de automático o semi-automático.  
- Datos móviles: Este tipo de datos se corresponde con información producida por dispositivos móviles, siendo de este tipo las llamadas telefónicas en el caso de que estas sean grabadas por algún motivo, los mensajes de textos (SMS) y la información global de ubicación de los dispositivos móviles que se obtiene mediante la triangulación por antenas de telefonía. 
- Contenido de aplicaciones: Estos datos se corresponde con toda la información generada mediante la diferentes aplicaciones que no tienen ningún tipo de estructura. La mayoría de ellos se corresponde con la información generada por la redes sociales y se corresponde con cualquier dato sin estructura que incluye diferentes tipo de formato como por ejemplo imágenes, texto planos, emoticones, video, etc. 

**Datos semi-estructurados**

Los datos semi-estructurados son aquellos que no pueden catalogarse en ninguno de los grupo anteriores debido a que tienen algún tipo de estructura definida pero es de tipo variable. Por ejemplo la estructura de una página web está formado por etiquetas basadas en el lenguaje HTML que tienen un significado preciso, pero su número, orden, contenido varia dependiendo de cada una de las páginas webs, por lo que a pesar de ser todos datos de tipo HTML, tienen una estructura parecida pero variable en base al contenido que presenten. Los formatos más comunes utilizados para definir tipos de datos semi-estructurados son los siguientes:

- El Lenguaje de Marcado para Hipertextos (HyperText Markup Language, HTML en sus siglas en inglés)[2][3] es un lenguaje para la definición de la estructura básica de una página web. Se utiliza para definir el contenido de la página web. Este lenguaje es combinado con otros dos lenguajes para describir la apariencia/presentación de una página web (CSS) o su funcionalidad (JavaScript). Este lenguaje está basado en una serie de etiquetas (<head>, <title>, <body>, <header>, <article>, <section>, <p>, <div>, <span>, <img>, etc) que permiten marcar o etiquetar los contenido de la página web de forma que serán mostrados de una manera específica en el navegador web. 
  
- El lenguaje de marcado extensible (Extensible Markup Language, XML en sus siglas en inglés)[4] es un lenguaje de marcado de propósito general que utiliza etiquetas o tags dispuesto de forma jerárquica para identificar la estructura y significado de la información donde no existe un conjunto de etiquetas general. Es decir, las etiquetas utilizadas para representar la información contenida en un archivo XML es definida por los creadores de los ficheros. Este tipo de formato permite la creación de cualquier lenguaje basado en etiquetas. Es considerado como uno de los principales lenguajes utilizados para compartir información de tipo general entre diferentes aplicaciones web. Algunos ejemplos son XHTML, MathML,  XSLT, RSS, y RDF. En la Figura 4 se presenta un ejemplo de un fichero de tipo XML.

- El lenguaje de notación de objetos de JavaScript (JavaScript Object Notation, JSON en sus siglas en inglés)[5] es un lenguaje basado en la notación literal de objetos utilizada por el lenguaje de scripting JavaScript. Debido a su simplicidad y naturaleza se ha convertido en el actual estandar para el transferencia de información superando a XML en parte debido a que puede ser procesado (parseado) mediante la función eval de javascript que está presente en casi todos los navegadores web simplificando en el proceso de análisis sintáctico que tiene cualquier lenguaje. En la Figura 4 se presenta un ejemplo de un fichero de tipo JSON.
  
**Sistemas de almancenamiento de la información**

- [Bases de datos relacionales](./clase_sql.md)
- [Bases de datos no sólo relacionales: Documentales](./clase_doc.md)
- [Bases de datos no sólo relacionales: Columnares](./clase_col.md)
- [Bases de datos no sólo relacionales: Grafo]()
