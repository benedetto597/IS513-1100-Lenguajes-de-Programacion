# -*- coding:utf-8 -*-
from Reader import Reader
from Automata import Automata

reader = (Reader()).read().run()
#Procesar reader con un autómata
automata = (Automata(reader)).run()

print("\n\nResultados")
for token in automata.tokens:
    #Obtener el valor y tipo de valor del token
    value, valueType = token.info()
    print("\t%s - %s" % (value,valueType))