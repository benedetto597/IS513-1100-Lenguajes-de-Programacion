# -*- coding: utf-8 -*-
"""
    ! Grámatica de los lenguajes de programación JavaScript, Ruby y Bash
    * Grámatica de JavaScript incluye funciones para la implementación semántica.
    * Grámatica de Bash y Ruby unicamente para reconocimmiento (sin semántica).
    ? Comentarios de multiples líneas reconocidos e ignorados.
    ? Grámaticas libres de ambiguedad.
    ? Reglas adicionales o no funcionales comentadas. 
    @author Edgar Benedetto
    @author Bryan Gonzáles
    @author David Jácome
    @author Luis Banegas
    @date 2020/08/18
    @version 1.0
"""

import re 

grammarJS = """

        ?start: exp+

        //Definicion de sentenciaexpresión
        ?exp: "function" var "(" (var ","?)* ")" "{" sentence* "}" -> addfunction
            | var "("((var|number) ","?)* ")" ";"? -> showfunction
            | var "(" var operator number ")" ";"? -> getrecursive
            | "console" "." "log" "(" string "," exp ")" ";"   -> getcon
            | "for" "(" var "=" number ";" var operation (number|var)  ";"  var increment ")" "{" sentence* "}" -> getfor
            
        //Definicion de sentencia
        ?sentence: assign ";"?  
            | "for" "(" var "=" number ";" logicoperation  ";"  var increment ")" "{" sentence* "}" -> getfor
            | "return" (number) ";"? -> getreturn 
            | "return" (var) ";"? -> getreturntwo
            | "return" (string) ";"? -> getreturnthre
            //| "return" reserve ";"? -> getreserve
            //| var "=" reserve|string|number ";" -> getvar 
            | "return" var operator exp ";"?   -> getreturnfunction
            | "console" "." "error" "(" (var|number|string) ")" ";" -> getconsoleerror
            | "console" "." "log" "(" (number|string) ")" ";"   -> getconsole
            | "console" "." "log" "(" var ")" ";"   -> getconsolevar
            | "if" "(" var operation number ")" sentence ";"? -> getif 
            | "if" "(" (var|number) operation (number|var) ")" "{" sentence "}" -> ifelse
            | else  
            | "while" "(" logicoperation ")" init sentence* "}" -> getwhile
            | break ";" -> getcomant
            | true ";" 
            | false ";" 
            | null ";" 
            | "/*" content* "*/" -> coment
            //e| inicoment content*  -> coment
            //| "for" "(" var "=" arithmeticoperationatom ";" logicoperation ";" var iteration ")" "{" sentence "}" -> getfor

        //Definicion de inicio de sentencia else
        ?else: "else" init sentence "}"  -> getelse 

        //Definicion de inicio de bucle while
        ?init: "{"
            | ";"

        //Definicion de alto de instrucción
        ?break: "break"

        //Definicion de booleano y nulo
        ?true: var "=" "true" -> gettrue

        ?false: var "=" "false" -> getfalse

        ?null: var "=" "null" -> getnull

        //Definicion de iterables
        ?increment: /\+\+/
            | /\-\-/

        //Definicion de asignación de variable
        ?assign: var "=" string  -> getstring
            | var "=" number -> getnum

        //Definicion de operación lógica
        ?logicoperation: arithmeticoperationatom operation arithmeticoperationatom  
        //?showfun: var "("((var|number) ","?)* ")" -> showfunction

        //Definicion del atómo aritmetico
        ?arithmeticoperationatom: var 
            | number
            | "-" arithmeticoperationatom
          
        //Definicion de cadenas
        ?string: /"[^"]*"/
            |  /̈́'[^']*'/

        //Definicion de operadores
        ?operator:/\*/
                | /\+/
                | /\-/
                | /\//
        
        //Definicion de distintas operaciones
        ?operation: /\==/
                | /\</
                | /\>/
                | /\>\=/
                | /\<\=/
                | /\!\=/     

        //Definicion del contenido de un comentario
        ?content: /./
                
        //Definicion de un numero
        ?number: /\d+(\.\d+)?/

        //Definicion de una variable
        ?var: /[a-z][\w]*/

        //Ignorar comentarios de una línea, saltos de línea, espacios y tabulados
        %ignore /\s+/

        %ignore /[\/\/].*/

"""



