# -*- coding: utf-8 -*-

import re 

grammarFun = """

        ?start: exp+
        
        ?exp: "function" var "(" (var ","?)* ")" "{" argument* "}" -> addfunction
            | var "("((var|number) ","?)* ")" ";"? -> showfunction
            | var "(" var operator number ")" ";"? -> getrecursive
            | "console" "." "log" "(" string "," exp ")" ";"   -> getcon
            
            //| inicoment cualquieronda finalcoment  -> coment                        
        ?argument: var "=" (number|string|var) ";"   ->assingvar 
            //| "for" "(" var "=" number ";" var operation (number|var)  ";"  var increment")""{" argument* "}" ->
            | "return" (number) ";"? -> getreturn 
            | "return" (var) ";"? -> getreturntwo
            | "return" (string) ";"? -> getreturnthre
            | "return" reserve ";"? -> getreturnreser
            | "return" var operator exp ";"?   -> getreturnfunction
            | "console" "." "error" "(" (var|number|string) ")" ";" -> getconsoleerror
            | "console" "." "log" "(" (number|string) ")" ";"   -> getconsole
            | "console" "." "log" "(" var ")" ";"   -> getconsolevar
            | "if" "(" var operation number ")" argument ";"? -> getif 
            | "if" "(" (var|number) operation (number|var) ")" "{" argument "}" -> ifelse
            | else  
            | "while" "(" logicoperation ")" init argument* "}" -> getwhile
            | break ";" -> getcomant
            | inicoment content* finalcoment -> coment
            | inicoment content* -> coment

        ?else: "else" init argument "}"  -> getelse 

        ?init: "{"

        ?break : "break"

        ?reserve: "true"
            | "false"
            | "null"

        ?logicoperation: var operation var 
        //?showfun: var "("((var|number) ","?)* ")" -> showfunction

        ?arithmeticoperationatom: var 
            | number
            | "-" arithmeticoperationatom
          
        //?ree:number
        ?string: /"[^"]*"/
            |  /̈́'[^']*'/

        ?operator:/\*/
                | /\+/
                | /\-/
                | /\//
        
        ?operation: /\==/
                | /\</
                | /\>/
                | /\>\=/
                | /\<\=/
                | /\!\=/
                
        ?increment: /\+\+/
                | /\-\-/


        ?inicoment: "/*"
                | "//"

        ?finalcoment: "*/"

        ?content: /[a-z]\w*/
                | /.+/
                | /\d+(\.\d+)?/
                | /̈́'[^']*'/
                | /"[^"]*"/
                

        ?number: /\d+(\.\d+)?/


        ?var: /[a-z][\w]*/

        %ignore /\s+/


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

    //Ignorar comentarios
    %ignore /[\#].+/
    %ignore /\s+/

"""



grammarRb = """
        //El axioma inicial
        ?start: exp+

        //definicion de una expresion
        ?exp: argument+

        ?argument: expre
            | sentence

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
        
        ?else: "else" argument+ "end"

        //Definir operación fin de instrucción 
        ?endfunction:  "return" arithmeticoperation
            | "return" string
            | "return" boolean
            | "return" var "(" parameter* ")"

        ?function: var "*" var "(" arithmeticoperation ")"
            | var "+" var "(" arithmeticoperation ")"
            | var "/" var "(" arithmeticoperation ")"
            | var "-" var "(" arithmeticoperation ")"
        //Definir operación lógica
        //a+b==b+a
        ?logicoperation: arithhmeticoperationatom logicoperator arithmeticoperation
            | arithmeticoperation logicoperator arithhmeticoperationatom
          
        //Definir comparación 
        ?comparisonoperation: arithhmeticoperationatom comparisonoperator arithmeticoperation
            | arithmeticoperation comparisonoperator arithhmeticoperationatom

        //definicion de la operacion aritmetica 
        ?arithmeticoperation: product
            | arithmeticoperation "+" product
            | arithmeticoperation "-" product
        //definicion de un atomo de operacion aritmetica
        ?product: arithhmeticoperationatom 
           | product "*" arithhmeticoperationatom
           | product "/" arithhmeticoperationatom 

        ?arithhmeticoperationatom: var
            | number
            | "-" arithhmeticoperationatom

        //Definición de operador logico
        ?logicoperator:  />=|<=|>|</
 
        ?comparisonoperator: /(==)|(!=)/

        //Definicion de booleano
        ?boolean: "true"
            | "false"

        //deficion de una cadena
        ?parameter: arithhmeticoperationatom
            | parameter "," arithhmeticoperationatom 
       
        ?comment: /./
       
        ?toprint: string
            | arithmeticoperation
            | var "(" arithmeticoperation ")"

        ?string: /[\"].+[\"]/
            | /[\'].+[\']/

        //deficion de una variable
        ?var: /[a-z][A-Za-z0-9_]*/

        //deficion de un numero
        ?number: /\d+(\.\d+)?/

        //ignore
        %ignore /\s+/
        %ignore /[\#].+/
        
"""