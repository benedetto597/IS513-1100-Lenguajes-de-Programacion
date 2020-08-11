PAC II 2020 - LLP 1100
@author ferlox
@date 2020/07/22
@version 0.1

LISP
======

* Es un lenduaje de proposito general.
* Integers, Ratios, Comples Numbers, String, Arrays, Vectors, Has Table, Funciones, Strams.
* Expresiones-S se define, recursivamente, como:
    * Un tipo de dato simple, el cual se llama "atomo".
        * Un atomo corresponde con: numero, lista, cadenas de caracteres y simbolos 
    * Una lista de expresiones-S dodne una expresion-S podria ser una lista de expresiones-S, que a su vez podria ser lista, y se pueden obtener expresiones anidadas de cualquier nivel de profundidad

Expresiones-S (S-expression)
----------

* Expresion Simbolica: ess una notacion de forma de texto usada en la representacion de extructuras de arbol, esta basada en lista anidadas, en donde cada sublista es un subarbol. Las expresiones-S se usan en la familia de lenguajes de programacions LISP. Su representacion es mediante secuencias de cadenas de caracter, delimitadas por parentesis, y separadas por espacios: (= 4 (+2 2)).
En c este ejemplo seria: 4 == 2 + 2.

Common Lisp
--------

* https://lisp-lang.org/
* Requiere el uso de notacion pre-fija.
* En consola lo ejecutaremos usando un programa SBCL (sudo aptitude).
    * http://www.sbcl.org
    * http://www.sbcl.org/manual

* Ejemplos:
    #
        (+ 1 2)
        (+ 1 (+ 1 1))
        (* (+1 2) (-3 4)) ; Obserce que existen espacios que sepparan cada elemento de la instruccion
        (+ (+ 3 4) (+ (+ 4 5) 6))
        (+ 3 4 5 6) ;La funcion de adicion puede tomar mas de un parametro 
        (defun funcion (x y) (+ x y 5)) ;La definicion de una funcion.
        (funcion 1 2) ;La ejecucion de una funcion.
        (let ((x 10)) x)
        (let ((y 10)) (- y 10))
        (list 4 5 6)
    #

* Para ejecutar un script:
    #
     $ sbcl --script programa.lisp
    #
* Tome en cuenta que:
    * SET que puede establecer el valor de simbolos.
    * SETQ puede establecer el valor de variables 
    * SETF es un macro, poseen la capacidad de definir varios elementos: simbolos, variables, elementos de un arreglo, instancias, etc.
* Ejemplo de peticion de datos:
    #
     (write (+ 1 (read)))
    #
* Ejemplo (sin imprimir resultado):
    #
        (defvar *unaVariableCualquiera*)
        (serf *unaVariableCualquiera* 42.1)
        (* 2.1 *unaVariableCualquiera*)
    #
* Ejemplo de funcion y ejecucion de funcion:
    #
        ; Se defune una funcion
        (defun square (x) (* x x))

        ; Se usa la funcion 
        (Write (square 3))
    #
* Ejercicio de un programa que imprime mensajes en pantalla y recive datos de usuario.
* Ejercicio de factorial que imprime el resultado 