import re 

grammarJS = """
        
        //El axioma inicial
        ?start: exp+

        //definicion de una expresion
        ?exp: argument+

        ?argument: expre 
            | sentence  

        //["if",[n,<,1,1]]<<   if(a[0] a[1] a[2])
        ?expre: "function" var "(" parameter? ")" arg -> assignfunc
            | arg        
            | var "=" "(" arithmeticoperation ")" ";" -> assignvar
            | var "=" arithmeticoperation ";" -> assignvar
            | var "=" "(" string ")" ";" -> assignvar
            | var "=" string  ";" -> assignvar
            | "console" "." "error" "(" (string | var)? ")" ";" -> printerror
            | "console" "." "log" "(" (string | arithmeticoperation | var)? ")" ";" -> printvar
            | "console" "." "log" "("string "," function ")" ";" -> printvar
            | "console" "." "log" "(" fun ")" ";" -> printvar
            | "console" "." "log" "(" concatenate ")" ";" ->printconcatenate
            | "return" function ";" -> getfunction
            | /return?/ var "(" arithmeticoperation ")" ";" -> assignfunction 
            | arithmeticoperation "(" arithmeticoperation ")" ";" -> assignrecursion
            | endfunction ";"
        ?fun: var "(" arithmeticoperation ")" -> assignfunction
        ?arg: "{" argument+ "}" -> getvalue
        //Definir sentencia
        ?sentence: "if" "(" boolean ")" -> assignif
            | "if" "(" (comparisonoperation | logicoperation) ")" "{" argument "}" ("else" "{" argument "}")? -> assignifelse
            | "if" "(" (comparisonoperation | logicoperation) ")"  argument ";" -> assignif
            | "while" "(" (boolean | comparisonoperation | logicoperation) ")" "{" argument+ "}" -> assignwhile
            | "for" "(" var "=" arithmeticoperationatom ";" (var logicoperator  arithmeticoperationatom ";")?  (var "++" | var "--") ")" "{" argument+ "}"  -> assignfor		
        
        //?else: "else" "{" argument+ "}" -> assignelse

        //Definir operación fin de instrucción 
        ?endfunction:  "return" arithmeticoperation -> getfunction
            | "return" string  -> getfunction
            | "return" boolean -> getfunction
          
           // | "return" var "(" parameter* ")" 

        ?function: var "*" var "(" arithmeticoperation ")" ->multfunction
            | var "+" var "(" arithmeticoperation ")" ->sumfunction
            | var "/" var "(" arithmeticoperation ")" ->divfunction
            | var "-" var "(" arithmeticoperation ")" ->subfunction
        //Definir operación lógica
        //a+b==b+a
        ?logicoperation: arithmeticoperationatom ">=" arithmeticoperationatom -> greaterequal
            | arithmeticoperationatom "<=" arithmeticoperationatom -> lesserequal
            | arithmeticoperationatom ">" arithmeticoperationatom -> greater
            | arithmeticoperationatom "<" arithmeticoperationatom -> lesser
          
        //Definir comparación 
        ?comparisonoperation: arithmeticoperationatom "==" arithmeticoperation -> compare
            | arithmeticoperation "==" arithmeticoperationatom -> compare
            | arithmeticoperation "!=" arithmeticoperationatom -> diferent
            | arithmeticoperationatom "!=" arithmeticoperation -> diferent

        //definicion de la operacion aritmetica 
        ?arithmeticoperation: product
            | arithmeticoperation "+" product -> sum
            | arithmeticoperation "-" product -> sub
        //definicion de un atomo de operacion aritmetica
        ?product: arithmeticoperationatom 
           | product "*" arithmeticoperationatom -> mul
           | product "/" arithmeticoperationatom -> div 

        ?arithmeticoperationatom: var -> getvar
            | number
            | "-" arithmeticoperationatom
            | "(" arithmeticoperation ")"        

        //Definición de operador logico
        ?logicoperator:  />=|<=|>|</
 
        ?comparisonoperator: /(==)|(!=)/
        //Definicion de booleano
        ?boolean: "true" ->gettrue
            | "false"

        //deficion de una cadena
        ?parameter: arithmeticoperationatom 
            | parameter "," arithmeticoperationatom 

        ?string: /"[^"]*"/
            | /'[^']*'/

        //deficion de una variable
        ?var: /[a-z][A-Za-z0-9_]*/

        //deficion de un numero
        ?number: /\d+(\.\d+)?/

        ?concatenate: string 
            | concatenate "+" string  
            | string "+" concatenate   
           
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
    
"""


grammarSh =  """
    //Axioma inicial
    ?start: exp+
    //definicion de una expresion
    ?exp: var "=" aritmeticoperationatom 
        | var "=" "$" aritmeticoperationatom
        | var "=" string
        | "echo" "\"" var "\""
        | "echo"  var 
        | "echo" "\"" combinate "\""
        | "echo" "\"" string* "\""
        | "echo" string* 
        | "echo" "\"" arithmeticoperation* "\""
 
    ?if: "if" "[[" condition "]]" ";"? "then" content "else" content "fi"
        | "if" "[[" condition "]]" ";"' "then" content "fi"
        | "if" "[[" condition "]]" ";"? "then" content "else" content "fi"
        | "if" "[[" condition "]]" ";"? "then" content elif "else" content "fi"
    
    ?logicoperation: arithmeticoperationatom "" arithmeticoperationatom
            //lesserequal
            | arithmeticoperationatom "-le" arithmeticoperationatom 
            //Greater
            | arithmeticoperationatom "-gt" arithmeticoperationatom 
            //Lesser
            | arithmeticoperationatom "-lt" arithmeticoperationatom 
          
        //Definir comparación 
    ?comparisonoperation: arithmeticoperationatom "-eq" arithmeticoperation 
        | arithmeticoperation "-eq" arithmeticoperationatom
        | arithmeticoperation "-ne" arithmeticoperationatom 
        | arithmeticoperationatom "-ne" arithmeticoperation 

    ?elif: "elif" content  
        | elif "elif" content 
    
    ?condition: conditionnum
        | conditionstr

    ?conditionnum:  aritmeticoperation

    ?conditionstr: string

    ?content: exp+

    ?combinate: string* var*
        | var* string

    ?boolean: "true" 
        |"false"

    ?exp2: if
        | "."
    //definicion de una variable
    ?var:  /[a-zA-Z]\w*/
        | "$" var
 
    //Definicion de una cadena
    ?string: /"[^"]*"/
        |  /̈́'[^']*'/
        | /[a-zA-Z][\w]+/
        | string " " string  

    //Definicion de un numero
    ?number: /\d+(\.\d+)?/
    s
    //Definicion de operacion aritmetica
    ?aritmeticoperation: product
        //| cadenaoperation "$" cadenaoperationatom -> con
        | aritmeticoperation "+" product -> sum
        | aritmeticoperation "-" product -> sub
    //definicion de un atomo de operacion aritmetica
    ?product: atom
        | product "*" atom
        | product "/" atom   
    ?atom: var -> getvar
        | number
        | "-" atom
        | "((" aritmeticoperation "))"
    ?concatenar: string 
        | concatenar "+" string -> con
        | concatenar "+" atom -> con
        | atom "+" concatenar -> con
    //Ignorar espacios,saltos de linea y tabulados
    %ignore /\s+/
    //Ignorar comentarios
    %ignore /\#\w+
"""
       