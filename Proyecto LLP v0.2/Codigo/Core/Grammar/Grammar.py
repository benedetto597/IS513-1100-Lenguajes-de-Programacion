# -*- coding: utf-8 -*-

import re 

grammarFun = """

        ?start: exp+
        
        ?exp: "function" var "(" (var ","?)* ")" "{" argument* "}" -> addfunction
            | var "("((var|number) ","?)* ")" ";"? -> showfunction
            | "console" "." "log" "(" string "," exp ")" ";"   -> getshowrecursin
            //| inicoment cualquieronda finalcoment  -> coment
            
            
        ?argument: var "=" (number|string|var) ";"   ->assingvar 
            | "return" (number) ";" -> getreturn
            | "return" (var) ";" -> getreturntwo
            | "return" (string) ";"-> getreturnthre
            | "console" "." "error" "(" (var|number|string) ")" ";" -> getconsoleerror
            | "return" var operator var "(" var operator number ")" ";"   -> getreturnfunction
            | "console" "." "log" "(" (number|string) ")" ";"   -> getconsole
            | "console" "." "log" "(" var ")" ";"   -> getconsolevar
            | "if" "(" var operation number ")" var number ";" -> getif 
            //| "if" "(" var operation number ")" var number ";" -> getif 
            | inicoment content* finalcoment -> coment
            | inicoment content* -> coment

        //?showfun: var "("((var|number) ","?)* ")" -> showfunction
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


