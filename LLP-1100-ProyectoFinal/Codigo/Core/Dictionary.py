# -*- coding: utf-8 -*-
"""
    ! Diccionario
    * Contiene palabras reservadas, booleanos, operadores lógicos. asignación, fin de instrucción
    inicio y fin de agrupación con su identificador para la creación de la tabla de símbolos.
    * El único lenguaje de progrmación encapsulado es JavaScript
    ? Incluye una función de busqueda interna para determinar si existe o no el lexema en el diccionario.
    @author Edgar Benedetto
    @author Bryan Gonzáles
    @author David Jácome
    @author Luis Banegas
    @date 2020/08/18
    @version 1.0
"""
class Dictionary:
    def __init__(self):
        self.json = {"return":"function return",
                "while":"cycle",
                "function":"Reserved word",
                "if":"Conditional",
                "console.log":"console print",
                "console.error":"console print error",
                "else":"Conditional",
                "false":"boleean",
                "for":"cycle",
                "null":"Reserved word",
                "break":"stop cycle",
                "==":"Comparision",
                "++":"Comparision",
                "--":"Comparision",
                "<=":"less than or equal",
                ">=":"greater than or equal",
                "!=":"different",
                "true":"boleean",
                "=":"Assignment",
                ";":"end of instruction",
                ",":"separator",
                "(":"Aggrupation Start",
                ")":"Aggrupation End",
                "{":"Aggrupation Start Function",
                "}":"Aggrupation End Function",
                "[":"Aggrupation End",
                "]":"Aggrupation End",
                "length":"Reserved word"
            }
    
    def searchDict(self,token):

        for k,v in  self.json.items():
            if token == k:
                return (True,v)
        return (False,"")