#-*- coding:utf-8 -*-
import re
from lark import Transformer, v_args

@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self): 
        self.variables = {}
    def mul(self,A,B):
        return float(A) * float(B)

    def div(self,A,B):
        return float(A) / float(B)

    def sum(self,A,B):
        return float(A) + float(B)
    
    def sub(self,A,B):
        return float(A) - float(B)

    def mulfunction(self,A,B):
        pass

    def divfunction(self,A,B):
        pass

    def sumsfunction(self,A,B):
        pass
    
    def subfunction(self,A,B):
        pass
    
    
    def assignvar(self,name,value):
        self.variables[name] = value
        
    def getvar(self,name):
        return self.variables[name]

    def printvar(self,name):
        print("%s " %self.cleanParam(self.getvar(name)))
    
    def cleanParam(self, param):
        param = str(param)
        if (re.match(r"^((\"[^\"]*\"?)*|(\'?[^\']*\')*)$",param)):
            return param[1:-1]
        return param
