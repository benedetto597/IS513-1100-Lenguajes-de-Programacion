# -*- coding:utf-8 -*-
form plex import *
import sys 

#[a-zA-Z]
letter = Range("AZaz")

#[0-9] o \d
digit =  Range("09")

# \s
space = Any(" \t\n")

#Lexicon esta basado en una lista de tuplas
lexicon = Lexicon([
    (letter, "Letter"),
    (digit, "Digit"),
    (space, IGNORE)
])

fileName = sys.argv[1:][0]
f = open(fileName, "r")

scanner = Scanner(lexicon, f, fileName)

#Leer ilimitadamente el escaner hasta encontrar un error
while True:
    try: 
        token = scanner.read()
        #En python 2 no se necesita parentesis en print
        print token
        if (token[0] is None):
            break
    #Exception generico
    except Exception as e:
        print "Lexical Error: %s" %e
        break
