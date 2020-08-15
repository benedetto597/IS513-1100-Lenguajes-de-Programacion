# -*- coding: utf-8 -*-

import re 

grammarFun = """

        ?start: exp+
        
        ?exp: "function" var "(" (var ","?)* ")" "{" argument* "}" 
            | var "("((var|number) ","?)* ")" ";"? 
            | "console" "." "log" "(" string "," exp ")" ";"   
            //| inicoment cualquieronda finalcoment  
            
            
        ?argument: var "=" (number|string|var) ";"    
            | "return" (number) ";" 
            | "return" (var) ";" 
            | "return" (string) ";"
            | "console" "." "error" "(" (var|number|string) ")" ";" 
            | "return" var operator var "(" var operator number ")" ";"   
            | "console" "." "log" "(" (number|string) ")" ";"   
            | "console" "." "log" "(" var ")" ";"   
            | "if" "(" var operation number ")" var number ";"  
            //| "if" "(" var operation number ")" var number ";"  
            | inicoment content* finalcoment 
            | inicoment content* 

        //?showfun: var "("((var|number) ","?)* ")" 
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
                
       
        ?inicoment: "/*"
                | "//"

        ?finalcoment: "*/"

        ?content: /[a-z]\w*/
                | /.+/
                | /\d+(\.\d+)?/
                | /̈́'[^']*'/
                | /"[^"]*"/
                

        ?number: /\d+(\.\d+)?/

        ?var: /[a-z]\w*/

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
            | "def" var "(" parameter ")" argument+ "end"        
            | var "=" arithmeticoperation
            | var "="  string 
            | "(" arithmeticoperation ")" 	
            | "puts" "(" toprint* ")"
            | "puts" toprint 
            | "return" function 
            | /return?/ var arithmeticoperation 
            | arithmeticoperation "(" arithmeticoperation ")"
            | var "(" arithmeticoperation ")"
            | endfunction
            | "/comment" comment* "uncomment/"
    
        ?comment: /./
        
        ?toprint: string
            | arithmeticoperation
            | var "(" arithmeticoperation ")"
           
        //Definir sentencia
        ?sentence: "if" boolean
            | "if" (comparisonoperation | logicoperation) argument+ "end"
            | "if" (comparisonoperation | logicoperation) argument+ else "end" 
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
       