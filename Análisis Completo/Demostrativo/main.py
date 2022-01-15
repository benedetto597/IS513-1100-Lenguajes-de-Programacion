# -*- coding:utf-8 -*-

import sys
from LexicalAnalysis import InformalTokenParser
from semanticAnalysis import SemanticAnalysis
from syntaxAnalysis import SyntaxAnalysis 

parser = (InformalTokenParser()).read().preprocess()

try: 
    lexicalAnalysis = parser.lexicalAnalysis()
    if(len(lexicalAnalysis) >0):
        print ("%s" % parser.text)
except Exception as e:
    print("Error: %s" % e)
