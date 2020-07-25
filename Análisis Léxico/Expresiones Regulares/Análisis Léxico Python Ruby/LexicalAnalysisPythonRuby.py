# -*- coding: utf-8 -*-
"""
    !Token Reader Python & Ruby (Analizador Léxico para archivos .py y .rb)
    *Permite el reconocimiento de distintos tokes usando expresiones regulares para Python y Ruby.
    Este programa posee lexema de palabras especiales, identificadores de usuario, 
    valores númericos, cadenas, fin de instrucción y saltos de línea, etc. Y todos los que 
    se necesiten para poder leer los archivos de la primer clase sincrona (29/06/2020)
    *Esta implementación no aplica el uso de "automatas finitos".
    ?No comprende sintñaxis, ni precedencia, ni comentarios, ni operadores, ni cadenas, etc.
    ?El resultado de un programa real deberá ser el pipeline que alimenta al análisis sintáctico
    @author Benedetto
    @date 2020/07/08
    @version 0.1
"""
from tabulate import tabulate
import sys, re

class TokenParserPythonRuby:

    def __init__(self): 
        self.python = [
            ["print","Impresión a consola"],
            ['"""',"Comentario de multiples líneas"],
            [";","Fin de instrucción"],
        ]
        
        self.ruby = [
            ["puts","Impresión a consola"],
            ["/comment","Inicio de comentario"],
            ["uncomment/","Fin de comentario"],
            ["end","Fin de instrucción"],
        ]

        self.generals = [
            ["+","Operador de suma"],
            ["-","Operador de resta"],
            ["*","Operador de multiplicación"],
            ["/","Operador de división"],
            ["%","Operador módulo o parseo"],
            ["=","Operador de asignación"],
            [",","Separador de instrucción"],
            [":","Asignador de función"],
            ["not","Booleano de negación"],
            ["and","Booleano de conjunción"],
            ["or","Booleano de disyunción"],
            ["True","Literal booleano"],
            ["False","Literal booleano"],
            ["def","Declaración de función"],
            ["class","Declaración de clase"],
            ["if","Bucle si"],
            ["else","Bucle si-no"],
            ["elif","Bucle si-no si"],
            ["#","Comentario de una línea"],
            ['"',"Comilla Doble"],
            ["'","Comilla Simple"],
            ["return","Retorno de función"],
            ["(","Inicio de agrupación"],
            ["[","Inicio de agrupación"],
            [")","Fin de Agrupación"],
            ["]","Fin de Agrupación"],
            [">","Operador de comparación mayor que"],
            ["<","Operador de comparación menor que"],
        ]

    def help(self):

        print("")
        print("*"*80)
        print("*"*80) 
        print("\tToken Reader Python & Ruby")
        print("""
        \tPermite el reconocimiento de distintos tokens usando expresiones 
        \tregulares para un lenguajes de múltiples instrucciones por línea 
        \tde código. 
        """)
        print("*"*80)
        print("*"*80)

    def read(self):
        #Ejemplo de ejecución python3 lexicalAnalysis.py sample1.py o sample1.rb
        param = sys.argv[1:]

        if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")

        self.fileName = param[0]
        if(re.match("^.*.py$",self.fileName) or re.match("^.*.rb$",self.fileName)):
            f = open(self.fileName,"r")
            self.text = f.read() #Lee la completidud del programa
            f.close()
        else:
            print("\tArchivo con extensión desconocida")
            print("\tFinalizando ejecución")

        return self

    def preprocess(self):

        text = self.text
        
        text = re.sub(r"\+"," + ", text)
        text = re.sub(r"\-"," - ", text)
        text = re.sub(r"\*"," * ", text)
        text = re.sub(r"/(?!comment) | (?!uncomment)/"," / ", text)
        text = re.sub(r"\%"," % ", text)
        text = re.sub(r"\#@"," # @ ", text)
        text = re.sub(r"\="," = ", text)
        text = re.sub(r"\,"," , ", text)
        text = re.sub(r"\:"," : ", text)
        text = re.sub(r"\not$"," not ", text)
        text = re.sub(r"\and$"," and ", text)
        text = re.sub(r"\or$"," or ", text)
        text = re.sub(r"\True"," True ", text)
        text = re.sub(r"\False"," False ", text)
        text = re.sub(r"\def"," def ", text)
        text = re.sub(r"\class"," class ", text)
        text = re.sub(r"\if"," if ", text)
        text = re.sub(r"\elif"," elif ", text)
        text = re.sub(r"\else"," else ", text)
        text = re.sub(r"\return"," return ", text)
        text = re.sub(r"\'.[a-zA-Z][a-zA-Z0-9\_\-]*"," ' ", text)
        text = re.sub(r'\".[a-zA-Z][a-zA-Z0-9\_\-]*',' " ' , text)
        text = re.sub(r"\("," ( ", text)
        text = re.sub(r"\)"," ) ", text)
        text = re.sub(r"\["," [ ", text)
        text = re.sub(r"\]"," ] ", text)
        text = re.sub(r"\<"," < ", text)
        text = re.sub(r"\>"," > ", text)
        text = re.sub(r"\s+"," ", text)
        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text
        remembered, stringDouble, stringSimple, comment = "","","",""
        tokenLine = 0

        tokens = re.split(r"\s",text)

        for token in tokens:

            token = ("%s".strip() % token).strip()
            if len(token) > 0:
                #Símbolos
                generalToken = self.checkToken(token, self.generals)

                if(re.match(r"^\#.[a-zA-Z][a-zA-Z0-9\_\-]*$",token)):
                    remembered = ""
                    result += [["Se reconoce un comentario de una línea: " ,"%s"% token[0]]]
                    comment = token

                elif(re.match(r"^\#.[a-zA-Z][a-zA-Z0-9\_\-]*$",remembered)):
                    rememberLine = self.searchTokenLine(remembered)
                    tokenLine = self.searchTokenLine(token)
                    
                    if(rememberLine == tokenLine):
                        comment = comment + " " + token
                    else:
                        remembered = ""
                        result += [["Se reconoce un comentario: " ,"%s"% token]]
                        comment = ""

                #Comentario de multiples líneas
                elif(re.match(r"^\"\"\"$",remembered) or re.match(r"^/comment$",remembered)):
                    if(re.match(r"^\"\"\"$",token) or re.match(r"^uncomment/$",token)):
                        remembered = ""
                        result += [["Se reconoce un comentario : " ,"%s"%comment]]
                        result += [["Se reconoce fin de comentario: " ,"%s"%token]]
                        comment = ""
                    else:
                        comment = comment + " " +  token
                

                #Cadena
                elif(re.match(r"^\'$",remembered) or re.match(r"^\"$",remembered)):
                    if(re.match(r"^\"$",remembered)):
                        if(re.match(r"^\"$",token)):
                            remembered = ""
                            result += [["Se reconoce una cadena : " ,"%s"%stringDouble]]
                            result += [["Se reconoce una comilla doble : " ,"%s"%token]]
                        else:
                            stringDouble = stringDouble + " " + token

                    if(re.match(r"^\'$",remembered)):
                        if(re.match(r"^\'$",token)):
                            remembered = '"'
                            result += [["Se reconoce una cadena : " ,"%s"%stringSimple]]
                            result += [["Se reconoce una comilla simple : " ,"%s"%token]]
                        else:
                            stringSimple = striingSimple + " " + token
                
                #Es un token exclusivo de python
                elif (re.match(r"^;$",token) or re.match(r"^\"\"\"$",token) or re.match(r"^print$",token)):
                    if(re.match("^.*.py$",self.fileName)):
                        tokenPython = self.checkToken(token, self.python)
                        remembered = token
                        result += [["Se reconoce %s " % tokenPython[1],"%s"%token]]
                    else:
                        quit(
                        "Error: \n\tSe ha encontrado un token desconocido para el lenguaje de Ruby en la línea '%d': '%s'\n\n" %(
                            self.searchTokenLine(token),
                            token
                        )
                    )

                #Es un token exclusivo de ruby
                elif (re.match(r"^uncomment/$",token) or re.match(r"^/comment$",token) or re.match(r"^puts$",token) or re.match(r"^end$",token)):
                    if(re.match("^.*.rb$",self.fileName)):
                        tokenRuby = self.checkToken(token, self.ruby)
                        remembered = token
                        result += [["Se reconoce %s " % tokenRuby[1],"%s"%token]]
                    else:
                        quit(
                        "Error: \n\tSe ha encontrado un token desconocido para el lenguaje de Python en la línea '%d': '%s'\n\n" %(
                            self.searchTokenLine(token),
                            token
                        )
                    )

                elif(len(generalToken) > 0):
                    remembered = token
                    result += [["Se reconoce %s: " % generalToken[1],"%s"%token]]
                
                #Es un identificador de usuario
                elif re.match(r"^[a-zA-Z][a-zA-Z0-9\_\-]*$",token):
                    remembered = token
                    result += [["Se reconoce el identificador de usuario: ","%s"%token]]

                #Es un operador de asignación
                elif re.match(r"^=$",token):
                    result += [["Se reconoce el operador de asignación: ","%s"%token]]

                #Es un número flotante
                elif re.match(r"^\d+\.\d+$",token):
                    remembered = token
                    result += [["Se reconoce el número flotante: ","%s"%token]]

                #Es un número entero
                elif re.match(r"^\d+$",token):
                    remembered = token
                    result += [["Se reconoce el número entero: ","%s"%token]]
                
                #Es un token desconcido
                else:
                    quit(
                        "Error: \n\tSe ha encontrado un token desconocido en la línea '%d': '%s'\n\n" %(
                            self.searchTokenLine(token),
                            token
                        )
                    )

        return result

    def checkToken(self, token):
        #Verificar si el token es una palabra reservada 
        pass

    def searchTokenLine(self, token):

        errorLine = 0

        f = open(self.fileName, "r")

        for line in f:
            errorLine += 1
            #Si encontramos el token se retorna la línea
            if re.match(r"^.*%s.*$" % self.prevent(token), line):
                break

        f.close()

        return errorLine

    def prevent(self, token):

        if re.match(r"[\+\*\.\(\)\{\}\[\]]+",token):
            return "\\%s" % token
        return token

    def checkToken(self, token, grammar):
        result = []
        for knowToken in grammar:
            if(knowToken[0] == token):
                result.append(knowToken[0])
                result.append(knowToken[1])
        
        return result