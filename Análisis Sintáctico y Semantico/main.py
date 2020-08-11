# -*- coding:utf-8 -*-

import sys
from Reader import Reader
from Semantic import Semantic
from lark import Lark, Transformer 
from Grammar import *

reader = (Reader()).read()
parser = Lark(grammar,parser="lalr", transformer = Semantic())
lenguaje = parser.parser

sample = reader.text

try: 
    lenguaje(sample)
except Exception as e:
    print("Error: %s" % e)
