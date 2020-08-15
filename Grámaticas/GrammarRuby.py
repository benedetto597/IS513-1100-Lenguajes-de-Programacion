
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