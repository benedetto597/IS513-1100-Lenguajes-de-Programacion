# -*- coding: utf-8 -*-
"""
    ! Reconocimiento de parametros leídos y ejecución
    * Obtiene los parametros leídos junto con el contenido del archivo 
    * Control de errores para lenguaje no reconocido o error sintáctico o semántico en la interpretación.
    * Interpretación exclusiva para lenguaje JavaScript
    * Reconocimiento por grámatica exclusivo para lenguaje Bash y Ruby
    ? Impresión del control de errores con color rojo (ANSI)
    ? Impresión de encabezado en azul y tabla de símbolos en blanco (ANSI)
    ? No hace uso de la extensión del archivo para reconocer el lenguaje de programación en el que esta escrito el código.
    @author Edgar Benedetto
    @author Bryan Gonzáles
    @author David Jácome
    @author Luis Banegas
    @date 2020/08/18
    @version 1.0
"""
from Core.AnalysisLexic import *
from Core.Reader import Reader
from Core.Lark import Lark, Transformer 
from Core.Semantic import *
from Core.Grammar.Grammar  import *
from tabulate import tabulate

class Recognition:
    def __init__(self):
        pass

    def info(self):
        print("\x1b[1;34m"+tabulate([["Intérprete Lenguajes ILANG"]]))
        print("\n\x1b[1;34m"+tabulate([["Edgar Josué Benedetto Godoy","20171033802"],["Luis Alejandro Samuel Banegas","20161002983"],["David Alejandro Jácome Jácome","20161001299"],["Bryan Josué Gonzáles Salgado","20141001209"],["@version","1.0"],["@date","18/08/2020"]], ["@authors","@Número de cuenta"],tablefmt="grid"))
        return self

    def run(self):
        reader = (Reader()).read() 
        whatLanguage,optionTable = reader.option

        if (whatLanguage == 1):
            automata = (Automata(reader)).run()

            parser = Lark(grammarJS ,parser="lalr",transformer = Semantic())
            language = parser.parse

            sample = automata.text 

            if (optionTable == 1):
                print("\n\x1b[1;34m"+tabulate([["Tabla de Símbolos"]]))
                print("\x1b[;0m"+tabulate(automata.tokens, ["Lexem","Token"], tablefmt="fancy_grid", colalign=("center","center",)))

            elif (optionTable == 0):
                print("\n\x1b[1;34m"+tabulate([["Ejecución de código interpretado."]])+"\n")
                try:
                    language(sample)

                except Exception as e:
                    quit("\x1b[;31m"+"\nError inesperado: \n %s"%(e))
               
        else:
            temp = [grammarRb,grammarBash]
            
            for i in range(len(temp)):
                parser = Lark(temp[i],parser="lalr")
                language = parser.parse

                sample = reader.text
                try:
                    language(sample)
                except Exception as e:
                    parser = Lark(temp[1],parser="lalr")
                    language = parser.parse
                    try:
                        language(sample)

                    except Exception as e:
                        parser = Lark(temp[0],parser="lalr")
                        language = parser.parse
                        try:
                            language(sample)
                        except Exception as e:
                           quit("\x1b[;31m"+"\nNo se reconocio el lenguaje\n") 
                        else:
                            print("\n\x1b[1;34m"+"\x1b[1;34m"+tabulate([["Lenguaje detectado"]])+"","\x1b[1;34m"+"\n\nRuby")
                            print("\n\x1b[1;34m"+tabulate([["\tPrograma Leido"]]))
                            print("\n\x1b[;32m"+sample)
                    else:
                        print("\n\x1b[1;34m"+"\x1b[1;34m"+tabulate([["Lenguaje detectado"]])+"","\x1b[1;34m"+"\n\nBash")
                        print("\n\x1b[1;34m"+tabulate([["\tPrograma Leido"]]))
                        print("\n\x1b[;32m"+sample)
                    
