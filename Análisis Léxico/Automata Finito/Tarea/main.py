from Core.LexicalAnalysis import Task 
from tabulate import tabulate
analize = (Task()).read()
print("%s%s%s" % ("-"*20, "Analizador Léxico" , "-"*20))
print("Programa encontrado:")
print ("%s\n" % analize.text)
print("El análisis léxico del software es:")
lexicalAnalysis = analize.lexicalAnalysis()
print(tabulate(lexicalAnalysis))