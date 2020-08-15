grammarBash =  """
    //Axioma inicial
    ?start: exp+
    //definicion de una expresion
    ?exp: "echo" combination  ";"?
        | var "=" string ";"?
        | var "=" arithmeticoperation ";"?
        | "if" "[" condition "]" ";"? "then" exp "else" exp "fi"
        | "if" "[" condition "]" ";"? "then" exp "fi"

    //Definicion de combinacion de variables y cadenas
    ?combination: string
        | var string*

    //Definicion de operacion aritmetica
    ?arithmeticoperation: product
        | arithmeticoperation "+" product 
        | arithmeticoperation "-" product 

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
    ?stringoperation: "-n" string
        | "-z" string
        | string "=" string
        | string "!=" string
        | string "\<" string
        | string "\>" string

    ?condition: logicoperation
        | comparisonoperation
        | stringoperation

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