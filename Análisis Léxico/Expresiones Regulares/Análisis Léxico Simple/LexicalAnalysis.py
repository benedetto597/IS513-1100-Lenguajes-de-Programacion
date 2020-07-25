
# -*- coding: utf-8 -*-
"""
    !Informal Token Reader (Analizador Léxico Informal Demostrativo)
    *Permite el reconocimiento de distintos tokes usando expresiones regulares para un lenguajes de
    múltiples instrucciones por línea de código. Este programa no posee lexema de palabras especiales,
    en su lugar, reconocerá identificadores de usuario, valores númericos, cadenas, fin de instrucción y
    saltos de línea.
    *Esta implementación no aplica el uso de "automatas finitos", lo que hacer la implementación sea
    completamente demostrativa.
    *Es por ello que esta demostración representa un ejemplo informal para realizar el proceso de
    detección de tokens, sobre el cual se hacen mención de aspectos especificos de la teoría pero no se
    aplican en completitud las prácticas obligatorias de la literatura, para encajar en una demostración
    dentro de la hora clase.
    ?Comprende la lógica general de la demostración
    ?Comprende identificadores de usuario
    ?Comprende operador de asignación
    ?Comprende valores númericos entero y flotante.
    ?Requiere fin de instrucción
    ?No comprende sintñaxis, ni precedencia, ni comentarios, ni operadores, ni cadenas, etc.
    ?El resultado de un programa real deberá ser el pipeline que alimenta al análisis sintáctico
    @author Izaguirre
    @date 2020/07/05
    @version 0.1
"""

#sudo -H pip3 install tabulate
from tabulate import tabulate
import sys, re

class InformalTokenParser:

    def __init__(self): pass

    def help(self):

        print("")
        print("*"*80)
        print("*"*80) 
        print("\tInformal Token Reader (Analizador Léxico Informal Demostrativo) ")
        print("""
        \tPermite el reconocimiento de distintos tokes usando expresiones 
        \tregulares para un lenguajes de múltiples instrucciones por línea de código. 
        \tEste programa no posee lexema de palabras especiales, en su lugar, 
        \treconocerá identificadores de usuario, valores númericos, cadenas, 
        \tfin de instrucción y saltos de línea
        """)
        print("*"*80)
        print("*"*80)

    def read(self):
        #python3 lexicalAnalysis.py sample1.lng
        param = sys.argv[1:]

        if len(param) != 1: quit("Error. No se ha definido un programa a ejecutar.")

        self.fileName = param[0]
        f = open(self.fileName,"r")
        self.text = f.read() #Lee la completidud del programa
        f.close()

        return self

    def preprocess(self):

        text = self.text
        text = re.sub(r"="," = ", text)
        text = re.sub(r";"," ; ", text)
        text = re.sub(r"\s+"," ", text)
        self.text = ("%s".strip() % text).strip()

        return self

    def lexicalAnalysis(self):
        result = []
        text = self.text

        tokens = re.split(r"\s",text)

        for token in tokens:

            token = ("%s".strip() % token).strip()
            if len(token) > 0:

                #Es un identificador de usuario
                if re.match(r"^[a-zA-Z][a-zA-Z0-9\_\-]*$",token):
                    result += [["Se reconoce el identificador de usuario: ","%s"%token]]

                #Es un operador de asignación
                elif re.match(r"^=$",token):
                    result += [["Se reconoce el operador de asignación: ","%s"%token]]

                #Es un número flotante
                elif re.match(r"^\d+\.\d+$",token):
                    result += [["Se reconoce el número flotante: ","%s"%token]]

                #Es un número entero
                elif re.match(r"^\d+$",token):
                    result += [["Se reconoce el número entero: ","%s"%token]]

                #Es un fin de instrucción
                elif re.match(r"^;$",token):
                    result += [["Se reconoce el fin de instrucción: ","%s"%token]]

                #Es un token desconcido
                else:
                    quit(
                        "Error: \n\tSe ha encontrado un token desconocido en la línea '%d': '%s'\n\n" %(
                            self.searchTokenLine(token),
                            token
                        )
                    )
        return result


    def searchTokenLine(self, token):

        errorLine = 0

        f = open(self.fileName, "r")

        for line in f:
            errorLine += 1
            
            if re.match(r"^.*%s.*$" % self.prevent(token), line):
                break

        f.close()

        return errorLine

    def prevent(self, token):

        if re.match(r"[\+\*\.\(\)\{\}\[\]]+",token):
            return "\\\\%s" % token
        return token

parser = (InformalTokenParser()).read().preprocess()
parser.help()

print("Programa encontrado:")
print ("\t%s\n" % parser.text)

lexicalAnalysis = parser.lexicalAnalysis()
print("El análisis léxico del software es:")
print(tabulate(lexicalAnalysis))