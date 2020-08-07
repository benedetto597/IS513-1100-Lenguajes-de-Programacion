import re 

grammarJS = """
        
        //El axioma inicial
        ?start: exp+

        //definicion de una expresion
        ?exp: argument+

        ?argument: expre
            | sentence

        ?expre: "function" var "(" parameter? ")" "{" argument+ "}" -> assignfunc        
            | var "=" "(" arithmeticoperation ")" ";" -> assignvar
            | var "=" arithmeticoperation ";" -> assignvar
            | var "=" "(" string ")" ";" -> assignvar
            | var "=" string  ";" -> assignvar
            | "console" "." "error" "(" (string? | var) ")" ";" -> printvar
            | "console" "." "log" "(" (string? | arithmeticoperation? | var) ")" ";" -> printvar
            | "console" "." "log" "(" string "," function ")" ";" -> printvar
            | "return" function ";" -> getfunction
            | /return?/ var "(" arithmeticoperation ")" ";" -> assignrecursion 
            | arithmeticoperation "(" arithmeticoperation ")" ";" -> assignrecursion
            | endfunction ";"

        //Definir sentencia
        ?sentence: "if" "(" boolean ")" -> assignif
            | "if" "(" (comparisonoperation | logicoperation) ")" "{" argument+ "}" else? -> assignif
            | "if" "(" (comparisonoperation | logicoperation) ")"  argument -> assignif
            | "while" "(" (boolean | comparisonoperation | logicoperation) ")" "{" argument+ "}" -> assignwhile
            | "for" "(" var "=" arithhmeticoperationatom ";" (logicoperation | arithhmeticoperationatom) ";" (var "++" | var "--") ")" "{" argument+ "}"  -> assignfor		
        
        ?else: "else" "{" argument+ "}" -> assignelse

        //Definir operación fin de instrucción 
        ?endfunction:  "return" arithmeticoperation -> assignend
            | "return" string -> assignend
            | "return" boolean -> assignend
            | "return" var "(" parameter* ")"

        ?function: var "*" var "(" arithmeticoperation ")" ->multfunction
            | var "+" var "(" arithmeticoperation ")" ->sumfunction
            | var "/" var "(" arithmeticoperation ")" ->divfunction
            | var "-" var "(" arithmeticoperation ")" ->subfunction
        //Definir operación lógica
        //a+b==b+a
        ?logicoperation: arithhmeticoperationatom logicoperator arithmeticoperation
            | arithmeticoperation logicoperator arithhmeticoperationatom
          
        //Definir comparación 
        ?comparisonoperation: arithhmeticoperationatom comparisonoperator arithmeticoperation
            | arithmeticoperation comparisonoperator arithhmeticoperationatom

        //definicion de la operacion aritmetica 
        ?arithmeticoperation: product
            | arithmeticoperation "+" product -> sum
            | arithmeticoperation "-" product -> sub
        //definicion de un atomo de operacion aritmetica
        ?product: arithhmeticoperationatom 
           | product "*" arithhmeticoperationatom -> mul
           | product "/" arithhmeticoperationatom -> div 

        ?arithhmeticoperationatom: var -> getvar
            | number
            | "-" arithhmeticoperationatom
            | "(" arithmeticoperation ")"        

        //Definición de operador logico
        ?logicoperator:  />=|<=|>|</
 
        ?comparisonoperator: /(==)|(!=)/
        //Definicion de booleano
        ?boolean: "true"
            | "false"

        //deficion de una cadena
        ?parameter: arithhmeticoperationatom ->  assignparameter
            | parameter "," arithhmeticoperationatom 

        ?string: /"[^"]*"/
            | /'[^']*'/

        //deficion de una variable
        ?var: /[a-z][A-Za-z0-9_]*/

        //deficion de un numero
        ?number: /\d+(\.\d+)?/

        ?concatenate: string 
            | concatenate "+" string -> con
            | concatenate "+" arithhmeticoperationatom -> con
            | arithhmeticoperationatom "+" concatenate -> con
        
        //ignore
        %ignore /\s+/

""" 


