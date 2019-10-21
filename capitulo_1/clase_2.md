![WideImg](https://fictizia.com/img/github/Fictizia-plan-estudios-github.jpg)

# [→ Máster en Big Data y Machine Learning](https://fictizia.com/formacion/master-big-data)
### Big Data, Machine Learning, Tensor Flow, Data Science, Data Analytics, Arquitecturas Big Data, Plataformas Big Data

## Capítulo 1 - Clase 02

En esta segunda clase del capítulo 1 se describirán como construir nuestros primeros programas en python con el fin de 
poder realizar los diferentes trabajos del máster. 

### 2.1 Creando mis primeros programas en python

Python es un lenguaje de programación en scripting. Es un lenguje interpretado, orientado a objetos con tipado dinámico, 
que  permite el desarrollo de algoritmos sencillos basados en un scripting, así como algoritmos complejos desarrollados 
con múltiples clases. 

**Instalación**

Instalamos [python 3.7]()


**Elementos básicos: La consola**

Python puede ejecutar mediante scripts desarrollados en uno o varios ficheros que interactuan entre sí o directamente en 
el terminal del sistema operativo. Actualmente python ofrece dos versión

* Python 2.7 que puede invocarse mediante el comando python
* Python 3.6 o 3.7 que puede invocarse mediante el comando python3. Esta será nuestra elección para la ejecución de los diferentes scripts que desarrollaremos en el máster. 

**Elementos básicos: La versión de python**

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

**Elementos básicos: Jugueteando con la consola**

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

**Creando mi primer programa python**

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

**Funciones**

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

**Variables (locales y globales)**

Las variables son contenedores que permiten almacenar información que es construida a partir de tipos de datos. Los tipos 
de datos estándar disponibles por defecto en python, como los tipos numéricos, secuencias, mapas y conjuntos usados para 
agrupar otros valores

***Tipos de datos***

Los tipos de datos estándar se pueden clasificar en dos grupos:

- Mutable: su contenido (valor) puede cambiarse en tiempo de ejecución.
- Inmutable: su contenido (valor) no puede cambiarse en tiempo de ejecución.

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
