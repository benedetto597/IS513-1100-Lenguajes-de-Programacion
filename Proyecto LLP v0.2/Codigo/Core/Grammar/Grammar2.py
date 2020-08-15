grammarJS = """
        
        //El axioma inicial
        ?start: exp+

        //definicion de una expresion
        ?exp: argument+

        ?argument: expre 
            | sentence  
            
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

        ?expre: "def" var parameter argument+ "end"        
            | var "=" arithmeticoperation
            | var "="  string 
            | var "=" string 
            //| var "=" arithhmeticoperationatom "+" arithhmeticoperationatom
            //| var "=" arithhmeticoperationatom "-" arithhmeticoperationatom

            | "puts" (string? | arithmeticoperation?)
            | "return" function 
            | /return?/ var arithmeticoperatio 
            | arithmeticoperation "(" arithmeticoperation ")"
            | endfunction

        //Definir sentencia
        ?sentence: "if" boolean
            | "if" (comparisonoperation | logicoperation) argument+
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
            | "(" arithmeticoperation ")"        

        //Definición de operador logico
        ?logicoperator:  />=|<=|>|</
 
        ?comparisonoperator: /(==)|(!=)/
        //Definicion de booleano
        ?boolean: "true"
            | "false"

        //deficion de una cadena
        ?parameter: arithhmeticoperationatom
            | parameter "," arithhmeticoperationatom 

        ?string: /"[^"]*"/
            | /'[^']*'/

        //deficion de una variable
        ?var: /[a-z][A-Za-z0-9_]*/

        //deficion de un numero
        ?number: /\d+(\.\d+)?/

        ?concatenate: string 
            | concatenate "+" string 
            | concatenate "+" arithhmeticoperationatom 
            | arithhmeticoperationatom "+" concatenate 
        
        //ignore
        %ignore /\s+/
        %ignore /\#\.+/
        
"""




grammar = """
    //todo minusculas
    //Axioma inicial
    ?start: exp+
    //definicion de una expresion
    ?exp: var "=" "(" string ")" ";" -> assignvar
        | "print" "(" concatenar ")" ";" -> printvar
        | "print"  concatenar  ";" -> printvar
        | "print" "(" var ")" ";" -> printvar
        | "print"  var  ";" -> printvar
        | var "=" "("  concatenar ")" ";" -> assignvar
        | var "="  concatenar  ";" -> assignvar
        | var "=" "(" aritmeticoperation ")" ";" -> assignvar
        | var "=" aritmeticoperation ";" -> assignvar
        | if -> funcionif
    ?if: "if" "(" boolean ")" "{" exp2 "}"

    ?boolean: "true" 
        |"false"

    ?exp2: if
        | "."
    //definicion de una variable
    ?var: /[a-zA-Z]\w*/   
    //Definicion de una cadena
    ?string: /"[^"]*"/
        |  /̈́'[^']*'/
    //Definicion de un numero
    ?number: /\d+(\.\d+)?/
    //Definicion de operacion aritmetica
    ?aritmeticoperation: product
        //| cadenaoperation "$" cadenaoperationatom -> con
        | aritmeticoperation "+" product -> sum
        | aritmeticoperation "-" product -> sub
    //definicion de un atomo de operacion aritmetica
    ?product: atom
        | product "*" atom -> mul
        | product "/" atom -> div  
    ?atom: var -> getvar
        | number
        | "-" atom
        | "(" aritmeticoperation ")"
    ?concatenar: string 
        | concatenar "+" string -> con
        | concatenar "+" atom -> con
        | atom "+" concatenar -> con
    //Ignorar espacios,saltos de linea y tabulados
    %ignore /\s+/
"""
