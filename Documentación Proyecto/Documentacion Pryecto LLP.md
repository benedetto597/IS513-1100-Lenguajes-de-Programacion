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
* Las **funciones** son tratadas al igual que las variables y se guardan con todo lo que las compone.
* Para hacer uso del árbol generado en un formato iterable por *Lark* se designa en *False* la forma línea por línea que utiliza *Lark* para devolver a los visitados, o hijos en el árbol.
> **@v_args(inline=False)** 
* Del árbol que devuelve *Lark* se obtienen sólo lo que es de interes, es decir, sólo las partes del mismo que corresponden al código que se está leyendo, para poder guardarlo en una variable temporal, para posteriormente determinar si es un argumento, función o variable, haciendo uso de la función llamada **cleanTree**.
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
* 
___

![Elementos historicos importantes](https://drive.google.com/uc?export=view&id=1pSRlAMBHa_Dg5ypdULDKYxq3yBassiyl)

Los lenguajes de programación tienen sus orígenes en la década de 1950 con la creación de FORTRAN, **lenguaje algorítmico** diseñado por un equipo en IBM dirigido por Jhon Bakus. Progresivamente en esa misma década se fueron creando lenguajes para distintas orientaciones como COBOL, el cual está **orientado a los negocios** o ya en la década siguiente llego Basic, el cual es **orientado a la educación** y así a lo largo de los años se crearón lenguajes capaces de realizar tareas particulares o especificas, progresivamente se fue optimizando la forma en la que el lenguaje era capaz de realizar dichas tareas especificas. En el siglo 21 se empezó a desvelar una forma de programar y orientar los lenguajes de programación que haría revolución en todo aquello que ya conocíamos, tan importante y secreto era que en el auge de Apple el cofundador y presidente ejecutivo de Apple Steve Jobs era invitado a reuniones secretas en las que se discutía sobre la **programación orientada a objetos**, lo cual puede llegar a ser inimaginable hoy en día dado que la programación orientada a objetos es hasta impartida en las universidades, el nivel de abstracción que se puede conseguir con dicho paradigma es muy extenso y dado que nuestros límites con la programación recaen en gran medida en la capacidad de abstraer elementos de la realidad y llevarlos a código ejecutable, la programación orientada a objetos llego a resolver una problemática que desencadeno aún más la revolución informática de la actualidad. Línea del tiempo de la implementación de cada lenguaje de programación:

![Implementación de cada lenguaje](https://drive.google.com/uc?export=view&id=1V0IJo_oDKQy-1Bx46gPEtWjkKTuqVm4Y)
![Implementación de cada lenguaje](https://drive.google.com/uc?export=view&id=16NQlG_9sU72RdCOIo18sF7Qhk7S33EHF)
![Implementación de cada lenguaje](https://drive.google.com/uc?export=view&id=1vWxchwFspZ5PYkLpsNpge9bp8LnEwxWg)

## Clasificación de los lenguajes de programación 
### Lenguajes algorítmicos
Los lenguajes algorítmicos fueron diseñados para **expresar cálculos matemáticos** o simbólicos. Fueron los primeros idiomas de **alto nivel**, es decir que son capaces de aprovechar al máximo los componentes físicos del computador, algunos de ellos son:
* FORTRAN
    * Primer lenguaje algorítmico, desarrollado por IBM.
* ALGOL 
    * Introdujo la **estructura de bloques** donde se pueden contener datos e instrucciones.
* CECEO 
    * Uso de función aplicada a datos.
* C 
    * Comparte con lenguaje ensamblador el poder de explotar todas las características de la arquitectura interna de una computadora.

### Lenguajes orientados a los negocios
* COBOL
    *  Introdujo la **estructura de datos de registro** para tales tareas.
* SQL 
    * Especifica la organización de bases de datos.

### Lenguajes orientadas a la educación
* BASIC
    * Tiene estructuras de datos simples.
* Logo
    * Tenía una sintaxis más convencional que *LISP* y presentaba "Gráficos de tortuga"
* Hypertalk
    * Poseía características de lenguajes orientados a objetos usando una sintaxis simple en ingles.
* Pascal
    * enfatizó el uso ordenado de estructuras de control condicional y en bucle sin sentencias **GOTO**.
    > GOTO: Instrucción de salto incondicional. -Peter Bishop

### Lenguajes orientados a objetos
Se utilizan para la **gestión de programas grandes**, dado que tienen 4 pilares que los hacen tan poderosos:

| Abstracción | Encapsulamiento | Herencia | Polimorfismo |
| :----------- | :------------- | :------ | :----------- |
| Es un proceso de interpretación, análisis y diseño de deconstruir algo que pertenece a la realidad conocida  y enfocarse en las características importantes de una situación u objeto filtrando o ignorando todas las particularidades no esenciales. | Es la agrupación de los componentes abstraídos donde se necesita reconocer cuales se aíslan y cuales no. | Es la obtención de características a partir de una entidad general | Es la propiedad por la que es posible enviar mensajes sintácticamente iguales a objetos de tipos distintos. 

Entre los lenguajes de programación orientados a objetos están: 
* C ++
    * Agrega objetos mientras preserva la eficiencia de los programas de C.
* Ada
    * No estaba orientado a objetos en sus inicios si no hasta Ada 95.
* Java
    * Agregar capacidades interactivas a Internet a través de “applets” web.
* Visual Basic
    * Amplia las capacidades de BASIC agregando objetos y programación **dirigida por eventos**.
    
### Lenguajes de formateo de documentos
Son los encargados de especificar la organización del **texto impreso y los gráficos**.
* Texas
    * Incorpora comandos de formato de texto sin formato en un documento.
* PostScript 
    * Hace uso de postfix, en la que el nombre de una operación sigue sus argumentos.
* SGML
    * Lenguaje de marcado generalizado estándar.

### Lenguajes de visualización de la World Wide Web
* HTML 
    * Lenguaje de marcado de hipertexto
* XML
    * Lenguaje de marcado extensible

### Lenguajes de script 
También conocidos como pequeños lenguajes, son lenguajes que están destinados a **resolver pequeños problemas**, suelen utilizarse para escribir utilidades del sistema operativo como: 
* JavaScript 
    * Adaptado al desarrollo web principalmente del *lado del cliente*.
* PHP
    * Adaptado al desarrollo web principalmente del *lado del servidor*.
* PERL 
    * Lenguaje práctico de extracción e informes 

### Lenguajes Conceptuales
Son lenguajes que no se orientan o desarrollan por un propósito especifico sino que **siguen un concepto** en particular, tienen como característica ser **multi-paradigma** y suelen ser de muy **alto nivel**. 
* PROLOG
    * Lenguaje de programación lógico e interpretado
* LISP
    * Se construye aplicando funciones a argumentos.

## Compiladores 
La compilación hace uso de programas llamados compiladores, los que se encargan de **traducir** lenguajes de programación de alto nivel a **código máquina**. La interpretación se utiliza para sistemas más pequeños que en los traducidos. Aquí es donde entran los **analizadores léxicos**, **sintácticos** y **semánticos**, los cuales son los encargados de la construcción del lenguaje a pequeña escala como el reconocimiento de símbolos admitidos por el lenguaje, las construcción a gran escala como el reconocimiento de expresiones, declaraciones, unidades de programa y por último el reconocimiento de el significado de el conjunto reconocido anteriormente, dichos analizadores funcionan como procesos separados por simplicidad, eficiencia y portabilidad, dado que cada uno de los análisis realiza tareas distintas con lo que se le da de entrada y consecuentemente la salida de uno es la entrada de otro, en el orden de analizadores mencionado.

### Analizador Léxico
Reconocedor de patrones, el cual se encarga de encontrar sub-cadenas en una cadena de caracteres determinada, El analizador léxico recoge personajes en **agrupaciones lógicas** y asigna códigos internos a las agrupaciones, estas agrupaciones lógicas se denominan lexemas. En esencia es un programa que identifica **lexemas**, Los lexemas incluyen: 

* Literales "#"
* Operadores
* Palabras reservadas

Los lenguajes de programación son un conjunto de lexemas y no de caracteres. Los lexemas se dividen:

* Nombres de variables
* Nombres de métodos
* Nombres de clases

El grupo que contiene estos nombres se conoce como identificador de usuario. Cada grupo de lexemas está representado por un nombre o token, el cual representa a dicho grupo. El **token** se define como una categoría de cada grupo de lexemas.
Distintos enfoques para la construcción de los analizadores léxicos orientan al uso de **diagramas de estados**, se utilizan para representar maquinas de estados las cuales especifican la secuencia de estados por las que pasa un objeto a lo largo de su vida en respuesta a evento, donde están los de uso general, los cuales se definen de la siguiente manera: 

Ejemplo de diagrama de estados de una llamada telefónica.

![Diagrama de estados General](https://drive.google.com/uc?export=view&id=1Gco--TgqDIGv23oVz6_6HSnpHUd0gkEy)


1. Estado Inicial: Estado por el cual empieza el diagrama de estados.
2. Estado: Situación en la que se satisface una condición particular.
3. Transición: Es una relación entre dos estados que indica que un objeto que esté en el primer estado realizará ciertas acciones y entrará en el segundo estado cuando ocurra un evento especificado y se satisfagan unas condiciones especificadas.
4. Estado Final: Es donde se terminan las transiciones dado que se consigue un estado de aceptación.

El uso de los diagramas de estado en los compiladores ayuda a la realización de un mapa de todos los caracteres que pueden ser aceptados por el lenguaje. Para lo cual se hace uso de los **autómatas** que utilizan estados y transiciones entre estados en respuesta a las entradas, en donde su concepto radica en leer cada elemento carácter por carácter donde se hace un mapa completo de todos los caracteres, para poder entenderlos en el analizador léxico, luego el analizador sintáctico se hace con **árboles de parseo**, usando conceptos como el diagrama de estados para entender el resto de elementos semánticos, los cuales tienen distintas funcionalidades como ser:

1. Software para diseñar y probar el comportamiento de circuitos digitales.
2. El “analizador léxico” de un compilador típico, es decir, el componente del compilador que separa el texto de entrada en unidades lógicas, tal como identificadores, palabras clave y signos de puntuación.
3. Software para explorar cuerpos de texto largos, como colecciones de páginas web, o para determinar el número de apariciones de palabras, frases u otros patrones.
4. Software para verificar sistemas de todo tipo que tengan un número finito de estados diferentes, tales como protocolos de comunicaciones o protocolos para el intercambio seguro de información.

El **autómata finito** o maquina de estado finito puede ser **determinista** donde solo puede haber para una lectura un único estado o **no determinista** donde puede haber dos estados diferentes para la misma lectura, es decir la diferencia entre estos autómatas es que solo porque existan dos caminos o transiciones de un estado, no significa que lo convierte en no determinista, sino que si de un estado se pudiese concretar una transición haciendo uso del mismo carácter, en ese caso si sería un no determinista, pero al pasar de un estado a otro con distintos caracteres llegando a un solo estado final, queda como determinista. El autómata finito sirve para definir lenguajes, pueden representarse con un diagrama de estados ya que se puede ver como un **grafo direccionado**: 

Ejemplo de una Maquina de estados finitos que acepta un solo estado final.

![Maquina de estado finito](https://drive.google.com/uc?export=view&id=14DUwl3snuSfuPZyjHSjWKjRgSjLztEGr)

Definición formal del Autómata Finito:
Formalmente, un autómata finito es una *quintupla* (Q, Σ, q0, δ, F) donde: 

* *Q* es un conjunto finito de estados.
* *Σ* es un alfabeto finito.
* *q0* es el estado inicial.
* *δ* es una función de transición.
* *F* es un conjunto de estados finales o de aceptación.

### Analizador Sintáctico
Es el que genera la sintaxis, tiene la forma del lenguaje. La salida del analizador léxico es la entrada del analizador sintáctico, y la salida del analizador sintáctico es la entrada del analizador semántico ya que el analizador sintáctico es al que le interesa saber el orden de los componentes. 
No es papel del analizador sintáctico entender las instrucciones, sino solo si el orden es correcto.
En el analizador sintáctico se salta por cada lexema para generar un árbol de parseo, donde con esa estructura se arma la forma en la que reconoce cada token el analizador. Se suelen hacer más de una vuelta al árbol por ejemplo la primera para encontrar errores, la segunda para generar el árbol de parseo y una tercera para definir la tabla de símbolos, etc. Para hacer una sintaxis se necesita hacer una gramática y la capacidad de poder realizar este análisis es también gracias a las **gramáticas independientes de contexto** los cuales utilizan una notación natural recursiva del lenguaje la cual es un conjunto finito de producciones o reglas, siendo conformado por símbolos o por variables, denominado también en ocasiones *símbolos no terminales* o categorías sintácticas, una de las variables representa el lenguaje que se está definiendo; se denomina símbolo inicial. Otras variables representan las clases auxiliares de cadenas que se emplean para definir el lenguaje del símbolo inicial, que forman las cadenas del lenguaje que se está definiendo. La gramática es el método formal para describir una sintaxis; Los lenguajes son identificados a través de nuestros lenguajes de programación por una gramática que la definimos gracias a la gramática libre contexto o  la forma Backus-Naur que son exactamente lo mismo. 
* *Gramática libre de contexto*: Ayuda a definir la posición de los elementos de los lenguajes de programación.
* *Gramática regular*: Ayuda a definir los tokens.

El **árbol de parseo** es el resultado que proporciona el analizador sintáctico de un lenguaje de programación y es la forma en la que se suele representar la estructura de los programas, siendo está estructura de datos una colecciones de nodos, que mantienen una relación padre-hijo, donde existe un nodo, el nodo raíz, que no tiene padre; este nodo aparece en la parte superior del árbol; los nodos sin hijos se denominan hojas. Al concatenar las hojas del árbol de izquierda a derecha(dependiendo de su construcción) se obtienen cadenas denominadas resultados del árbol. 

### Analizador Semántico
Recibe el resultado del análisis sintáctico con lo cual ya se puede asignar un significado a todos los componentes reconocidos correctamente en los análisis previos. Es en esta etapa donde se utiliza como entrada el árbol sintáctico detectado por el análisis sintáctico para comprobar restricciones de tipo y otras limitaciones semánticas y preparar la generación de código.En **compiladores de un solo paso**, las llamadas a las rutinas semánticas se realizan directamente desde el analizador sintáctico y son dichas rutinas las que llaman al generador de código, las cuales hacen uso de la **pila semántica** que contiene la información semántica asociada a los operandos y a veces a los operadores en forma de registro semántico. El instrumento más utilizado para conseguirlo es la gramática de atributos.

En compiladores de dos o más pasos, el análisis semántico se realiza independientemente de la generación de código, pasándose información a través de un archivo intermedio, que normalmente contiene información sobre el árbol sintáctico en forma lineal.

Un componente importante del análisis semántico es la **verificación de tipos**. Aquí, el compilador verifica si cada operador tiene operandos permitidos por la especificación del lenguaje fuente. Por ejemplo, las definiciones de muchos lenguajes de programación requieren que el compilador indique un error cada vez que se use un número real como índice de una matriz. Sin embargo, la especificación del lenguaje puede imponer restricciones a los operandos, por ejemplo, cuando un operador aritmético binario se aplica a un número entero y a un número real, revisa que los arreglos tengan definido el tamaño correcto.

___
<!-- Conclusiones -->
## Conclusiones

1. Los lenguajes de programación son un área de estudio cuanto menos apasionante y de interés masivo, teniendo en cuenta las estadísticas relacionadas con salarios en dicho rubro, es fácil de identificar que más de uno concreta su acercamiento a carreras relacionadas con la idea de simplemente generar una estabilidad económica, lo cual no es un acercamiento erróneo pero si quizá un acercamiento desaprovechado, dado que el conjunto de conocimientos que se necesitan adquirir para llegar a profesionalizarse en este rubro incita a un despliegue de creatividad e innovación, con lo que también es normal encontrar genios en el área, dando como resultado un rubro enriquecido por todas las partes que lo componen y hacen de este un apasionante camino a recorrer.

2. La historia de los lenguajes de programación sigue siendo un relato corto, dado que aún no se concreta ni un siglo desde su primer aparecimiento, pero no obstante la velocidad de su avance no es equivalente a su tiempo en los libros de historia; la revolución informática se ha desencadenado con una aceleración creciente casi exponencial, donde el software ha liderado con sistemas embebidos, Inteligencia artificial, etc. Dando como resultado una variada colección de programas y aplicaciones capaces de resolver problemas tan complejos como simples; también puede verse este avance en su apartado físico, como con la **ley de Moore** que expresa que: 
> Aproximadamente cada dos años se duplica el número de transistores en un microprocesador. - Moore, Gordon E. 

3. La variedad de lenguajes de programación que existen en la actualidad permiten al programador escoger de forma adecuada la opción más optima para la tarea a realizar, dado que se han desarrollado lenguajes de programación de objetivo especifico  como Logo para niños, Verilog y VHSIC, R y S para estadísticas, Mata para programación matricial, Mathematica y Maxima para matemáticas, fórmulas de hojas de cálculo y macros, SQL para consultas a bases de datos relacionales, Yacc para crear parseadores, expresiones regulares para crear análisis léxico, Generic Eclipse Modeling System para crear lenguajes con el objetivo de diagramar, Csound un lenguaje para síntesis digital, y los lenguajes de entrada de GraphViz y GrGen, paquetes de software usados para graficar y reescribir gráficas. Otros lenguajes de propósito general como C o Java son a los que lo largo de los años se han optimizado en el apartado de su compilación, por lo tanto la mayoría de los problemas que se puedan presentar en la actualidad pueden cubrirse con un lenguaje de propósito general o sino con alguno de dominio especifico.

4. La tarea realizada por el compilador representa una parte fundamental de que en la actualidad el trabajo de ejecutar un programa resulte tan sencillo y en muchas ocasiones casi inmediato, por lo tanto es importante conocer la forma en la que se compone cada una de sus partes, la forma en la que desestructura y estructura el código de entrada; teniendo en cuenta que dichos componentes pueden estar integrados o por separado, comúnmente el análisis léxico está separado del sintáctico por la optimización de recursos dado que la forma en la que operan los mismos datos es completamente distinta.

5. Las estructuras de datos fundamentales, como pilas y árboles son aprovechados al máximo en el proceso que ejecutan los compiladores, dado que son estructuras extremadamente flexibles, en especial la estructura de los árboles que desde sus inicios es utilizada para el pareseo de lenguajes. Por lo tanto el conocimiento previo sobre estructuras de control y estructuras de datos es un requisito necesario para adentrarse en los lenguajes de programación.

___

## Bibliografía

* Robert W. Sebesta, University of Colorado at Colorado Springs "Conceptos de Lenguajes de Programación, 10ma Edición".
* John E. Hopcroft, Rajeev Motwani, Jeffrey D. Ullman. "Introducción a la computación, lenguajes y teoría de los autómatas 2da Edición".
* Michael L. Scott " Programming Language Pragmatics 2nd  Edition".
* Wagner, Ferdinand; Schmuki, Ruedi; Wagner, Thomas; Wolstenholme, Peter "Modeling Software with Finite State Machines: A Practical Approach 1th Edition".
* Dick Grune, Kees van Reeuwijk, Henri E. Bal, Ceriel J.H. Jacobs, Koen Langendoen"Modern Compiler Design 2nd Edition".
___
___








