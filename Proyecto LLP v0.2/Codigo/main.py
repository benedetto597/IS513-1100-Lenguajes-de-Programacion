# -*- coding: utf-8 -*-

from Core.Reader import Reader
from Core.Lark import Lark, Transformer 
from Core.Grammar.Grammar  import *
from tabulate import tabulate
from Core.SemanticTwo import *

reader = (Reader()).read() 

parser = Lark(grammarBash ,parser="lalr")
language = parser.parse
sample = reader.text

try:
    language(sample)
    print("It works")

except Exception as e:
    quit("\x1b[;31m"+"\nError sintactico: \n %s"%e) 

