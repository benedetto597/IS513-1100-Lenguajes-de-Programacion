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

class Task:
    def __init__(self): 
        self.numbers = ["0","1","2","3","4","5","6","7","8","9"]
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
                        "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.symbols = [".","+","-","/","*","=","==","(",")","++","+=",";",":","::","<",">","<=",">=","{","}","_","<<",">>",'"',"'"]
        self.brakes = ["\n","\t"," "]
        self.specials = ["return","#include","#define","int","main","namespace","std","cout","cin","float","#endif","#ifndef","class","public","<iostream>"]

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
        head = [["N","Token","Tipo"],["-"*3,"-"*8,"-"*29]]
        result += head
        new_token = ""
        i = 0
        while(i != len(text)):
            possible_answers = self.filtrate(text[i])
            if(len(possible_answers) > 0):
                    
                #Palabras reservadas
                if("#include" in possible_answers or "#endif" in possible_answers or "#ifndef" in possible_answers):
                    if(text[i+1] == "i"):
                        if(text[i+2] == "n"):
                            new_token = "#include"
                            result += [[i,new_token,"Palabra reservada"]]
                            new_token = ""
                            i = i + 8
                            
                        elif(text[i+2] == "f"):
                            new_token = "#ifndef"
                            result += [[i,new_token,"Palabra reservada"]]
                            new_token = ""
                            i = i + 7

                    elif(text[i+1] == "e"):
                        new_token = "#endif"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 6

                if("return" in possible_answers or "int" in possible_answers or "main" in possible_answers or "namespace" in possible_answers or "std" in possible_answers or "cout" in possible_answers or "cin" in possible_answers or "float" in possible_answers or "class" in possible_answers or "public" in possible_answers):
                    if(text[i] == "c"):
                        if(text[i+1] == "o" and text[i+2] == "u" and text[i+3] == "t"):
                            new_token = "cout"
                            result += [[i,new_token,"Palabra reservada"]]
                            new_token = ""
                            i = i + 4
                        if(text[i+1] == "i" and text[i+2] == "n"):
                            new_token = "cin"
                            result += [[i,new_token,"Palabra reservada"]]
                            new_token = ""
                            i = i + 3
                        if(text[i+1] == "l" and text[i+2] == "a" and text[i+3] == "s" and text[i+4] == "s"):
                            new_token = "class"
                            result += [[i,new_token,"Palabra reservada"]]
                            new_token = ""
                            i = i + 5
                    if(text[i] == "r" and text[i+1] == "e" and text[i+2] == "t" and text[i+3] == "u" and text[i+4] == "r" and text[i+5] == "n"):
                        new_token = "return"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 6
                    if(text[i] == "i" and text[i+1] == "n" and text[i+2] == "t"):
                        new_token = "int"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 3
                    if(text[i] == "m" and text[i+1] == "a" and text[i+2] == "i" and text[i+3] == "n"):
                        new_token = "main"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 4
                    if(text[i] == "s" and text[i+1] == "t" and text[i+2] == "d" ):
                        new_token = "std"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 3
                    if(text[i] == "f" and text[i+1] == "l" and text[i+2] == "o" and text[i+3] == "a" and text[i+4] == "t"):
                        new_token = "float"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 5
                    if(text[i] == "p" and text[i+1] == "u" and text[i+2] == "b" and text[i+3] == "l" and text[i+4] == "i" and text[i+5] == "c"):
                        new_token = "public"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 6
                    if(text[i] == "n" and text[i+1] == "a" and text[i+2] == "m" and text[i+3] == "e" and text[i+4] == "i" and text[i+5] == "e"  and text[i+6] == "s"  and text[i+7] == "p" and text[i+8] == "a" and text[i+9] == "c" and text[i+10] == "e"):
                        new_token = "namespace"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 11
                    if(text[i] == "<" and text[i+1] == "i" and text[i+2] == "o" and text[i+3] == "s" and text[i+4] == "t" and text[i+5] == "r"  and text[i+6] == "e"  and text[i+7] == "a" and text[i+8] == "m" and text[i+9] == ">"):
                        new_token = "<iostream>"
                        result += [[i,new_token,"Palabra reservada"]]
                        new_token = ""
                        i = i + 10
                    

                #Identificadores de usuario
                if(text[i] in self.alphabet):
                    for j in range(len(text[i-len(text)])):
                        if(text[i] != " " or text[i] != "\t" or text[i] != "\n" or text[i] != ";" or text[i] != "," or text[i] != "+" or text[i] != "-" or text[i] != "*" or text[i] != "/" or text[i] != "=" or text[i] != "==" or text[i] != "(" or text[i] != ")" or text[i] != "."):
                            new_token = new_token + text[i]
                            i = i + 1
                        result += [[i,new_token,"Identificador de usuario"]]
                    new_token = ""

                #Digitos
                if(text[i] in self.numbers):
                    for j in range(len(text[i-len(text)])):
                        if(text[i] != " " or text[i] != "\t" or text[i] != "\n" or text[i] != ";" or text[i] != "," or text[i] != "+" or text[i] != "-" or text[i] != "*" or text[i] != "/" or text[i] != "=" or text[i] != "==" or text[i] != "(" or text[i] != ")"):
                            new_token = new_token + text[i]
                            i = i + 1
                        if("." in new_token):
                            result += [[i,new_token,"Coma flotante"]]
                        else:
                            result += [[i,new_token,"Entero"]]
                    new_token = ""
                #Simbolos
                if("." in possible_answers):
                    result += [[i,text[i],"Operador de función"]]
                    new_token = ""
                        
                if("'" in possible_answers):
                    result += [[i,text[i],"Comilla simple"]]
                    i = i + 1
                    for k in text[i-len(text)]:
                        if(text[i] != "'"):
                            new_token = new_token + text[i]
                        i = i + 1
                    result += [[i,new_token,"Cadena"]]
                    i = i + 1
                    result += [[i,text[i],"Comilla simple"]]
                    
                    new_token = ""

                if('"' in possible_answers):
                    result += [[i,text[i],"Comilla doble"]]
                    i = i + 1
                    for l in range(len(text[i-len(text)])):
                        if(text[i] != '"'):
                            new_token = new_token + text[i]
                            i = i + 1
                    result += [[i,new_token,"Cadena"]]
                    i = i + 1
                    result += [[i,text[i],"Comilla doble"]]
                    
                    new_token = ""

                if("," in possible_answers):
                    result += [[i,text[i],"Separación"]]
                    new_token = ""

                if("{" in possible_answers):
                    result += [[i,text[i],"Inicio de declaración"]]
                    new_token = ""

                if("}" in possible_answers):
                    result += [[i,text[i],"Fin de declaración"]]
                    new_token = ""

                if(">" in possible_answers):
                    if(text[i-1] in self.alphabet):
                        pass
                    else:
                        if(text[i-1] != ">" ):
                            result += [[i,text[i],"Mayor que"]]
                            new_token = ""
                        else:
                            result += [[i,text[i] + text[i-1],"Desplazamiento a la derecha"]]
                            new_token = ""

                if("<" in possible_answers):
                    if(text[i+1] in self.alphabet):
                        pass
                    else:
                        if(text[i-1] != "<" ):
                            result += [[i,text[i],"Menor que"]]
                            new_token = ""
                        else:
                            result += [[i,text[i] + text[i-1],"Desplazamiento a la izquierda"]]
                            new_token = ""

                if(":" in possible_answers):
                    if(text[i-1] != ":"):
                        result += [[i,text[i],"Asignación de función"]]
                    else:
                        result += [[i,text[i] + text[i-1],"Alcance"]]

                    new_token = ""

                if("(" in possible_answers):
                        result += [[i,text[i],"Inicio de agrupación"]]
                        new_token = ""
                
                if(")" in possible_answers):
                        result += [[i,text[i],"Fin de agrupación"]]
                        new_token = ""
                    
                if("=" in possible_answers):
                    if(text[i-1] != "+" and text[i-1] != "=" and text[i-1] != "<" and text[i-1] != ">"):
                        if(text[i+1] != "="):
                            result += [[i,text[i],"Asignacion"]]
                            new_token = ""
                        else:
                            new_token = new_token + text[i]
                    elif(text[i-1] == "="):
                        result += [[i,text[i] + text[i-1],"Comparación"]]
                        new_token = ""
                    elif(text[i-1] == "<"):
                        result += [[i,text[i] + text[i-1],"Menor igual que"]]
                        new_token = ""
                    elif(text[i-1] == ">"):
                        result += [[i,text[i] + text[i-1],"Mayor igual que"]]
                        new_token = ""
                    elif(text[i-1] == "+"):
                        result += [[i,text[i] + text[i-1],"Acumulación"]]
                        new_token = ""

                if("+" in possible_answers):
                    if(text[i-1] != "+"):
                        if(text[i+1] != "=" and text[i+1] != "+" ):
                            result += [[i,text[i],"Suma"]]
                            new_token = ""
                        else:
                            new_token = new_token + text[i]
                    else:
                        result += [[i,text[i]+text[i-1],"Acumulación"]]

                if("-" in possible_answers):
                    new_token = ""

                if("/" in possible_answers):
                    result += [[i,text[i],"División"]]
                    new_token = ""

                if("*" in possible_answers):
                    result += [[i,text[i],"Multiplicación"]]
                    new_token = ""

                if(";" in possible_answers):
                    result += [[i,text[i],"Fin de instrucción"]]
                    new_token = ""

                if(" " in possible_answers or "\t" in possible_answers or "\n" in possible_answers):
                    new_token = ""
                    
            else:
                    quit(
                        "Error: \n\tSe ha encontrado un token desconocido en la línea '%d': '%s'\n\n" %(
                            self.searchTokenLine(text[i]),
                            text[i]
                        )
                    )
                
            i = i + 1
            
        return result

    def filtrate(self, token):
        answers = []
    
        for brake in self.brakes:
            if(brake == token):
                answers.append(brake)

        for reserve in self.specials:
            if(reserve[0] == token):
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
    
    def searchTokenLine(self, token):

        errorLine = 0

        f = open(self.fileName, "r")

        for line in f:
            errorLine += 1
            for i in range(len(line)):
                if(token in line[i]):
                    break
        f.close()

        return errorLine

