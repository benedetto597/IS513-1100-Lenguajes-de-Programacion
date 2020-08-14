# -*- coding: utf-8 -*-

from Core.AnalysisLexic import *
from Core.Reader import Reader
from Core.Lark import Lark, Transformer 
from Core.Grammar.Grammar  import *
#from Core.Grammar.GrammarEjemplo import *
from tabulate import tabulate
from Core.Semantic import *

reader = (Reader()).read()

whatLanguage,optionTable = reader.option



if (whatLanguage == 1):
    automata = (Automata(reader)).run()
    #-------------------
    # #reader = (reader()).read()

    
    sample = automata.text 
    parser = Lark(grammarJS ,parser="lalr",transformer = Semantic())

    language = parser.parse
    try:
        language(sample)

    except Exception as e:
        quit("\x1b[;31m"+"\nError sintactico: \n %s"%e) 
    

    if (optionTable == 1):
        print(tabulate(automata.tokens, ["Token","Lexem"], tablefmt="fancy_grid", colalign=("center","center",)))
    else:
        pass
        #print("Nos salio Profe...."+sample)
       
        

else:
    if reader.ext == "rb":
        gr = grammarRb
    else:
        gr = grammarSh

    parser = Lark(gr,parser="lalr", transformer = Semantic())
    language = parser.parse

    sample = reader.text    

    try:
        language(sample)

    except Exception as e:
        print("Error: %s"%e) 

    #print("Nos salio Profe....")
    #print(reader.text)