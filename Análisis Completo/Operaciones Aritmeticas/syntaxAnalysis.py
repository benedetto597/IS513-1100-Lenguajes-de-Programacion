# -*- coding: utf-8 -*-
"""
    ! Sintax Analysis (AnalizadorSintáctico de operaciones Aritmeticas)
    ! Non-CFG
    * Permite el reconocimiento de distintos tokens en el orden
    * correcto de instrucciones
    ? Comprende la asignación de operaciones aritméticas
    ? a una variable cualquiera
    ? comrepden operador de asignación.
    ? Comprende valores númericos enteros y coma flotante.
    ? Requiere fin de instrucción.
    ? Se comunica mediante pipeline.
    @author Benedetto
    @date 2020/07/30
    @version 1.0
"""

import re

class SyntaxAnalysis:
    pass

    def __init__(self):pass

    def help(self):
        print("")
        print("*"*80)
        print("*"*80) 
        print("\tSintax Analysis (Analizador Sintáctico de operaciones Aritmeticas a una variable cualquier)")
        print("""
        \tPermite el reconocimiento de distintos tokens en el orden
        \tcorrecto de instrucciones
        \tComprende operaciones Aritmeticas a una variable cualquier
        \t@author Benedetto
        \t@date 2020/07/13
        \t@version 1.0
        """)
        print("*"*80)
        print("*"*80)

    def read(self, text):
        #self.text = input()
        self.text = text
        return self

    def parse(self):
        text = self.text
        lines = re.split(r";",text)

        for i in range(len(lines)):
            line = ("%s".strip() % lines[i]).strip()
            if(len(line) >0):
                if(
                    re.match(r"^[a-zA-Z][a-zA-Z0-9\d_]*\s*=\s*\d+(\.\d+)?$", line) or
                    re.match(r"^[a-zA-Z][a-zA-Z0-9\d_]*\s*=\s*[a-zA-Z][a-zA-Z0-9\d_]*$", line) or 
                    re.match(r"^[a-zA-Z][a-zA-Z0-9\d_]*\s*=\s*((\d+(\.\d+)?|[a-zA-Z][a-zA-Z0-9\d_]*)*(\s*)?(\*|\/|\+|\-|\^)(\s*)?(\d+(\.\d+)?|[a-zA-Z][a-zA-Z0-9\d_]*))*" , line)

                ):
                    pass
                else:
                    quit("Error sintáctico: Se ha encontrado un error en la línea %d" % i)

        return True
"""
parser = (SyntaxAnalysis()).read()

if parser.parse():
    print("%s" % parser.text)
"""