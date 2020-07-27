# -*- coding:utf-8 -*-

"""
    * Generador de Analizadores Léxicos con Plex
    ! Funciona en Python2.7
    ? Programa de ejemplo para generación de un analizador léxico que comprende
    ? Comentarios, cadenas, operador de suma y concatenación, espacios, tabulados
    ? y saltos de línea
    @author Benedetto
    @date 2020/07/21
    @version 0.1
"""

from plex import *
from tabulate impor tabulate
import sys

class LexicalAnalysis:
    def __init__(self):
        #Cadena de texto 
        stringDouble = Str("\"") + Rep(AnyBut("\"") + Str("\""))
        stringSimple = Str("\'") + Rep(AnyBut("\'") + Str("\'"))

        #Espacios en blanco
        space = Any(" \t\n")
        #Comentarios con {}
        comment = Str("{") + Rep(AnyBut("}")) + Str("}")

        #Operadores 
        assignOp = Str("=")
        sumOp = Str("+")

        self.lexicon = Lexicon([
            (stringDouble, "string")
            (stringSimple, "string")
            (sumOp, "sum/concat operator")
            (assignOp, "assign operator")
            (space | comment, IGNORE)
        ])

    def perse(self):
        lexicon = self.lexicon
        lexicalTable = []

        filename = sys.argv[1:][0]
        f = open(filename, "r")
        scanner = Scanner(lexicon, f, filename)

        while True:
            try:
                token = scanner.read()
                if not token[0]: break
                #Obtener Descripcion y valor 
                desc, val = token
                lexicalTable += [[val, desc]]

            except Exception as e:
                print  ("Lexical Error: %s" % (e))
                f.close()
                return False

        f.close()
        self.lexicalTable = lexicalTable
        return self

parser = (LexicalAnalysis())
if parser.parse():
    print "Análisis Léxico: "
    print tabulate(parser.lexicalTable)