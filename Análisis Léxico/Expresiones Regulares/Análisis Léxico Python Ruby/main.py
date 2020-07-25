# -*- coding:utf-8 -*-
from LexicalAnalysisPythonRuby import TokenParserPythonRuby
parser = (TokenParserPythonRuby()).read().preprocess()
parser.help()

print("Programa encontrado:")
print ("\t%s\n" % parser.text)

lexicalAnalysis = parser.lexicalAnalysis()
print("El análisis léxico del software es:")
print(tabulate(lexicalAnalysis))