grammarRb = """
        //El axioma inicial
        ?start: exp+

        //definicion de una expresion
        ?exp: argument+

        ?argument: expre
            | sentence

        ?expre: "def" var parameter argument+ "end" -> assignfunc        
            | var "=" arithmeticoperation -> assignvar
            | var "="  string  -> assignvar
            | var "=" string  -> assignvar
            //| var "=" arithhmeticoperationatom "+" arithhmeticoperationatom
            //| var "=" arithhmeticoperationatom "-" arithhmeticoperationatom

            | "puts" (string? | arithmeticoperation?) -> printvar
            | "return" function  -> getfunction
            | /return?/ var arithmeticoperation-> assignrecursion 
            | arithmeticoperation "(" arithmeticoperation ")" -> assignrecursion
            | endfunction

        //Definir sentencia
        ?sentence: "if" boolean -> assignif
            | "if" (comparisonoperation | logicoperation) argument+ -> assignif
            | "if" (comparisonoperation | logicoperation) argument+ "end" else? -> assignif
            | "while" (boolean | comparisonoperation | logicoperation) argument+ "end" -> assignwhile
            | "for" var "in" arithhmeticoperationatom ".." arithhmeticoperationatom "do" argument+ "end"  -> assignfor		
        
        ?else: "else" argument+ "end" -> assignelse

        //Definir operación fin de instrucción 
        ?endfunction:  "return" arithmeticoperation -> assignend
            | "return" string -> assignend
            | "return" boolean -> assignend
            | "return" var "(" parameter* ")"

        ?function: var "*" var "(" arithmeticoperation ")" ->multfunction
            | var "+" var "(" arithmeticoperation ")" ->sumfunction
            | var "/" var "(" arithmeticoperation ")" ->divfunction
            | var "-" var "(" arithmeticoperation ")" ->subfunction
        //Definir operación lógica
        //a+b==b+a
        ?logicoperation: arithhmeticoperationatom logicoperator arithmeticoperation
            | arithmeticoperation logicoperator arithhmeticoperationatom
          
        //Definir comparación 
        ?comparisonoperation: arithhmeticoperationatom comparisonoperator arithmeticoperation
            | arithmeticoperation comparisonoperator arithhmeticoperationatom

        //definicion de la operacion aritmetica 
        ?arithmeticoperation: product
            | arithmeticoperation "+" product -> sum
            | arithmeticoperation "-" product -> sub
        //definicion de un atomo de operacion aritmetica
        ?product: arithhmeticoperationatom 
           | product "*" arithhmeticoperationatom -> mul
           | product "/" arithhmeticoperationatom -> div 

        ?arithhmeticoperationatom: var -> getvar
            | number
            | "-" arithhmeticoperationatom
            | "(" arithmeticoperation ")"        

        //Definición de operador logico
        ?logicoperator:  />=|<=|>|</
 
        ?comparisonoperator: /(==)|(!=)/
        //Definicion de booleano
        ?boolean: "true"
            | "false"

        //deficion de una cadena
        ?parameter: arithhmeticoperationatom ->  assignparameter
            | parameter "," arithhmeticoperationatom 

        ?string: /"[^"]*"/
            | /'[^']*'/

        //deficion de una variable
        ?var: /[a-z][A-Za-z0-9_]*/

        //deficion de un numero
        ?number: /\d+(\.\d+)?/

        ?concatenate: string 
            | concatenate "+" string -> con
            | concatenate "+" arithhmeticoperationatom -> con
            | arithhmeticoperationatom "+" concatenate -> con
        
        //ignore
        %ignore /\s+/
        %ignore /#.*/
        %ignore //
        
"""


grammarSh = """
?start: exp+

"""
