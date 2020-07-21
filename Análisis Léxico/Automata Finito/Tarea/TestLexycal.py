# -*- coding: utf-8 -*-
"""
    !Token Reader (Analizador Léxico)
    *Permite el reconocimiento de distintos tokes usados en el lenguaje de C++. 
    Este programa posee lexema de palabras especiales,
    *Esta implementación aplica el uso de "automatas finitos"
    @author Edgar Benedetto
    @date 2020/07/19
    @version 0.1
"""

from tabulate import tabulate
import sys

class Test:
    def __init__(self): 
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.symbols = ["+","-","/","*","=","==","(",")","++","+=",";",":","::","<",">","<=",">=","{","}","_","<<",">>",'"',"'","/","/*","*/"]
        self.brakes = ["\n","\t"," "]
        self.specials = ["return","#include","#define","int","main","namespace","std","cout","cin","float","#endif","#ifndef","class","public"]

    def read(self):
        param = sys.argv[1:]

        if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")

        self.fileName = param[0]
        f = open(self.fileName,"r")
        self.text = f.read()
        f.close()

        return self

    def lexicalAnalysis(self):
        text = self.text
        result = []
        new_token = ""
        line = 0
        i = 0

        while(i != len(text)):
            possible_answers = filtrate(text[i])

            if(len(possible_answers) > 0):
                #Si se encuentra el numero despues del punto del token no se toma en cuenta
                    
                #Palabras reservadas
                if("#include" in possible_answers or "#endif" in possible_answers or "#ifndef" in possible_answers):
                    if(text[i+1] == "i"):
                        if(text[i+2] == "n"):
                            new_toke = "#include"
                            result += [["Se reconoce la palabra reservada: ","%s"%new_toke]]
                            new_token = ""
                            i = i + 7
                            
                        elif(text[i+2] == "f"):
                            new_toke = "#ifndef"
                            result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                            new_token = ""
                            i = i + 6

                    elif(text[i+1] == "e"):
                        new_toke = "#endif"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 5

                if("return" in possible_answers or "int" in possible_answers or "main" in possible_answers or "namespace" in possible_answers or "std" in possible_answers or "cout" in possible_answers or "cin" in possible_answers or "float" in possible_answers or "class" in possible_answers or "public" in possible_answers):
                    if(text[i] == "c"):
                        if(text[i+1] == "o" and text[i+2] == "u" and text[i+3] == "t"):
                            new_toke = "cout"
                            result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                            new_token = ""
                            i = i + 3
                        if(text[i+1] == "i" and text[i+2] == "n"):
                            new_toke = "cin"
                            result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                            new_token = ""
                            i = i + 2
                        if(text[i+1] == "l" and text[i+2] == "a" and text[i+3] == "s" and text[i+4] == "s"):
                            new_toke = "class"
                            result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                            new_token = ""
                            i = i + 4
                    if(text[i] == "r" and text[i+1] == "e" and text[i+2] == "t" and text[i+3] == "u" and text[i+4] == "r" and text[i+5] == "n"):
                        new_toke = "return"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 5
                    if(text[i] == "i" and text[i+1] == "n" and text[i+2] == "t"):
                        new_toke = "int"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 2
                    if(text[i] == "m" and text[i+1] == "a" and text[i+2] == "i" and text[i+3] == "n"):
                        new_toke = "main"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 3
                    if(text[i] == "s" and text[i+1] == "t" and text[i+2] == "d" ):
                        new_toke = "std"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 2
                    if(text[i] == "f" and text[i+1] == "l" and text[i+2] == "o" and text[i+3] == "a" and text[i+4] == "t"):
                        new_toke = "float"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 4
                    if(text[i] == "p" and text[i+1] == "u" and text[i+2] == "b" and text[i+3] == "l" and text[i+4] == "i" and text[i+5] == "c"):
                        new_toke = "public"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 5
                    if(text[i] == "n" and text[i+1] == "a" and text[i+2] == "m" and text[i+3] == "e" and text[i+4] == "i" and text[i+5] == "e"  and text[i+6] == "s"  and text[i+7] == "p" and text[i+8] == "a" and text[i+9] == "c" and text[i+10] == "e"):
                        new_toke = "namespace"
                        result += [["Se reconoce la palabra reservada: ","%s"%new_token]]
                        new_token = ""
                        i = i + 10

                #Identificadores de usuario
                if(text[i] in self.alphabet):
                    while(text[i] != " " or text[i] != "\t" or text[i] != "\n" or text[i] != ";" or text[i] != "," or text[i] != "+" or text[i] != "-" or text[i] != "*" or text[i] != "/" or text[i] != "=" or text[i] != "==" or text[i] != "(" or text[i] != ")" or text[i] != "."):
                        new_token = new_token + text[i]
                        i++
                    result += [["Se reconoce un identificador de usuario: ","%s"%new_token]]
                    new_token = ""

                #Digitos
                if(text[i] in self.numbers):
                    while(text[i] != " " or text[i] != "\t" or text[i] != "\n" or text[i] != ";" or text[i] != "," or text[i] != "+" or text[i] != "-" or text[i] != "*" or text[i] != "/" or text[i] != "=" or text[i] != "==" or text[i] != "(" or text[i] != ")"):
                        new_token = new_token + text[i]
                        i++
                    if("." in new_token):
                        result += [["Se reconoce un número de coma flotante: ","%s"%new_token]]
                    else:
                        result += [["Se reconoce un número entero: ","%s"%new_token]]
                    new_token = ""
                #Simbolos
                #FALTAN COMENTARIOS
                if("'" in possible_answers):
                    result += [["Se reconoce una comilla simple: ","%s"%text[i]]
                    i++
                    while(text[i] != '"'):
                        new_token = new_token + text[i]
                        i++
                    result += [["Se reconoce una cadena: ","%s"%new_token]
                    result += [["Se reconoce una comilla simple: ","%s"%text[i]]
                    i++
                    
                    new_token = ""

                if('"' in possible_answers):
                    result += [["Se reconoce una comilla doble: ","%s"%text[i]]
                    i++
                    while(text[i] != '"'):
                        new_token = new_token + text[i]
                        i++
                    result += [["Se reconoce una cadena: ","%s"%new_token]
                    result += [["Se reconoce una comilla doble: ","%s"%text[i]]
                    i++
                    
                    new_token = ""

                if("," in possible_answers):
                    result += [["Se reconoce el operador de separación: ","%s"%text[i]]]
                    new_token = ""

                if("{" in possible_answers):
                    result += [["Se reconoce el operador de inicio declaración: ","%s"%text[i]]]
                    new_token = ""

                if("{" in possible_answers):
                    result += [["Se reconoce el operador de fin declaración: ","%s"%text[i]]]
                    new_token = ""

                if(">" in possible_answers):
                    if(text[i-1] != ">" ):
                        result += [["Se reconoce el operador comparación de mayor que: ","%s"%text[i]]]
                        new_token = ""
                    else:
                        result += [["Se reconoce el operador de nivel de bit de desplazamiento a la derecha: ","%s"%text[i] + text[i-1]]]
                        new_token = ""

                if("<" in possible_answers):
                    if(text[i-1] != "<" ):
                        result += [["Se reconoce el operador de comparación menor que: ","%s"%text[i]]]
                        new_token = ""
                    else:
                        result += [["Se reconoce el operador de nivel de bit de desplazamiento a la izquierda: ","%s"%text[i] + text[i-1]]]
                        new_token = ""

                if("::" in possible_answers):
                    result += [["Se reconoce el operador de alcance: ","%s"%text[i] + text[i-1]]]
                    new_token = ""

                if("(" in possible_answers):
                        result += [["Se reconoce el operador de inicio de agrupación: ","%s"%text[i]]]
                        new_token = ""
                
                if(")" in possible_answers):
                        result += [["Se reconoce el operador de fin de agrupación: ","%s"%text[i]]]
                        new_token = ""
                    
                if("=" in possible_answers):
                    if(text[i-1] != "+" and text[i-1] != "=" and text[i-1] != "<" and text[i-1] != ">"):
                        if(text[i+1] != "="):
                            result += [["Se reconoce el operador de asignacion: ","%s"%text[i]]]
                            new_token = ""
                        else:
                            new_token = new_token + text[i]
                    elif(text[i-1] == "="):
                        result += [["Se reconoce el operador de comparación: ","%s"%text[i] + text[i-1]]]
                        new_token = ""
                    elif(text[i-1] == "<"):
                        result += [["Se reconoce el operador de comparación: ","%s"%text[i] + text[i-1]]]
                        new_token = ""
                    elif(text[i-1] == ">"):
                        result += [["Se reconoce el operador de comparación: ","%s"%text[i] + text[i-1]]]
                        new_token = ""
                    elif(text[i-1] == "+"):
                        result += [["Se reconoce el operador de acumulación: ","%s"%text[i] + text[i-1]]]
                        new_token = ""

                if("+" in possible_answers):
                    if(text[i-1] != "+"):
                        if(text[i+1] != "=" and text[i+1] != "+" ):
                            result += [["Se reconoce el operador de suma: ","%s"%text[i]]]
                            new_token = ""
                        else:
                            new_token = new_token + text[i]
                    else:
                        result += [["Se reconoce el operador de acumulación: ","%s"%text[i]+text[i-1]]]

                if("-" in possible_answers):
                    result += [["Se reconoce el operador de resta: ","%s"%text[i]]]
                    new_token = ""

                if("/" in possible_answers):
                    result += [["Se reconoce el operador de división: ","%s"%text[i]]]
                    new_token = ""

                if("*" in possible_answers):
                    result += [["Se reconoce el operador de multiplicación: ","%s"%text[i]]]
                    new_token = ""
                    
                if("\n" in possible_answers):
                    new_token = ""
                    line++

                if(";" in possible_answers):
                    result += [["Se reconoce el operador de fin de instrucción: ","%s"%text[i]]]
                    new_token = ""

                if(" " in possible_answers or "\t" in possible_answers or "\n" in possible_answers):
                    new_token = ""
                    
            else:
                    quit(
                        "Error: \n\tSe ha encontrado un token desconocido en la línea '%d': '%s'\n\n" %(
                            line,token
                        )
                    )
                
            i++
            
        return result

    def filtrate(self, token):
        answers = []

        for brake in self.brakes:
            if(brake == token):
                answers.append(brake)

        for reserve in self.specials:
            if(reserve[char] == token):
                answers.append(reserve)
                
        for char in self.alphabet:
            if(char == token):
                answers.append(char)

        for number in self.numbers:
            if(number == token):
                answers.append(number)

        for symbol in self.symbols:
            if(symbol == token):
                answers.append(symbol)

        return answers 

analize = (Test).read()
print("*"*50) 
print("Analizador Léxico")
print("*"*50)
print ("\t%s\n" % analize.text)
print("El análisis léxico del software es:")
lexicalAnalysis = analize.lexicalAnalysis()
print(tabulate(lexicalAnalysis))