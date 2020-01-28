![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 6 - Clase 4: Tratamiento y enriquecimiento de la información mediante Cloud DataFlow ##

### Introducción a Cloud DataFlow ###

Cloud Dataflow es un servicio completamente administrado de GCP para transformar y enriquecer datos que son ingeridos mediante proceso de streaming (tiempo real) o batch (lotes). Debido a su enfoque de aprovisionamiento y administración de recursos sin servidores, permite acceder a una capacidad "prácticamente" ilimitada de recursos para el desarollo de sistema de procesamiento de datos. Actualmente existen un amplio número de procesos de transformación, debido a su versatilidad y al amplio uso que está realizando las empresas de servicio. Debido a ellos DataFlow ofrece casos prácticos de procesos de transformación para diferentes áreas, entre los que se incluyen:

- Análisis de flujo de clics, puntos de venta y segmentación en el comercio minorista.
- Detección de fraude en servicios financieros.
- Anális de experiencia del usuario personalizada en videojuegos.
- Análisis y visualización de estadísticas de IoT en la fabricación, salud y logística.

<img src="https://cloud.google.com/dataflow/images/diagram-dataflow.png?hl=es-419" alt="Diagrama de funcionamiento de dataflow" width="800"/>

**Recursos**

- [Introducción a Cloud DataFlow](https://airflow.apache.org/docs/stable/)
- [Guía de uso rápido de Cloud DataFlow para Python](
https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python?hl=es-419)
- [Guía de uso rápido de Cloud DataFlow para Java](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-java-maven?hl=es-419)
- [QuickLabs Cloud DataFlow](https://www.qwiklabs.com/focuses/1100?locale=es&parent=catalog)
- [Instalación de Cloud DataFlow mediante Pypi - Python](https://pypi.org/project/google-cloud-dataflow/)
- [Página oficial del proyecto Apache Beam](https://beam.apache.org/)
- [Documentación oficial del proyecto Apache Beam](https://beam.apache.org/documentation/)
- [Guía de inicio sobre Apache Beam](https://beam.apache.org/get-started/beam-overview/)


### Introducción a Apache Beam ###

Cloud DataFlow es una tecnología basada en el proyecto [Apache Beam]() del ecosistema Apache que aparecio en 2016. Apache Beam es un modelo de programación que permite desarrollar, de forma sencilla, procesos o aplicaciones para el tratamientos de datos en batch (lotes) y streaming que pueden ser desplegadas en cualquier "motor de ejecución" utilizando diferentes interfaces de entrada y salida. 

El modelo de Apache Beam se basa en la utilización de abstracciones que te aíslan de los detalles de bajo nivel del procesamiento distribuido, como la coordinación de trabajadores individuales, la fragmentación de conjuntos de datos y otras tareas similares. Este modelo está basa en tres conceptos básicos: 

__Conceptos básicos__

- Pipelines o "Canalizaciones": Un Pipeline es una secuencia de procesos (secuenciales o paralelos) que implica todo el flujo de tratamiento y manipulación de la información. Es decir, un pipeline suele incluir los procesos de lectura de datos de entrada a partir de un sistema de almacenamiento, los diferentes procesos de transformación y la escritura de los datos en un sistema de almacenamiento. Las aplicaciones o programas desarrollados mediante Apache Beam utilizan como base un objeto de tipo Pipeline y, a partir de ahí utilizan ese objeto como base para la creación de las canalizaciones (PColection). 

- PCollection o "colecciones": Son representaciones abstractas de un conjunto de datos de elementos múltiples que puede distribuirse. Una canalización puede contener un conjunto de datos de un tamaño fijo o un conjunto de datos no delimitado de una fuente de datos que se actualiza continuamente.

- PTransform o "transformaciones": Son operación de procesamiento que realizan transformaciones sobre los datos contenidos en una colección. Una transformación utiliza uno o más objetos de tipo PCollection como entrada, realiza una operación sobre cada uno de los elementos de esa colección y genera uno o más objetos PCollection como salida. Una transformación puede realizar casi cualquier tipo de operación de procesamiento, lo que incluye cálculos matemáticos, conversiones de datos de un formato a otro, agrupación, lectura y escritura, filtrado, etc. 

- Conectores de Entrada/Salida: Los conectores de Entrada y Salida (I/O) de Apache Beam permiten leer y escribir datos a través de las canalizaciones. Un conector de Entrada y salida (I/O) está formado por dos elementos: (1) un origen o fuente y (2) un destino. En Apache Beam los origenes y destinos de los conectores son transformaciones que permiten que las canalizaciones funcionen con datos. 

- ParDo: ParDo es la operación de procesamiento paralelo central de Apache Beam. Esta operación permite invocar una función especificada por el usuario que será aplicada sobre cada uno de los elementos del objeto PCollection que está siendo utilizado como entrada. Este proceso recopila los elementos de salida en un objeto PCollection. Una de las grandes ventajas de la operación ParDo es que permite el procesamiento de los elementos de forma individual y paralelo.

- Agregación: La agregación es una operación de procesamiento que  algunos valores de varios elementos de entrada. El principal patrón de procesamiento para agregación en Apache Beam es agrupar todos los elementos con una clave y ventana comunes. Luego, combina cada grupo de elementos con una operación asociativa y conmutativa.
Funciones definidas por el usuario (UDF)
