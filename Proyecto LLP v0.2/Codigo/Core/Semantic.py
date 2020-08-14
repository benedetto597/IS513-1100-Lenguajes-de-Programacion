#-*- coding:utf-8 -*-
import re
from Core.Lark import Transformer, v_args

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

    #@v_args(inline=False)
    def assignfunc(self,name,param,argum):
        if isinstance(param,list):
            pass
        else:
            


    """
    def assignfunc(self,name,param,argum):
        if isinstance(param,list):
            pass
        else:
            value = self.getvar(name)
            self.assignvar(param,value)
        
        return argum
    """
            
    def getvalue(self,value):
        return value

    def assignfunction(self,fun,arg):
        self.assignvar(fun,arg)     

    def gettrue(self):
        return True

    def gettrue(self):
        return False

    def getfunction(self,A):
        
        if isinstance(A, str):
            return A
        elif A == True:
            #re.match(r"true",A)
            return True
        elif A == False:
            return False
        elif isinstance(A, int) or isinstance(A, float):
            return A
        else:
            v = self.getvar(A)
            if v:
                return self.cleanParam(v)
            else:
                quit("No Existe la Variable %s" %(A)) 

    def mulfunction(self,A,B):
        pass

    def divfunction(self,A,B):
        pass

    def sumsfunction(self,A,B):
        pass
    
    def subfunction(self,A,B):
        pass

    def compare(self,A,B):
        if A == B:
            return True
        return False
    
    def diferent(self,A,B):
        if A != B:
            return True
        return False

    def greaterequal(self,A,B):
        if A >= B:
            return True
        return False
    
    def lesserequal(self,A,B):
        if A <= B:
            return True
        return False

    def greater(self,A,B):
        if A > B:
            return True
        return False

    def lesser(self,A,B):
        if A < B:
            return True
        return False
            
    def assignifelse(self,A,B,C):
        if A:
            print(B)
           
        else:
            print(C)
        
    def assignif(self,A,B):
        if A:
            return B
    
    
    def assignvar(self,name,value):
        self.variables[name] = value
        
    def getvar(self,name):
        return self.variables[name]

    def printvar(self,name=None):
        if not name:
            pass
        else:
            for  i in self.variables:
                if i == name:
                    print("\x1b[;32m"+"%s " %self.cleanParam(self.getvar(name)))
                    return self
            print("\x1b[;32m"+"%s"%(self.cleanParam(name)))

    def printerror(self,name=None):
        if not name:
            pass
        else:
            for  i in self.variables:
                if i == name:
                    print("\x1b[;31m"+"%s " %self.cleanParam(self.getvar(name)))
                    return self
            print("\x1b[;31m"+"%s"%(self.cleanParam(name)))

    def cleanParam(self, param,param2 = None):
        param = str(param)
        if (re.match(r"^((\"[^\"]*\"?)*|(\'?[^\']*\')*)$",param)):
            if param2:
                return param[2:-2]
            else:    
                return param[1:-1]
        return param

    
    @v_args(inline=False)
    def printconcatenate(self,toConcatenate):
        result = ""
        count = 2
        toConcatenate = str(toConcatenate[0]).split(",")
        for i in range(len(toConcatenate)):
            if i == len(toConcatenate)-1:
                result += (str(self.cleanParam((str(toConcatenate[i]).strip(")]")),True))).strip('"')
            if(i == count):
                #print("\n"+str(toConcatenate[i]))
                result += (str(self.cleanParam((str(toConcatenate[i]).strip(")]")),True))).strip('"') + " "
                count += 3
        print("\x1b[;32m"+result)