grammarBash =  """
    //Axioma inicial
    ?start: exp+

    //definicion de una expresion
    ?exp: "echo" combination  ";"?
        | var "=" string ";"?
        | var "=" arithmeticoperation ";"?
        | "if" "[" "["? condition "]"? "]" ";"? "then" command ";"? "fi"
        | "if" "[" "["? condition "]"? "]" ";"? "then" command ";"? "else" command ";"? "fi"
        | "if" "[" "["? condition "]"? "]" ";"? "then" command ";"? ["elif" "[" "["? condition "]"? "]" ";"? "then" command ";"? ]* "else" command ";"? "fi"
        | "for" "((" ";" ";" "))" ";"? "do" exp+ ";"? "done"
        | "for" var "in" number+ ";"? "do" exp+ ";"? "done"
        | "for" var "in" stringoption+ ";"? "do" exp+ ";"? "done"
        | "for" var "in" var+ ";"? "do" exp+ ";"? "done"
        | "for" var "in" "{" arithmeticoperationatom "." "." arithmeticoperationatom "}" ";"? "do" exp+ ";"? "done"
        | "for" "((" ";" ";" "))" ";"? "do" exp+ ";"?  "done"
        | "for" "((" var "=" [number+|var] ";" var foroperation [number+|var] ";" var ["++" | "--"]"))" ";"? "do" exp+ ";"? "done"
        | "while" ":" ";"? "do" exp+ ";"? "done"
        | "while" "[" "["? condition "]"? "]" ";"? "do" exp+ actioncount? ";"? "done"
    
    //Definicion de iteración 
    ?actioncount: "((" var ["++"|"--"] "))"
        
    //Definicion de operaciones aritmeticas admitidas en el for
    ?foroperation: "<"
        | "<="
        | ">"
        | ">="

    //Definicion de opciones en forma de cadena para el bucle for
    ?stringoption: /[a-zA-Z]+/

    //Definir contenido de las sentencias
    ?command: "continue" 
        | "break" 
        | exp+

    //Definicion de combinacion de variables y cadenas
    ?combination: string
        | var string*
    

    //Definicion de operacion aritmetica
    ?arithmeticoperation: product
        | arithmeticoperation "+" product 
        | arithmeticoperation "-" product 
        | arithmeticoperation "%" product 

    //definicion de un atomo de operacion aritmetica
    ?product: arithmeticoperationatom
        | product "*" arithmeticoperationatom
        | product "/" arithmeticoperationatom   
        
    //Definir atomo aritmetico
    ?arithmeticoperationatom: var
        | number
        | "-" arithmeticoperationatom
        | "$((" arithmeticoperation "))"

    //Definir operacion logica
    ?logicoperation: arithmeticoperationatom "-ge" arithmeticoperationatom
        //lesserequal
        | arithmeticoperationatom "-le" arithmeticoperationatom 
        //Greater
        | arithmeticoperationatom "-gt" arithmeticoperationatom 
        //Lesser
        | arithmeticoperationatom "-lt" arithmeticoperationatom 
          
    //Definir comparación igual y distinta
    ?comparisonoperation: arithmeticoperationatom "-eq" arithmeticoperation 
        | arithmeticoperation "-eq" arithmeticoperationatom
        | arithmeticoperation "-ne" arithmeticoperationatom 
        | arithmeticoperationatom "-ne" arithmeticoperation 

    //Definicion de operaciones con cadenas
    ?stringoperation: "-n" [string | var]
        | "-z" [string | var]
        | [string | var] "=" [string | var]
        | [string | var] "==" [string | var]
        | [string | var] "!=" [string | var]
        | [string | var] "\<" [string | var]
        | [string | var] "\>" [string | var]

    //Definicion de condiciones para la sentencia if
    ?condition: logicoperation
        | comparisonoperation
        | stringoperation
        | arithmeticoperation

    //Definicion de una variable
    ?var:  /[a-zA-Z]\w*/
        | "$" var
 
    //Definicion de una cadena
    ?string: /[\"].+[\"]/
        | /[\'].+[\']/

    //Definicion de un numero
    ?number: /\d+(\.\d+)?/

    //Ignorar comentarios de una línea, saltos de línea, espacios y tabulados
    %ignore /[\#].+/
    %ignore /\s+/

"""




