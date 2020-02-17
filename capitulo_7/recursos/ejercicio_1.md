![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 7 - Ejercicio 01: Creando Regresiones Lineales ##

El objetivo de este ejercicio es construir regresiones lineales de tipo simple y múltiple. Para poder construir nuestros modelos de Machine Learning de forma sencilla vamos a utilizar un servidor de Jupyter Notebooks. Para ello, vamos a construir un contenedor que contenga un servidor Jupyter Notebooks fin de poder desarrollar diferentes tipos de algoritmos de manera sencilla. Este ejercicio ba a estár compuesto de tres fases:

- 1 Desplegando nuestro contenedor Jupyter Notebook
- 2 Construyendo nuestra regresión lineal simple
- 3 Construyendo nuestra regresión lineal múltiple

### Desplegando nuestro contenedor Jupyter Notebook

Docker nos permite desplegar de forma sencilla contenedores utilizando imágenes previamente creadas, para aprender como reutilizar estas imágenes vamos a desplegar un servidor Jupyter Notebook. Existe diferentes maneras de construir nuestro contenedor Jupyter Notebook, (1) mediante la utilización el despligue de una imagen; o (2) mediante la generación de un fichero de despliegue (docker-compose.yml)

**Paso 1: Descargando la imagen**

En primer lugar vamos a descarga la imagen que queremos instalar, para comprobar que imágenes tenemos disponibles podemos ir acceder al listado de imágenes disponibles en dockerhub. Para este ejercicio vamos a utilizar una imagen espécifica para Data Scientisth, que puede descargarse en el siguiente [enlace](https://hub.docker.com/r/jupyter/datascience-notebook/) . 

```
$ docker pull jupyter/datascience-notebook:latest
```

A continuación comprobaremos si la imagen se ha descargado correctamente y está disponible en nuestro repositorio local de imágenes, mediante el siguiente comando:

```
$ docker images 
```

Obteniendo la siguiente salida que nos indica que hemos descargado la imagen mongo en su versión (tag) 3.4.21-xenial hace 6 semanas. 

```
REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
jupyter/datascience-notebook   latest              9e64f3a158ed        2 weeks ago         4.91GB
```

**Paso 2: Desplegandando la imagen **

Una vez que hemos descargado la imagen podemos deplegarla para levantas nuestro servidor MongoDB, mediante el siguiente comando:

```
$ docker run --name=jupyter_server -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes jupyter/datascience-notebook:latest -d
```

**Paso 3: Desplegandando la imagen mediante compose**

La otra alternativa a la creación de nuestro contenedor por linea de comando, es crear nuestro contenedor mediante un fichero de despliegue, para ello tenemos que crear nuestro fichero docker-compose.yml. Además incluiremos la configuración de red necesario para desplegar nuestro contenedor dentro de una futura red de contenedores. 

```
version: '3.4'
services:
  
  jupyter:
    restart: always
    image: jupyter/datascience-notebook:latest
    container_name: jupyter_server 
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
    environment:
      - JUPYTER_ENABLE_LAB=yes
    networks:
      fictizia_ml:
        ipv4_address: 172.24.1.3

networks:
  fictizia_ml:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "true"
    ipam:
      driver: default
      config:
        - subnet: 172.24.1.0/24
```

Una vez construido nuestro fichero de despliegue podemos lanzar nuestro fichero de despliegue mediante el siguiente comando:

```
$ docker-compose -f docker_compose.yml up --build -d
```

**Paso 4: Accediendo a nuestro Jupyter Notebook server**

Una vez que hemos desplegado correctamente nuestro servidor Jupyter Notebook podremos acceder a el mediante la siguiente url:

```
http://localhost:8888/
```

Pero al intentarlo nos solicitará un token de acceso. Para obtener el token de acceso es necesario acceder a los logs del contenedor que hemos desplegado mediante el siguiente comando:


```
$ docker logs jupyter_server
```

La salida de este comando nos mostará todo el log del contenedor donde podremos encontrar el token de acceso para acceder a nuestro servidor Jupyter Notebooks. 

```
Executing the command: jupyter lab
[I 06:21:03.420 LabApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 06:21:04.777 LabApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
[I 06:21:04.778 LabApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
[I 06:21:05.881 LabApp] Serving notebooks from local directory: /home/jovyan
[I 06:21:05.881 LabApp] The Jupyter Notebook is running at:
[I 06:21:05.881 LabApp] http://5778cabb64d7:8888/?token=1e6d710c051275c055ab068fe46b7ef9f5b8a6eb24519bc0
[I 06:21:05.881 LabApp]  or http://127.0.0.1:8888/?token=1e6d710c051275c055ab068fe46b7ef9f5b8a6eb24519bc0
[I 06:21:05.881 LabApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[C 06:21:05.886 LabApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-6-open.html
    Or copy and paste one of these URLs:
        http://5778cabb64d7:8888/?token=1e6d710c051275c055ab068fe46b7ef9f5b8a6eb24519bc0
     or http://127.0.0.1:8888/?token=1e6d710c051275c055ab068fe46b7ef9f5b8a6eb24519bc0
```

**Paso 5: Creando nuestro notebook python**

Una vez que hemos desplegado nuestro servidor Jupyter Notebook y hemos accedido a la consola de inicio. Podremos trabajar con el interfaz:

<img src="./img/jupyter_1.png" alt="Interfaz inicial Jupyter Notebook" width="800"/>

Como podemos observar en la imagen, el posible crear diferentes tipos de elementos (notebooks, scripts, etc). Para la realización de este ejercicio vamos a utilizar un notebook de tipo Python 3. De forma que una vez que pulsemos sobre el botón de python 3 crearemos un nuevo notebook, como se muestra en la siguiente imagen:

<img src="./img/jupyter_3.png" alt="Interfaz inicial Jupyter Notebook" width="800"/>

Este interfaz nos permite crear incluir fragmentos de código python y analizar su resultado una vez que ha sido ejecutado el fragmento de código, cada uno de estos fragmento es representado mediante un id entre corchetes, siendo su significado el siguiente:

- [id]: Identifica un fragmento de código con el id. 
- [*]: Identificado un fragmento de códico en ejecución. 

### 1. Construyendo nuestra regresión lineal simple

**Paso 1.1: Instalando paquetes en Jupyter**

Los notebooks son como entidades independientes que permiten la utilización de cualquier tipo de páquete python y para ellos nos ofrece la posibilidad de instalar paquete mediante la utilización de la sistema de instalación de paquetes pip. Para la instalación de los diferentes paquetes que utilizaremos para la realización de nuestro paquetes tenemos que ejecutar el siguiente comando:

```
!pip install pandas scikit-learn numpy seaborn matplotlib tensorflow==1.15
```

Como podemos observar, es necesario incluir el caracter __!__ antes del comando de instalación. A continuación hay que seleccionar el fragmento y pulsar la tecla play para ejecutar el código contenido en el fragmento. Siendo el resultado de la ejecución de esta linea, el siguiente:

```
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Requirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (0.25.3)
Requirement already satisfied: scikit-learn in /opt/conda/lib/python3.7/site-packages (0.22.1)
Requirement already satisfied: numpy in /opt/conda/lib/python3.7/site-packages (1.17.5)
Requirement already satisfied: seaborn in /opt/conda/lib/python3.7/site-packages (0.9.0)
Requirement already satisfied: matplotlib in /opt/conda/lib/python3.7/site-packages (3.1.1)
Collecting tensorflow==1.15
  Using cached tensorflow-1.15.0-cp37-cp37m-manylinux2010_x86_64.whl (412.3 MB)
```

En este caso no se ha realizado la instalación de ningún paquete debido a que todos ya estaban instalados en el servidor Jupyter. 

**Paso 1.2: Inportando librerías**

Una vez que se ha realizado la instalación de los diferentes paquetes python, es necesario importar aquellas clases y métodos necesarios para la realización del ejercicio.

```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

import pandas as pd
import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
```

En este caso vamos a utilizar los datos contenidos en el dataset de SKLearn Boston, el cual contiene información sobre el precio de las viviendas en la ciudad de Boston. Además hemos incluido una serie de librerias para la manipulación de los datos (pandas, numpy y math), otras para el proceso de aprendizaje (model_selection, tensorflow) y otras para la visualización de los resultados (matplotlib y seaborn).

**Paso 1.3: Análisis y manipulación de los datos **

A continuación vamos a cargar nuestro datos. Para ellos vamos a utilizar la función __load_boston__ que carga los datos del dataset en bruto (raw). Una vez cargados los datos vamos a transformalos en un DataFrame de pandas con el fin de poder analizar y manipular el conjunto de datos.

```
raw_data = load_boston()

features_names = list()

for feature in raw_data['feature_names']:
    features_names.append(feature)
features_names.append('FEATURE')

data = pd.DataFrame(data=np.c_[raw_data['data'], raw_data['target']], columns=features_names)
```

Una vez generado el DataFrame es posible visualizar su contenido de forma sencilla. Podemos utilizar la función __data.head()__ para visualizar en formato tabla la información de las primeras 5 instancias de datos. También podemos utilizar la función __sns.countplot(data=data, x='FEATURE')__ sobre la característica __FEATURE__ con el fin de generar un gráfico con la distribución de sus valores. 

**Paso 1.4: Preparación de los datos **

El siguiente paso consiste en preparar los datos para que sean utilizados durante el proceso de aprendizaje. Para este ejercició hemos decidido utilizar la edad (AGE) de las viviendas como variable independiente y coste (FEATURE) de la vivienda como variable dependiente. Para ello es necesario extraer la información referente a ambas variables del dataset y convertirla en un array:

```
classes = data['FEATURE']
features = data['AGE']

X = np.asarray(features)
Y = np.asarray(classes)
```

A continuación es necesario construir los conjuntos de entrenamiento y test. Para ellos vamos a utilizar la función __train_test_split__ que nos permite dividir el conjunto de datos en dos conjuntos (entrenamiento y test) indicando el tamaño que queremos utilizar para el conjunto de test. En este caso, vamos a generar un conjunto de test con el 20% de los elementos del conjunto de instancias inicial. 

```
n_samples = X.shape[0]

X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2)

n_samples_train = X_train.shape[0]
n_samples_test = Y_train.shape[0]
```

**Paso 1.5: Construyendo el procesos de entrenamiento **

Una vez que hemos prepado nuestros datos tenemos que construir nuestro algoritmo de aprendizaje mediante la utilización de tensorflow. Para ello vamos a crear una función reutilizable, que nos permitirá ejecutar diferentes procesos de aprendizaje con el objetivo de modificar algunos de los hiperparametros del proceso e intentar conseguir el mejor modelo posible. La función se denominará __train__ y utilizará 5 parámetros de entrada:

- X_train: Es el conjunto de ejemplos de entrenamiento.
- Y_train: Es el resultado esperado de cada uno de los ejemplos de entrenamiento. 
- n_samples: Es un valor numerico que se corresponde con el número de ejemplos de entrenamiento.
- learning_rate: Es la tasa de aprendizaje del algoritmo de entrenamiento. Su valor estará comprendido entre 0 y 1. 
- training_epochs: Es el número de iteraciones del proceso de entrenamiento con el fin de minimizar el error y conseguir el mejor modelo. Su valor estár comprendido entre 1 y +inf. 

Para la creación de este proceso utilizaremos diferentes elementos del framework de tensorflow. En primer lugar debemos definir las diferentes variables que vamos a utilizar. En este caso utilizaremos dos tipos de variables:

- placeholder: Son las variables de entrada (inputs) del algoritmo. Se generan mediante el método __tf.placeholder__
- Variable: Son las variables que se utilizan durante la ejecución del algoritmo, en este caso son las variables que queremos calcular (pendiente e interceptor de y). Se generan mediante el método __tf.Variable__.  

Una vez definidas las variables tenemos que construir dos ecuaciones:

- La ecuación de la recta que nos permitirá calcular el valor a predecir en base a las variables que va calculando el algoritmos (pendiente e interceptor de y). Esta ecuación se corresponde con la ecuación de la recta. 
- La ecuación de coste (error) que nos permitirá calcular la diferencia entre el valor obtenido por la ecuación de la recta y el resultado experado que se conoce previamente. Para ello utilizaremos la técnica de [mínimos cuadrados](https://es.wikipedia.org/wiki/M%C3%ADnimos_cuadrados). Este valor será utilizado por el algoritmo de optimización que elijamos para intertar mejorar los valores que se van calculando en cara iteración. Para este ejecicio vamos a utilizar el algoritmo de [Optimización del descenso del gradiente](http://numerentur.org/gradiente-descendente/) con el fin de minimizar el error mediante la función __tf.train.GradientDescentOptimizer__. 

```
HISTORY_NAMES = ['loss', 'mae', 'a', 'b', 'epoch']

def train(X_train, Y_train, n_samples, learning_rate, training_epochs):
    
    history = []
    
    X = tf.placeholder("float", name="X")
    Y = tf.placeholder("float", name="Y")

    y_intercept_pred = tf.Variable(np.random.randn(), name="y_intercept")
    slope_pred = tf.Variable(np.random.randn(), name="slope")

    y_pred = tf.add(tf.multiply(X, slope_pred), y_intercept_pred)

    cost = tf.reduce_sum(tf.pow(y_pred-Y, 2))/(2 * n_samples_train)

    optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
    
```

Una vez que se han definido todas las variables y funciones necesarias para el proceso de aprendizaje, podemos construir el bucle en tensorflow. Para ello primero deberemos inicializar la variables mediante el método __tf.global_variables_initializer__. Este método inicializará todas las variables definidas previamente cuando se ejecute dentro de la sesion. A continuación será necesario crear una sesión en tensorflow para poder ejecutar todas nuestras funciones, siendo la primera la que inicializa la variables mediante la ejecución del método __session.run(init)__ de la sesión previamente creada. 

```
    init = tf.global_variables_initializer()

    with tf.Session() as session:

        session.run(init)
```

Una vez inicializadas las variables podemos comenzar el bucle de aprendizaje que se ejecutará tantas veces como iteraciones de entrenamiento. Cada una de las iteraciones de este bucle calculará un nuevo valor para la pediente (slope_pred) y el interceptor de la y (y_intercept_pred) mediante el proceso de optimización seleccionado. Para ello se utilizarn todos los ejemplos de entrenamiento. 

```
        for epoch in range(training_epochs):
            
            mae = 0
            
            for (x, y) in zip(X_train, Y_train):
                session.run(optimizer, feed_dict={X: x, Y: y})
                mae += session.run(cost, feed_dict={X: x, Y: y})
```

Además para cada una de la iteraciones recogeremos una serie de valores (mae, error, slope y y_intercept) con el objetivo de analizar la evolución de estos valores una vez terminado el proceso de entrenamiento. 

```
            mae = mae / len(X_train)
            cost_error = session.run(cost, feed_dict={X: X_train, Y: Y_train})
            slope = session.run(slope_pred)
            y_intercept = session.run(y_intercept_pred)

```
Los mostraremos cada 25 iteraciones con el fin de visualizar la evolución de nuestro proceso de aprendizaje. 

```
 
            if (epoch + 1) % 25 == 0:
                cost_error = session.run(cost, feed_dict={X: X_train, Y: Y_train})
                slope = session.run(slope_pred)
                y_intercept = session.run(y_intercept_pred)
                print("Iteración: " + str(epoch+1) + ": Loss=" + str(cost_error) + " con a=" + str(slope) + " y b=" + str(y_intercept))
            
            iteration = [cost_error, mae, slope, y_intercept, epoch+1]
            history.append(iteration)    

```

Una vez finalizar el proceso de entrenamiento, utilizaremos el último valor calculado para la pendiente y el interceptor de la y con el fin de calcular el resultado de nuestra recta de regresión sobre el conjunto de entrenamiento y la información que hemos recolectado durante el proceso de entrenenamiento. 

```

        slope = session.run(slope_pred)
        y_intercept = session.run(y_intercept_pred)

        return (slope * X_train) + y_intercept, pd.DataFrame(data=history, columns=HISTORY_NAMES)

```

**Paso 1.6: Visualizando el resultado del proceso de entrenamiento**

Una vez realizado el proceso de entrenamiento vamos a utilizar la información recolectada por el proceso de entrenamiento con el fin de visualizar su evolución. Para ellos vamos a crear una función que denominaremos __print_chart__ y utilizará 7 parámetros de entrada:

- X_train: Es el conjunto de ejemplos de entrenamiento.
- Y_train: Es el resultado esperado de cada uno de los ejemplos de entrenamiento. 
- label_x: Es la etiqueta que se utilizará en la gráfica de aprendizaje para el eje x (Variable independiente). 
- label_y: Es la etiqueta que se utilizará en la gráfica de aprendizaje para el eje y (Variable dependiente). 
- result: Es el conjunto de valores utilizando la recta de regresión calculada por el algoritmo de aprendizaje. 
- history_data: Es el DataFrame generado por el proceso de aprendizaje. 
- training_epochs: Es el número de iteraciones del proceso de entrenamiento con el fin de minimizar el error y conseguir el mejor modelo. Su valor estár comprendido entre 1 y +inf. 

En la primera parte de la función mostraremos la grafica de evolución del coste (loss) que intentamos minimizar para conseguir la mejor recta de regresión

```
def print_chart(X_train, Y_train, label_x, label_y, result, history_data, training_epochs):
    
    plt.figure()
    plt.plot(history_data.epoch, history_data.loss, 'ro', label='Evolución del coste')
    plt.xlabel('Iteración')
    plt.ylabel('Coste (loss)')
    plt.legend('Evolución del coste (loss) durante el proceso de aprendizaje')

```

En la segunda parte de la función mostramos la recta de regresión obtenida tras el proceso de aprendizaje sobre el conjunto de entrenamiento. 

```
    plt.figure()
    plt.plot(X_train, Y_train, 'ro', label='Aprendizaje tras ' + str(training_epochs) + 'iteraciones')
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.plot(X_train, result, label="Recta de regresión")
    plt.show()
```

**Paso 1.7: Ejecutando nuestro proceso de aprendizaje**

Una vez construidas nuestras funciones podemos ejecutar nuestro proceso de aprendizaje de la siguiente manera, ejecutando el proceso de aprendizaje durante 100 iteraciones con una tasa de aprendizaje del 0.06. 

```
learning_rate = 0.06
training_epochs = 100

result, history_result = train(X_train, Y_train, n_samples_train, learning_rate, training_epochs)
print_chart(X_train, Y_train, 'Edad', 'Precio', result, history_result, training_epochs)
```

Siendo el resultado obtenido tras ejecutar el codígo el siguiente:

```
Iteración: 25: Coste=98.71037 con a=0.26858303 y b=5.9782166
Iteración: 50: Coste=84.432076 con a=0.20912959 y b=11.179977
Iteración: 75: Coste=75.92339 con a=0.16129795 y b=15.364909
Iteración: 100: Coste=71.00587 con a=0.12281656 y b=18.73176
```

<img src="./img/regresion_results_1.png" alt="Resultado de regresión lineal simple tras 100 iteraciones" width="800"/>

Ahora podemos modificar el número de iteraciones y la tasa de aprendizaje con el fin de aplicar todos los procesos de regresión simple sobre el dataset elegido de forma sencilla. Puedes ver el código completo en la (solución)[../ejercicio_1/regresion_lineal_simple.ipynb]

### 2. Construyendo nuestra regresión lineal múltiple

La mayoría de los problemas que queremos resolver no están formados por una única variable independiente, sino por múltiples. Por lo que es importante aprender como construir regresiones lineales múltiples con el fin de construir modelos que sean capaces de utilizar múltiples variables de entrada. Para ello vamos a construir una regresión lineal multiple utilizando el mismo dataset del ejercicio anterior.

**Paso 2.1: Instalando paquetes en Jupyter**

Los notebooks son como entidades independientes que permiten la utilización de cualquier tipo de páquetes python y para ello nos ofrece la posibilidad de instalar paquete mediante la utilización de la sistema de instalación de paquetes pip. Para la instalación de los diferentes paquetes que utilizaremos para la realización de nuestro paquetes tenemos que ejecutar el siguiente comando:

```
!pip install pandas scikit-learn numpy seaborn matplotlib tensorflow==1.15
```

Como podemos observar, es necesario incluir el caracter __!__ antes del comando de instalación. A continuación hay que seleccionar el fragmento y pulsar la tecla play para ejecutar el código contenido en el fragmento. Siendo el resultado de la ejecución de esta linea, el siguiente:

```
WARNING: pip is being invoked by an old script wrapper. This will fail in a future version of pip.
Please see https://github.com/pypa/pip/issues/5599 for advice on fixing the underlying issue.
To avoid this problem you can invoke Python with '-m pip' instead of running pip directly.
Requirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (0.25.3)
Requirement already satisfied: scikit-learn in /opt/conda/lib/python3.7/site-packages (0.22.1)
Requirement already satisfied: numpy in /opt/conda/lib/python3.7/site-packages (1.17.5)
Requirement already satisfied: seaborn in /opt/conda/lib/python3.7/site-packages (0.9.0)
Requirement already satisfied: matplotlib in /opt/conda/lib/python3.7/site-packages (3.1.1)
Collecting tensorflow==1.15
  Using cached tensorflow-1.15.0-cp37-cp37m-manylinux2010_x86_64.whl (412.3 MB)
```

En este caso no se ha realizado la instalación de ningún paquete debido a que todos ya estaban instalados en el servidor Jupyter. 

**Paso 2.2: Inportando librerías**

Una vez que se ha realizado la instalación de los diferentes paquetes python, es necesario importar aquellas clases y métodos necesarios para la realización del ejercicio.

```
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

import pandas as pd
import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
```

En este caso vamos a utilizar los datos contenidos en el dataset de SKLearn Boston, el cual contiene información sobre el precio de las viviendas en la ciudad de Boston. Además hemos incluido una serie de librerias para la manipulación de los datos (pandas, numpy y math), otras para el proceso de aprendizaje (model_selection, tensorflow) y otras para la visualización de los resultados (matplotlib y seaborn).

**Paso 2.3: Análisis y manipulación de los datos **

A continuación vamos a cargar nuestro datos. Para ellos vamos a utilizar la función __load_boston__ que carga los datos del dataset en bruto (raw). Una vez cargados los datos vamos a transformalos en un DataFrame de pandas con el fin de poder analizar y manipular el conjunto de datos.

```
raw_data = load_boston()

features_names = list()

for feature in raw_data['feature_names']:
    features_names.append(feature)
features_names.append('FEATURE')

data = pd.DataFrame(data=np.c_[raw_data['data'], raw_data['target']], columns=features_names)
```

Una vez generado el DataFrame es posible visualizar su contenido de forma sencilla. Podemos utilizar la función __data.head()__ para visualizar en formato tabla la información de las primeras 5 instancias de datos. También podemos utilizar la función __sns.countplot(data=data, x='FEATURE')__ sobre la característica __FEATURE__ con el fin de generar un gráfico con la distribución de sus valores. 

**Paso 2.4: Preparación de los datos **

El siguiente paso consiste en preparar los datos para que sean utilizados durante el proceso de aprendizaje. Para este ejercició hemos decidido utilizar la edad (AGE) y el número de habitaciones (RM) de las viviendas como variable independiente y coste (FEATURE) de la vivienda como variable dependiente. En este paso es donde se produce el primer cambio respecto a la regresión lineal simple, ahora tenemos dos variables dependientes que forman una matriz de valores. Esto supone un cambio en la estructura de la ecuación de la recta como veremos posteriomente. Al igual que en ejemplo anterior es necesario extraer la información referente a las tres variables del dataset y convertirla en arrays.

```
classes = data['FEATURE']
features = data[['AGE', 'RM']]

X = np.asarray(features)
Y = np.asarray(classes)
```

A continuación es necesario construir los conjuntos de entrenamiento y test. Para ellos vamos a utilizar la función __train_test_split__ que nos permite dividir el conjunto de datos en dos conjuntos (entrenamiento y test) indicando el tamaño que queremos utilizar para el conjunto de test. En este caso, vamos a generar un conjunto de test con el 20% de los elementos del conjunto de instancias inicial. 

```
n_samples = X.shape[0]

X_train, x_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2)

n_samples_train = X_train.shape[0]
n_samples_test = Y_train.shape[0]
```

**Paso 2.5: Construyendo el procesos de entrenamiento **

Una vez que hemos prepado nuestros datos tenemos que construir nuestro algoritmo de aprendizaje mediante la utilización de tensorflow. Para ello vamos a crear una función reutilizable, que nos permitirá ejecutar diferentes procesos de aprendizaje con el objetivo de modificar algunos de los hiperparametros del proceso e intentar conseguir el mejor modelo posible. La función se denominará __train__ y utilizará 5 parámetros de entrada:

- X_train: Es el conjunto de ejemplos de entrenamiento.
- Y_train: Es el resultado esperado de cada uno de los ejemplos de entrenamiento. 
- n_samples: Es un valor numerico que se corresponde con el número de ejemplos de entrenamiento.
- learning_rate: Es la tasa de aprendizaje del algoritmo de entrenamiento. Su valor estará comprendido entre 0 y 1. 
- training_epochs: Es el número de iteraciones del proceso de entrenamiento con el fin de minimizar el error y conseguir el mejor modelo. Su valor estár comprendido entre 1 y +inf. 

Para la creación de este proceso utilizaremos diferentes elementos del framework de tensorflow. En primer lugar debemos definir las diferentes variables que vamos a utilizar. En este caso utilizaremos dos tipos de variables:

- placeholder: Son las variables de entrada (inputs) del algoritmo. Se generan mediante el método __tf.placeholder__. Aunque en este caso es necesario definir el shape de las variables debido a que una de ellas es una matriz. Para ello utilizaremos la propiedade __shape=(n, None)__ que nos permite indicar el formato de los datos que en este caso será n (número de variables del conjunto de datos de entrada). 
- Variable: Son las variables que se utilizan durante la ejecución del algoritmo, en este caso son las variables que queremos calcular (pendiente e interceptor de y). Se generan mediante el método __tf.Variable__. Del mismo modo que en caso anterio es necesario definir el formato de los datos para la pendiente, ya que en este caso tenemos múltiples pendiente de forma que utilizaremos la propierdad __shape=(1, n)__. 

Una vez definidas las variables tenemos que construir dos ecuaciones:

- La ecuación de la recta que nos permitirá calcular el valor a predecir en base a las variables que va calculando el algoritmos (pendiente e interceptor de y). Esta ecuación se corresponde con la ecuación de la recta, aunque en este caso la operacin de multiplicacin de la variable x por la pendiente se ha sustituido por una multiplicacin de matrices. 
- La ecuación de coste (error) que nos permitirá calcular la diferencia entre el valor obtenido por la ecuación de la recta y el resultado experado que se conoce previamente. Para ello utilizaremos la técnica de [mínimos cuadrados](https://es.wikipedia.org/wiki/M%C3%ADnimos_cuadrados). Este valor será utilizado por el algoritmo de optimización que elijamos para intertar mejorar los valores que se van calculando en cara iteración. Para este ejecicio vamos a utilizar el algoritmo de [Adam](https://arxiv.org/abs/1412.6980https://arxiv.org/abs/1412.6980) con el fin de minimizar el error mediante la función __tf.train.AdamOptimizer__. 

```
HISTORY_NAMES = ['loss', 'mae', 'a', 'b', 'epoch']

def train(X_train, Y_train, n_samples, learning_rate, training_epochs):
    
    history = []
    
    n = X_train.shape[1]
    
    X = tf.placeholder(tf.float32, shape=(n, None), name="X")
    Y = tf.placeholder(tf.float32, shape=(1, None), name="Y")

    y_intercept_pred = tf.get_variable(shape=(), name="y_intercept")
    slope_pred = tf.get_variable(shape=(1, n), name="slope_pred")
    
    y_pred = tf.matmul(slope_pred, X) + y_intercept_pred
    
    Loss = tf.reduce_sum((y_pred - Y)**2)
    
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(Loss)
    
```

Una vez que se han definido todas las variables y funciones necesarias para el proceso de aprendizaje, podemos construir el bucle en tensorflow. Para ello primero deberemos inicializar la variables mediante el método __tf.global_variables_initializer__. Este método inicializará todas las variables definidas previamente cuando se ejecute dentro de la sesion. A continuación será necesario crear una sesión en tensorflow para poder ejecutar todas nuestras funciones, siendo la primera la que inicializa la variables mediante la ejecución del método __session.run(init)__ de la sesión previamente creada. 

```
    init = tf.global_variables_initializer()

    with tf.Session() as session:

        session.run(init)
```

Una vez inicializadas las variables podemos comenzar el bucle de aprendizaje que se ejecutará tantas veces como iteraciones de entrenamiento. Cada una de las iteraciones de este bucle calculará un nuevo valor para la pediente (slope_pred) y el interceptor de la y (y_intercept_pred) mediante el proceso de optimización seleccionado. Para ello se utilizarn todos los ejemplos de entrenamiento. 

```
        mae = 0

        for epoch in range(training_epochs):
             
            _, current_loss, current_slope, current_y_intercept = session.run([optimizer, Loss, slope_pred, y_intercept_pred], feed_dict={
                X: X_train.transpose(),
                Y: Y_train.transpose()
            })
```

Además para cada una de la iteraciones calcularemos el sólo el mae, ya que el resto de valores son generados en el proceso de aprendizaje, con el objetivo de analizar la evolución de estos valores una vez terminado el proceso de entrenamiento. 

```
            mae = current_loss / len(X_train)

```
Los mostraremos cada 25 iteraciones con el fin de visualizar la evolución de nuestro proceso de aprendizaje. 

```
 
            if (epoch + 1) % 25 == 0:
                slope = session.run(slope_pred)
                print("Iteración: " + str(epoch+1) + ": Loss=" + str(current_loss) + " con as=" + str(current_slope) + ", b=" + str(current_y_intercept))
            
            iteration = [current_loss, mae, current_slope, current_y_intercept, epoch+1]
            history.append(iteration)    

```

Una vez finalizado el proceso de entrenamiento, utilizaremos el último valor calculado para la pendiente y el interceptor de la y con el fin de calcular el resultado de nuestra recta de regresión sobre el conjunto de entrenamiento y la información que hemos recolectado durante el proceso de entrenenamiento. 

```

        slope = session.run(slope_pred)
        y_intercept = session.run(y_intercept_pred)

        return (slope * X_train) + y_intercept, pd.DataFrame(data=history, columns=HISTORY_NAMES)

```

**Paso 2.6: Visualizando el resultado del proceso de entrenamiento**

Una vez realizado el proceso de entrenamiento vamos a utilizar la información recolectada por el proceso de entrenamiento con el fin de visualizar su evolución. Para ellos vamos a crear una función que denominaremos __print_chart__ y utilizará 7 parámetros de entrada:

- X_train: Es el conjunto de ejemplos de entrenamiento.
- Y_train: Es el resultado esperado de cada uno de los ejemplos de entrenamiento. 
- label_x: Es la etiqueta que se utilizará en la gráfica de aprendizaje para el eje x (Variable independiente). 
- label_y: Es la etiqueta que se utilizará en la gráfica de aprendizaje para el eje y (Variable dependiente). 
- result: Es el conjunto de valores utilizando la recta de regresión calculada por el algoritmo de aprendizaje. 
- history_data: Es el DataFrame generado por el proceso de aprendizaje. 
- training_epochs: Es el número de iteraciones del proceso de entrenamiento con el fin de minimizar el error y conseguir el mejor modelo. Su valor estár comprendido entre 1 y +inf. 

En la primera parte de la función mostraremos la grafica de evolución del coste (loss) que intentamos minimizar para conseguir la mejor recta de regresión

```
def print_chart(X_train, Y_train, label_x, label_y, result, history_data, training_epochs):
    
    plt.figure()
    plt.plot(history_data.epoch, history_data.loss, 'ro', label='Evolución del coste')
    plt.xlabel('Iteración')
    plt.ylabel('Coste (loss)')
    plt.legend('Evolución del coste (loss) durante el proceso de aprendizaje')

```

En la segunda parte de la función mostramos la distribución de los valores en formato 3D con el fin de analizar la distribución de valores utilizados. 

```
    plt.figure()
    ax = plt.axes(projection='3d')
    
    xdata = X_train[:,0]
    ydata = X_train[:,1]
    zdata = Y_train[:,0]
   
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
    plt.show()
```

**Paso 2.7: Ejecutando nuestro proceso de aprendizaje**

Una vez construidas nuestras funciones podemos ejecutar nuestro proceso de aprendizaje de la siguiente manera, ejecutando el proceso de aprendizaje durante 100 iteraciones con una tasa de aprendizaje del 0.06. 

```
learning_rate = 0.06
training_epochs = 100

result, history_result = train(X_train, Y_train, n_samples_train, learning_rate, training_epochs)
print_chart(X_train, Y_train, 'Edad', 'Precio', result, history_result, training_epochs)
```

Siendo el resultado obtenido tras ejecutar el codígo el siguiente:

```
Iteración: 25: Loss=57618.28 con as=[[0.15290189 0.987823]], b=1.9863163
Iteración: 50: Loss=36299.77 con as=[[0.06888402 2.117016]], b=3.0250173
Iteración: 75: Loss=25638.203 con as=[[-0.01295658  2.999957]], b=3.7998881
Iteración: 100: Loss=21568.828 con as=[[-0.06754547  3.6055403]], b=4.2649207
```

<img src="./img/regresion_results_2.png" alt="Resultado de regresión lineal multiple (2 variables) tras 100 iteraciones" width="800"/>

Ahora podemos modificar el número de iteraciones y la tasa de aprendizaje con el fin de aplicar todos los procesos de regresión multiple sobre el dataset elegido de forma sencilla. Además es posible añadir mas variables independientes al proceso de aprendizaje, aunque sería necesario modificar la función de visualización. Puedes ver el código completo en la (solución)[../ejercicio_1/regresion_lineal_multiple.ipynb]
