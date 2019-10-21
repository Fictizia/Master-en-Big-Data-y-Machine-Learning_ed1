![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 1 - Clase 02

En esta segunda clase del capítulo 1 se describirán como construir nuestros primeros programas en python con el fin de 
poder realizar los diferentes trabajos del máster. 

2.1 Instalación
2.2 Elementos básicos en python
2.3 Creando mi primer programa python
2.4 El flujo de ejecución
2.5 Funciones
2.6 Variables (locales y globales)
2.7 Clases y objetos
2.8 Tipos de datos básicos


### Creando mis primeros programas en python

Python es un lenguaje de programación en scripting. Es un lenguje interpretado, orientado a objetos con tipado dinámico, 
que  permite el desarrollo de algoritmos sencillos basados en un scripting, así como algoritmos complejos desarrollados 
con múltiples clases. 

**2.1 Instalación**

Instalamos [python 3.7]()


**2.2 Elementos básicos en python: La consola**

Python puede ejecutar mediante scripts desarrollados en uno o varios ficheros que interactuan entre sí o directamente en 
el terminal del sistema operativo. Actualmente python ofrece dos versión

* Python 2.7 que puede invocarse mediante el comando python
* Python 3.6 o 3.7 que puede invocarse mediante el comando python3. Esta será nuestra elección para la ejecución de los diferentes scripts que desarrollaremos en el máster. 

**2.2 Elementos básicos en python: La versión de python**

Para comprobar la versión de python que vamos a utilizar deberemos comprobar que versiones tenemos disponibles, siendo la 
versión por defecto de la mayoría de los sistemas operativos, la versión 2.7. 

Salida generada al ejecutar el comando python en Ubuntu 18.04

```
python --version
Python 2.7.15+

```

Salida generada al ejecutar el comando python3 en Ubuntu 18.04
```
python3 --version
Python 3.6.8

```

**2.2 Elementos básicos en python: Jugueteando con la consola**

Python puede utilizar directamente usando la consola mediante un interprete de comando, creando de esta manera una sesión 
para la ejecución de comandos.

```
python3
Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```

Sientete libre de escribir algunos comando básicos como los siguientes:

Impresión de una cadena de caracteres.

```
>>> print("hola2")
hola2
>>> 

```

Asignación de un valor a una varible e impresión de su contenido.

```
>>> a = 10
>>> print(a)
10
>>> 

```

Finalizar la ejecución del interprete de comando. 

```
>>> exit()
```

Además de salir del interprete del comando, la función exit() nos permite finalizar la ejecución de un programa en python en 
cualquier momento. Si queremos informar del tipo de salida que se ha producido, podemos incluir un valor en la función por 
ejemplo exit(10) generando como salida el valor 10. El valor 10 puede tener un significado específico permitiendo que nuestro 
programa termine de diferentes maneras utilizando diferentes valores (códigos). 

**2.3 Creando mi primer programa python**

Los archivos que incluyen código python utilizan la extensión .py. A pesar de ser un lenguaje interpretado es necesario 
compilar el código cada vez que se produce un cambio en el archivo de código fuente python (*.py) de modo que se produce 
una nueva compilación que generar un archivo con extensión .pyc (Si borramos este tipo de archivos se vuelve a producir 
una nueva compilación).

La estructura de un archivo python se puede dividir en tres grupos de información:

* La cabecera (opcional) nos permite definir el programa que ejecutará nuestro archivo por defecto en entorno unix (Linux y Mac) 
esta cabecera indicará al interprete de comando (terminal) el programa que deberá ejecutar el código. 

  Cabecera para python 

  ```
  #!/usr/bin/env python

  print('Holaaaa')

  ```

  Cabecera para python 3

  ```
  #!/usr/bin/env python

  print('Holaaaa')

  ```

* Los comentarios (opcional) nos permiten incluir información útil para los desarrolladores que no será ejecutada por el compilador.


   Ejemplo de comentarios en python

  ```
  #!/usr/bin/env python3
  
  # Este es un comentario para nuestro ejemplo
  # escrito en dos lineas
 
  """ Aunque es posible escribir un comentario multilinea. Donde
      el texto se distribuye en múltiples
      linea as """
      
  print('Holaaaa') # Aúnque también podemos escribir aquí 
 
  """ Utilizar una multilinea con una sóla linea """
  
  ```

**El flujo de ejecución**

Los programas en python siguen el flujo de ejecución en base al orden en el que se hayan escrito los comando en el script, 
aunque es posible definir un punto de inicio con el fin de construir un código con piezas reutilizables. Para ello, tenemos 
que definir un punto de inicio o "main". La mayora de los lenguajes de programación utilizan como punto de inicio de sus 
código fuente el método main. En python es posible utlizar esta forma de ejecución en python mediante la utilización de la 
variable __name__, que es una variable especial de python que define como se ejecuta el script. 

```
#!/usr/bin/env python3

if __name__ == "__main__":
    print('Holaaaa')

```

***IMPORTANTE***

El indentado es un tipo de notación secundaria utilizado para mejorar la legibilidad del código fuente, pero en python tiene 
una mayor importancia ya que define el flujo de ejecución del programa. Es decir, que define como el código es interpretado y 
ejecutado. 

Hagamos algo un poco más dificil!!!

```
#!/usr/bin/env python3

def my_function():
    for i in [0, 1, 2, 3]:
        print("Hola " + str(i))
    print("adios")

print("Bye")

if __name__ == "__main__":
    my_function()
```

El resultado de la ejecución de este programa será:

```
Bye
Hola 0
Hola 1
Hola 2
Hola 3
Adios
```

El inteprete de comando ha ejecutado los cómandos básicos como el print("Bye") y luego a comenzado la ejecución a través del 
método main llamando a la función. ¿Pero qué es una función?

**2.5 Funciones**

Las funciones nos permiten crear métodos reutilizables que pueden ser ejecutados multiples veces. Las funciones se definen 
utilizando la palabra reservada def seguido del nombre de la función y unos parentesis donde se incluyen los parámetros, 
finalizando con :. A continuación se introduce el código de la función utilizando el indentado 

```
#!/usr/bin/env python3

def my_function(valor):
    print(valor)

if __name__ == "__main__":
    my_function("Hola")
    my_function("Adios")

```

El resultado de la ejecución de este programa será:

```
Hola
Adios
```

**2.6 Variables (locales y globales)**

Las variables son contenedores que permiten almacenar información mediante un nombre univoco. La denominación de las variables debe realizarse en base a cuatro reglas básicas

* No pueden comenzar por un número --> 1nombre
* No pueden contener espacios --> variable prueba
* No pueden contener operadores (+, -, *, /, etc) ni el símbolo ? --> my_var?
* No pueden llamarse como la palabras reservadas (True, for, ...) --> True

Además es posible comprobar si una cadena de texto es un nombre válido para una varible de Python mediante la función :

```
'סְפִירוֹת'.isidentifier()
```

***Operaciones básicas con variables***

La asignación de las variables se realiza mediante el operador de asignación '='

```
mi_variable_1 = 23
mi_variable_2 = 'Nombre'

```
El acceso al valor de la variables que hemos asignado previamente se realiza mediante el llamada a la variable

```
mi_variable_1 = 23
print(mi_variable_1)
mi_variable_2 = 'Nombre'
a = mi_variable_2
print(a)
```
Aúnque si intentamos acceder al valor de una variable a la que se le ha asignado un valor previamente obtendremos un error en tiempo de ejecución:

```
>>> print(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>>
```
La asignación en python nos permite asignar el valor de múltiples variables mediante la misma operación. Este sistema de 
asignación múltiple es denominado como 'asignación desestructurada'. 

```
>>> a,b = 1, 2
>>> print(b)
2
>>>
```

Incluso es posible realizar la asignacón desestructurada con tipos de datos diferentes

```
>>> a, b = 1, 'prueba'
>>> print(a)
1
>>> print(b)
prueba
>>>
```

o asignadoles el mismo valor a ambas variables

```
>>> a, b = 1
>>> print(b)
1
>>> 

```

**2.7 Clases y objetos**

Los objetos son los elementos básicos de cualquier lenguaje de Programación Orientado a Objetos (POO). En el caso de python cualquier cosa es un objeto, eso quiere decir que nuestras variables son objetos. 

Pero, ¿Qué es un objeto?

Un objeto puede definirse como un ente abstracto utilizado en POO que permite definir los diferentes componentes de un programa. Los objetos se define en base a una clase que permite la definición de un estructura y un conjunto de funciones o métodos que pueden aplicarse una vez que se ha creado el objeto. 

¿Los objetos se crean?

Si, se deben crear de manera explícita, pero hay algunas excepciones. Los llamados "tipos básicos" crean automaticamente un objeto al realizarse la asignación de su valor:

```
>>> a = 1
>>> print(type(a))
<class 'int'>
>>> a = int(1)
>>> print(type(a))
<class 'int'>
>>> b = [1, 2, 3] #¿Qué es esto?
>>> print(type(b))
<class 'list'>
>>>

```

¿Cómo defino una clase?

Las clases se definen de forma similar a las funciones, pero dentro de si mismas contienen funciones y varibles (Objetos).

```
#!/usr/bin/env python3

class prueba:
  def __init__(self, a, b):
    self.__a = a 
    self.__b = b

  def get_a(self):
    return self.__a

  def get_b(self):
    return self.__b


p = prueba(1, 10)
print(p.get_a())

```

Pero .... ¿Qué es la función __init__ ?, ¿Qué es la variable self?. Todo esto lo veremos más adelante. 

**2.8 Tipos de datos básicos**

Los tipos de datos definen la clase que se ha utilizado para definir el objeto. Para conocer el tipo de un variable en python, se puede utilizar la función type(), que nos indica el tipo del objeto, es decir la clase utilizada para definir el objeto. 

```
>>> a = 1
>>> print(type(a))
<class 'int'>
>>> a = 'Prueba'
>>> print(type(a))
<class 'str'>
>>> 

```

Los tipos estándar en python se pueden clasificar en dos grupos dependiendo de si su valor puede cambiarse en tiempo de ejecución. 

* Mutable: su contenido (valor) puede cambiarse en tiempo de ejecución.
* Inmutable: su contenido (valor) no puede cambiarse en tiempo de ejecución. En caso de querer cambiar el valor, es necesario reasignar la variable (objeto).

Categoría |	Nombre | Descripción
------------ | ---------- | ------------
Números inmutables | int | entero
Números inmutables | long | entero largo
Números inmutables | float | coma flotante
Números inmutables | complex | complejo
Números inmutables | bool | booleano
Secuencias inmutables | str | cadena de caracteres
Secuencias inmutables | unicode | cadena de caracteres Unicode
Secuencias inmutables | tuple | tupla
Secuencias inmutables | xrange | rango inmutable
Secuencias mutables | list | lista
Secuencias mutables | range | rango mutable
Secuencias mutables | Mapas | dict(diccionario)
Conjuntos mutables | set | conjunto mutable
Conjuntos inmutables | frozenset | conjunto inmutable
------------ | ---------- | ------------

*** Números ***

Los tipos numéricos en Python se agrupan en tres categorías o número dependiendo de su tamaño y su representación: (1) enteros, (2) reales y (3) complejos. 

Clase	| Tipo | Descripción | Ejemplo
------------ | ---------- | ------------ | ------------ 
bool | Número entero	| Número entero binario (0, 1) | True es 1, False es 0
int	| Número entero	| Número entero con precisión fija | 21
long |	Números	entero | Número entero con overflow (Super grande) |	42L ó 456966786151987643L
float	| Números real | 	Coma flotante de doble precisión | 3.1415927
complex	| Números	complejo | Parte real y parte imaginaria j |(1.25 + 5j)
------------ | ---------- | ------------ | ------------ 

**** Boleanos ****

Los boleanos representan un entero de tipo binario que puede tomar dos tipos de valores (False = 0 y True = 1). Se define mediante la utilización de las palabras reservadas False y True. Este tipo de objetos se utilizan normalmente para la creación de variables de control de bucles o de variables de comprobación. 

```
>>> a = True
>>> print(type(a))
<class 'bool'>
>>> print(a)
True
>>> 

```

Se pueden convertir en enteros mediante la utilización del método creador de la clase de enteros "int". 


```
>>> a = int(True)
>>> print(type(a))
<class 'int'>
>>> print(a)
1
>>> 
```

**** Enteros ****

Los enteros representan valores enteros con signo que no tienen decimales, es decir pueden utilizarse para almacenar valores positivos y negativos (además del cero). En Python se pueden representar números enteros de dos tipos: (1) el tipo int (para enteros de -2.147.483.648 a 2.147.483.647 en plataformas de 32 bits y -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807 en plataformas de 64 bits); y (2) el tipo long (para enteros de cualquier precisión) que sólo está disponible en python 2.7.

Las variables de tipo entero se puede definir de manera directa asignando un número entero a una variable o bien utilizando la clase "int". 

```
>>> a = 2
>>> b = int(2)
>>> print(type(a))
<class 'int'>
>>> print(type(b))
<class 'int'>
>>> 
```

El long (entero largo) se puede definir de manera directa asignando un número entero con la letra mayuscula L al final o utilizando la clase "long". 


```
>>> a = 2L
>>> b = long(24)
>>> print(type(a))
<class 'long'>
>>> print(type(b))
<class 'long'>
>>> 
```

**** Reales ****

Los reales representan números reales con signo. La mayoría de los lenguajes de programación permiten la definición de número reales mediante dos tipos de datos (float y double), pero en el caso de python los números decimales se almacenan siempre con doble precisión. En python, los números reales se escriben separando la parte entera de la decimal mediante un punto. Al igual que los enteros, las variables de tipo real pueden ser definidas de manera directa asignando un número decimal o utilizando la clase float. 

```
>>> a = 2.4
>>> b = long(.65)
>>> print(type(a))
<class 'float'>
>>> print(type(b))
<class 'float'>
>>> 
```

**** Complejos ****

Los complejos representan números reales con parte imaginaria. Python, es uno de los pocos lenguajes que posee un tipo de dato de tipo complejo, principalmente para utilizarnos en aplicaciones de caracter científico. Los números complejos se pueden definir mediante un suma entre la parte real y la parte imaginario se la siguiente manera. 


```
>>> a = 2.4 + 23.4j
>>> print(type(a))
<class 'complex'>
>>> 
```

**** Operaciones entre números ****

Todos los operadores matemáticos pueden ser aplicados entre número de diferente tipo siendo como resultado un nuevo número cuyo tipo se corresponde con el de mayor tipo de los implicados en la operación matemática, siendo la jerarquía de tipos la siguiente:

int << long << float << complex

Las operaciones mátemáticas disponibles en python son las siguientes:

* Suma: a + b
* Resta: a - b
* Multiplicación: a * b
* División: a / b 
* Cociente de la división: a // b 
* Resto de la división: a % b
* Potencia: a ** b

*** Cadenas de caracteres ***

*** Tuplas ***

*** Listas ***

*** Diccionarios ***
