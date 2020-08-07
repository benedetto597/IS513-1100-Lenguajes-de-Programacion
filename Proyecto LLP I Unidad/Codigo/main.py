# -*- coding: utf-8 -*-

from Core.AnalysisLexic import *
from Core.Reader import Reader
from Core.lark import *
from Core.Semantic import Semantic
from Core.Grammar.Grammar  import *
from tabulate import tabulate

reader = (Reader()).read()
whatLanguage,optionTable = reader.option

if (whatLanguage == 1):

    automata = (Automata(reader)).run()
    #-------------------
    # #reader = (reader()).read()

    parser = Lark(grammarJS,parser="lalr",transformer=Semantic())
    language = parser.parse

    sample = automata.text  
    
    if (optionTable == 1):
       print(tabulate(automata.tokens, ["Token","Lexem"], tablefmt="fancy_grid", colalign=("center","center",)))
    else:
        pass
        #print("Nos salio Profe....")
        #print(automata.text)
    try:
        language(sample)
    except Exception as e:
        quit("Error: %s"%e) 


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
       quit("Error: %s"%e) 

    #print("Nos salio Profe....")
    #print(reader.text)