grammarRb = """
        //El axioma inicial
        ?start: exp+

        //definicion de una expresion
        ?exp: argument+

        //Definir argumento
        ?argument: expre
            | sentence

        //Definir Expresión contenida en los argumentos
        ?expre: "def" var parameter argument+ "end" 
            | "/comment" comment* "uncomment/"
            | var "=" arithmeticoperation
            | var "="  string 
            | var "(" arithmeticoperation ")"
            | "def" var "(" parameter ")" argument+ "end"        
            | function
            | "(" arithmeticoperation ")" 	
            | "puts" "(" toprint* ")"
            | "puts" toprint 
            | "return" function 
            | /return?/ var arithmeticoperation 
            | arithmeticoperation "(" arithmeticoperation ")"
            | endfunction
    
        //Definir sentencia
        ?sentence: "if" boolean
            | "if" (comparisonoperation | logicoperation) argument+ "end" else?
            | "while" (boolean | comparisonoperation | logicoperation) argument+ "end"
            | "for" var "in" arithhmeticoperationatom ".." arithhmeticoperationatom "do" argument+ "end" 	
        
        //Definición de sentencia else
        ?else: "else" argument+ "end"

        //Definir operación fin de instrucción 
        ?endfunction:  "return" arithmeticoperation
            | "return" string
            | "return" boolean
            | "return" var "(" parameter* ")"

        //Definir función
        ?function: var "*" var "(" arithmeticoperation ")"
            | var "+" var "(" arithmeticoperation ")"
            | var "/" var "(" arithmeticoperation ")"
            | var "-" var "(" arithmeticoperation ")"

        //Definir operación lógica
        ?logicoperation: arithhmeticoperationatom logicoperator arithmeticoperation
            | arithmeticoperation logicoperator arithhmeticoperationatom
          
        //Definir comparación 
        ?comparisonoperation: arithhmeticoperationatom comparisonoperator arithmeticoperation
            | arithmeticoperation comparisonoperator arithhmeticoperationatom

        //Definicion de la operacion aritmetica 
        ?arithmeticoperation: product
            | arithmeticoperation "+" product
            | arithmeticoperation "-" product
        //Definicion de un atomo de operacion aritmetica
        ?product: arithhmeticoperationatom 
           | product "*" arithhmeticoperationatom
           | product "/" arithhmeticoperationatom 

        //Definicion del atomo de operacion aritmetica
        ?arithhmeticoperationatom: var
            | number
            | "-" arithhmeticoperationatom

        //Definición de operador logico
        ?logicoperator:  />=|<=|>|</
 
        //Definicion de los operadores de comparación
        ?comparisonoperator: /(==)|(!=)/

        //Definicion de booleano
        ?boolean: "true"
            | "false"

        //deficion de una cadena
        ?parameter: arithhmeticoperationatom
            | parameter "," arithhmeticoperationatom 
       
        //Definicion de lo contenido en un comentario
        ?comment: /./
       
        //Definicion de las distintas combinaciones al momento de imprimir
        ?toprint: string
            | arithmeticoperation
            | var "(" arithmeticoperation ")"

        //Definicion de cadenas
        ?string: /[\"].+[\"]/
            | /[\'].+[\']/

        //Deficion de una variable
        ?var: /[a-z][A-Za-z0-9_]*/

        //Deficion de un numero
        ?number: /\d+(\.\d+)?/

        //Ignorar comentarios de una línea, saltos de línea, espacios y tabulados
        %ignore /\s+/
        %ignore /[\#].+/
        
"""
        
