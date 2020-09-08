<!-- Encabezado -->
## IS513 Lenguajes de Programación Sección 1100
### Proyecto Final
### Integrantes
| Nombre | Número de cuenta |
| :----------- | :------------- | 
| Edgar Josué Benedetto Godoy | 20171033802 | 
| Bryan Josué Gonzáles Salgado | 20141001209 | 
| David Alejandro Jácome Jácome | 20161001299 | 
| Luis Alejandro Samuel Banegas | 20161001299 |

___
___

<!-- Titulo -->
# Documentación del Proyecto Final IS-513 LLP

<!-- Aspectos generales -->
## Generales
* Para la impresón en consola con colores se implemetntan metodos de códigos **ANSI** los cuales no necesitan una previa instalación, se usa en la impresión de los encabezados, tabla de símbolos, códgio del programa leído, control de errores y para las impresiones en JavaScript; algunos estilos no están soportados por todas las consolas.
![Tabla ANSI](https://drive.google.com/uc?export=view&id=1QiDFa9xF9hOoBo-oggjlnA5eQ2A1Voqy)

* Para los manejos de errores se hace uso de **try** and catch de Python que en vez de catch es **except** cumpliendo la misma función.
* Para el análisis léxico **no** se hará uso de generadores de análisis léxicos como *Plex* porque requiere de una versión antigua de Python para funcionar, para lo cual el análisis léxico es trabajado en su totalidad con Autómata Finito.
* Para el análisis semántico / sintáctico se usa **Lark**, aprovechando su lado sintáctico para 3 lengujes de programación distintos, y su parte semántica sólo para JavaScript.
* Se hace uso de **Tabulate** para la impresión de la tabla de símbolos y la impresión del encabezado. El resultado en consola del encabezado es la siguiente:
![Encabezado con Tabulate](https://drive.google.com/uc?export=view&id=19M3oOI9m_5hgdendKhghLgcZ313plcwB)

* En la lectura del archivo a **Reconocer** se prueba primero con la grámatica de Ruby luego con la grámatica de Bash, sin importar la extensión del archivo.
* El vídeo que se debe adjuntar es grabado con **OBS (Open Broadcaster Software)** dado que al culminar la grabación codifica directamente en MP4/H. 264.
* La documentación del generador de análisis sintáctico / semántico *Lark* junto con algunos ejemplos: 
[https://lark-parser.readthedocs.io/en/latest/](https://lark-parser.readthedocs.io/en/latest/ "Documentación de Lark")
___

<!-- Parte de Interpretación -->
## Interpretación
En la parte de la interpretación se debe simular la acción intermedia que sucede al momento de traducir un lenguaje de programación a un lenguaje máquina, en este caso sólo es con el lenguaje de programación JavaScript el cual será sometido a 3 análisis, el análisis Léxico, Sintáctico y Semántico, donde los últimos 2 están unidos, dado que es común encontrarlos relacionados porque es optimo además de detectar el orden, detectar también cual funcionalidad cumple cada instrucción. 

<!-- Análisis Léxico de la parte de Interpretación -->
### Análisis Léxico
 La forma en la que se divide la tabla de símbolos es la siguiente:

![Tabla de símbolos](https://drive.google.com/uc?export=view&id=1PSW4R9ncRHMwR7VE-L-lJieZ6IlvOSqi)
* Se aislan carácteres especiales para el manejo de lo que pueda venir después, haciendo uso de los estados.
    * Algunos carácteres no necesitan un control de estado estricto por la variedad de carácteres que puede contener eg. Cadenas simples o dobles.
* Al momento de realizar la **lectura carácter por carácter** se recuerda o guarda la cantidad de los mismos necesarias para determinar si el lexema leído es aceptado por el lenguaje y luego ese lexema lo subdividimos para poder presentarlo en la tabla de símbolos.
* Para el control de rangos de carácteres se hace uso de la tabla *ASCII*.
* Dado que la lectura se realiza carácter por carácter, al momento de llegar a un carácter que permita determinar si el **lexema leído** es aceptado o no por el lenguaje se hace un regreso para poder realizar la correcta lectura del lexema que sigue a continuación.
* Se usan 2 meta estados, que refieren al token cuando está formado y cuando el token está en formación, derivando en estados individuales para cada token.
* Existe un diccionario de **palabras reservadas** y carácteres aceptados por el lenguaje JavaScript con su respectivo tipo para la realización de la tabla de símbolos.

### Análisis Sintáctico / Semántico
* La grámatica no puede contener reglas que no tengan elementos terminales.
* En la grámatica no se puede ignorar una regla establecida.
* Se hace un guardado temporal de todo dado que progrsivamente se debe ejecutar tanto cuando está encapsulado en una función.
* Las **funciones** son tratadas al igual que las variables y se guardan con todo lo que las compone.
* Las **funciones** contenidas en el código intrpretado son ejecutadas por una función en python llamada *run* la cual es inicializada en *runFunction* donde se obtienen las sentencias contenidas en esa función junto con sus paramentros y demás argumentos para progresivamente ejecutarlas. 
* Para hacer uso del árbol generado en un formato iterable por *Lark* se designa en *False* la forma línea por línea que utiliza *Lark* para devolver a los visitados, o hijos en el árbol.
> **@v_args(inline=False)** 
* Del árbol que devuelve *Lark* se obtienen sólo lo que es de interes, es decir, sólo las partes del mismo que corresponden al código que se está leyendo, para poder guardarlo en una variable temporal, para posteriormente determinar si es un argumento, función o variable, haciendo uso de la función llamada **cleanTree**.
* Cada sentencia, funcion y variable es almacenada en objetos diccionario, los cuales tienen por llaves el nombre de la sentencia, función o variable a la que corresponde el lexema asignado como valor de esa llave.
* Para reconocer el llamado de una función se hace uso de **showFunction** donde se usa *cleanTree* para obtener los parametros del llamado de la función, al estar límitados por 0, 1 o 2 parametros sólo se analiza la cantidad de elementos obtenidos del árbol generado por *Lark*.

## Reconocimiento
* Al no poder poner la extensión del archivo a reconocer dado que existe la posibilidad de que un archivo con extención *cualquiera* puede contener código de bash o ruby, se hace la lectura de reconocimiento probando con ambas grámaticas, si alguna hace **match** en su totalidad implica que se reconoce el contenido de ese archivo con alguno de los lenguajes disponibles, en este caso sólo son 2:
    1. Bash.
    2. Ruby.
* Límitado a sólo el reconocimiento no se asigna función a ninguna de las reglas dado que no tiene un tratamiento semántico.
* Las reglas grámaticales se leen línea a línea de forma predeterminada, para ignorar comentarios basta con poner la expresión regular del primer elemento que contiene junto con la representación de todos los carácteres Repetidos 0 o más veces, en *Ruby* es así:
> **%ignore /[\#].+/** 
* En la grámatica de Bash se incluye el caso en el que se encuentre en una recursión infinita en la que la única forma de deterla es haciendo uso de **Cntrl + C** y *exp* sginifica que puede contener cualquier expresión de las admitidas y todo sólo haciendo uso de la siguiente regla:  
>**" for " " (( " " ; " " ; " " )) " " ; "? " do " exp+ ";"?  "done"**
* Las variables en *Bash* pueden llevar un signo de dolar *$* que representa la obtención del valor de esa variable, dado que en cualquer momento se puede acceder al valor de una variable y no se está análizando su lado semántico, puede ser usado el *$* en una variable sin tenerla declarada previamente, lo cual no representa un error sintáctico, en cambio si uno semántico.
* En *Bash*, el uso multiple de cadenas y variables en las impresiones se puede englobar con una regla que contenga o sólo una cadena o alguna variable con una o ninguna cadena donde el caso de haber más de una variable en la misma línea es tratado con esta regla.
> **string | var string***
* Los comentarios de una línea en ambos lenguajes son ignorados haciendo uso de la misma regla, los comentarios de multiples líneas de *Ruby* son englobados en una regla.

___
