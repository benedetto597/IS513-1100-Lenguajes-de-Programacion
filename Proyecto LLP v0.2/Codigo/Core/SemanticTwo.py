#-*- coding:utf-8 -*-
import re
from Core.Lark import Transformer, v_args

"""
1. Guardar datos de la funcion(nombre,parametros).
2. Analizar mediante reglas gramaticales, las diferentes reglas, o metodos que conforman dicha funcion.
3. Una vez, Guardar cada metodo que contenga dicha funcion en un diccionario.
4. Al realizarce un llamado, existe un control de errores(nombre,parametros).
5. Realizar llamado a la funcion(tomandola como si fuera void).
6. Recursividad.(implementar ejemplo).
7. Optimizar para manejar n cantidad de funciones.
"""

@v_args(inline=True)
class Semantic(Transformer):
    def __init__(self): 
        self.variables = {}
        self.functions = {} # {"nombre de la funcion": [a,b,c,d]}
        self.tempSentence = {}
        self.tempSentence2 = {}
        self.arguments = {} # {"nombre de la funcion":{"return": [a], "console.log":""},
        self.countIf = 1
        self.logicOp = []
        self.startUp = False
                                        
    def printFun(self, param):
        #param = (str(param[0])).strip("\"")
        print("%s"%(param))

    def assingvar(self,name,value): 
        self.variables[name] = value
        #print("%s \n %s" %(name,value))
    
    def getreserve(self):
        pass

    def getother(self):
        pass
    
    def savevar(self,name,value):
        self.arguments["assign"] = [str(name),str(value)]
        
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


    @v_args(inline=False)
    def addfunction(self,param):
        cont = self.cleanTree(param)
        array = cont.split(",")  
        var = self.arguments
        self.arguments = {}
       
        self.tempSentence[array[0]] = var
        self.functions[array[0]] = array[1:]
        self.cleanParams(array[1:])
        
    @v_args(inline=False)
    def getrecursive(self,params):
        #{"factorial":["n","-","1"]}
        cont = self.cleanTree(params)
        cont = cont.split(",")
 
        params = cont[1:]
        self.tempSentence2[cont[0]] = params
        #print(self.tempSentence2)


    @v_args(inline=False) #<nombre>(argumento);
    def showfunction(self,param):
        
        #print((self.arguments,self.functions))
        cont = self.cleanTree(param)
        cont = cont.split(",")
        #print(self.variables)
        #integrar dinamismo
        #probar caso con string
        if cont[1] in self.variables:
            cont[1] = self.variables[cont[1]]
        else:
            if re.match(r"\d+(\.\d+)?",cont[1]):
                cont[1] = float(cont[1])
            elif re.match(r"^((\"[^\"]*\"?)*|(\'?[^\']*\')*)$",cont[1]):
                pass
            else:
                quit("\x1b[;31m"+"Error")

        
        params = cont[1:]

        if cont[0] in self.functions:
            if len(params) == len(self.getParamsFunction(cont[0])):
                return self.runFunction(cont[0],params)
            else:
                quit("\x1b[;31m"+"Error, Cantidad de parametros ingresada, no valida.")
        else:
            quit("\x1b[;31m"+"Error, Funcion, inexistente.")
        
        

    @v_args(inline=True)
    def cleanParam(self, param):
        param = str(param)
        if (re.match(r"^((\"[^\"]*\"?)*|(\'?[^\']*\')*)$",param)):
            if param:
                return param[2:-2]
            else:    
                return param[1:-1]
        return param

    def cleanTree(self,tree):
        cont = ""
        #print("\n"+str(len(tree)))
        for i in range(len(tree)):
            #print(i)
            if tree[i] == None:
                continue
            if i == len(tree):
                cont = cont +str(tree[i])
            else:
                cont = cont +str(tree[i])+","
        return cont[0:-1]
    
    def getParamsFunction(self,name):
        return self.functions[name]

    def cleanParams(self,params):
        for i in range(len(params)):
            if params[i] in params[i+1:]:
                quit("\x1b[;31m"+"Error Parametro(s) repetidos.")
    
    #devuelve posicion dinamica de la variable declarada en la funcion.
    def posicionTree(self,name,argument,params):
        var = self.functions[name] 
        #print((var,argument))
        count = None 
        for i in range(len(var)):
            if var[i] == argument:
                count = i
        #print((params,count))
        return float(params[count])


    #print console error, solo para strings y numeros.
    def printConsoleError(self,argument):
        if isinstance(argument,int):
            #agregar quit()
            print("\x1b[;31m"+"%s" %(argument))
            return self
        print(argument)
        #var = (str(argument[0])).strip("\"")
        #print("\x1b[;31m"+"%s" %(var))

    #print console error, solo para strings y numeros.
    def printConsoleLog(self, argument):
        if isinstance(argument,int):
            #agregar quit()
            #texto sin efecto.
            print("\x1b[;0m"+"%s" %(argument))
            return self
        print(argument)
        #var = (str(argument[0])).strip("\"")
        #print("\x1b[;0m"+"%s" %(var))

    def runFunction(self,name,params):
        #print(self.functions)

        var = self.tempSentence[name]
        print(var)
        self.countIf = 1
        a,b = self.run(var,params,name)
        if a:
            #print(b)
            return b

        #print("\n\n")

    def logicalOperator(self,array,name,params,num = None):
        #array[-1]
        exc = array[2]
        if num == None:
            pos = self.posicionTree(name,array[0],params)
        else:
            pos = float(num)

        if re.match(r"[a-z]\w*",array[2]):
            exc = self.posicionTree(name,array[2],params)
        #print((float(array[2]),pos))
        if (array[1] == "=="):
            if pos == float(exc):
                return True
            else:
                return False
        if (array[1] == "!="):
            if pos != float(exc):
                return True
            else:
                return False
        elif (array[1] == "<"):
            if pos < float(exc):
                return True
            else:
                return False
        elif (array[1] == "-"):
            value = pos - float(exc)
            return value

    def run(self,var,params,name):
        for i,j in var.items():
            if i == "returntree":
                self.printFun(j)
                #brake
            elif i == "return":
                #self.printFun(j)
                return (True,float(j))
            elif i == "returntwo":
                self.printFun(j)
            elif i == "break":
                    return (False,j)
            elif i == "recursive":
                #["n","*",{"factorial":["n","-","1"]}]
                value = self.posicionTree(name,j[0],params)
                json = j[-1]

                a,b = list(json.keys()),list(json.values())
                op = self.logicalOperator(b[0],name,params)
                v = self.runFunction(a[0],[op])
                # hacer generica la operacion aritmetica
                value = value*v              
                return (True,value)

            elif i == "consoleLogVar":
                var = self.functions[name]  #[a,b,a]
                arr = j #bryan
                #print((var,arr[0])) #bryan
                if arr[0] in var:
                    temp = j
                    value = self.posicionTree(name,temp[0],params)
                    print(value)
                else:
                    self.printConsoleLog(j)

            elif (i.find("consoleError")>=0):
                
                self.printConsoleError(j)
                #self.printConsoleError(22)
            elif (i.find("consoleLog") >=0):
                self.printConsoleLog(j)
            
            elif (i.find("while") >= 0):
                #['n', '!=', 'm', {'consoleError': '"Bye!"','break':'break'}]
                json = j[-1]
                
                if self.logicalOperator(j,name,params):
                    a,b = self.run(json,params,name)
                    if a:
                        return (True,b)
                    if b == "break":
                        pass
                    else:
                        jsonWhile = {}
                        jsonWhile["while"] = j
                        a,b = self.run(jsonWhile,params,name)
                        if a:
                            return (True,b)


            elif (i.find("for") >= 0):
                json = j[-1]
                array = j[-2]
                num = int(j[0])
                op = self.logicalOperator(array,name,params,num)
                current = True
                if op:
                    a,b = self.run(json,params,name)
                    if a:
                        return (True,b)
                    if b == "break":
                        current = False
                if current and op:
                    if j[1] == "++":
                        num += 1
                    elif j[1] == "--":
                        num -= 1
                    jsonFor = {}
                    jsonFor["for"] = [num,j[1],array,json]
                    a,b = self.run(jsonFor,params,name)
                    if a:
                        return (True,b)

                

                        
            elif (i.find("ifelse") >= 0):
                jsonIf = j[-2]
                jsonEl = j[-1]
                if self.logicalOperator(j,name,params):
                    a,b = self.run(jsonIf,params,name)
                    if a:
                        return (True,b)
                else:
                    a,b = self.run(jsonEl,params,name)
                    if a:
                        return (True,b)

            elif (i.find("if") >= 0):

                json = j[-1]
                if self.logicalOperator(j,name,params):
                    a,b = self.run(json,params,name)
                    if a:
                        return (True,b)
                    #print((array,json))
                
                
                    
        return (False,None)
    
    #=========================metodos de la funcion================================

    @v_args(inline=True)    
    def getreturn(self,param):
        va = str(param)
        
        self.tempSentence2["return"] = va
        #print(self.tempSentence2)
        #self.arguments["return"]= [(va)]
        

    def getreturntwo(self,param):
        va = str(param)
        
        self.tempSentence2["returntwo"] = va
       # self.arguments["returntwo"]= [va]
        
        #print(self.arguments)

    def getreturnthre(self,param):
        va = str(param)
        
        self.tempSentence2["returntree"] = va
        #self.arguments["returntree"]= [va]
        #print(self.arguments)

    @v_args(inline=False)    
    def getreturnfunction(self,param):
        #["n","*",{"factorial":["n","-","1"]}]
        arg = self.cleanTree(param)
        arg = arg.split(",")
        #print((arg,self.tempSentence2))       
        arg.append(self.tempSentence2)
        self.tempSentence2 = {}
        self.arguments["recursive"] = arg

        #self.arguments["returnFunction"] = arg.split(",")
        #print(self.arguments)
    
#======================resultado recursividad====================
    @v_args(inline=False)    
    def ifelse(self,param):
        var = (self.cleanTree(param)).split(",")

        json = self.tempSentence2
        #a = list(self.tempSentence2.keys())
        var.append(json)
        self.tempSentence2 = {}
        self.startUp = True
        self.arguments["ifelse"] = var
    
   
    @v_args(inline=False)    
    def getelse(self,param):
        #var = (self.cleanTree(param)).split(",")
        json = self.tempSentence2
        if self.startUp:
            array = self.arguments["ifelse"]
            array.append(json)
            self.tempSentence2 = {}
            self.arguments["ifelse"] = array


    @v_args(inline=True)    
    def getconsole(self,param):
        #pendiente caso numeros.
        var = str(param)
        if "consoleLog" in self.tempSentence2:
            self.countIf += 1
            name = "consoleLog%s"%self.countIf
            self.tempSentence2[name] = var
        else:
            self.tempSentence2["consoleLog"] = var
        #self.arguments["consoleLog"] = [var]

    @v_args(inline=False)    
    def getif(self,param):
 
        var = (self.cleanTree(param)).split(",")
        #print(var,"///")

        a = list(self.tempSentence2.keys())
        if "if" in self.arguments:
            self.countIf += 1
            name = "if%s"%self.countIf  
            if not(a == []):
                var.append(self.tempSentence2)
                self.tempSentence2 = {}
                self.arguments[name] = var  
        elif not(a == []):
            var.append(self.tempSentence2)
            self.tempSentence2 = {}
            self.arguments["if"] = var




  #===========verificacion en caso de inexistencia de variable, verificar en los parametros=============      
    def getconsolevar(self,param): #z
        #tomar en cuenta sobreescritura de metodos.
        var = str(param)
        if "consoleLogVar" in self.tempSentence2:
            self.countIf += 1
            name = "consoleLogVar%s"%self.countIf
            self.tempSentence2[name] = var
        else:
            self.tempSentence2["consoleLogVar"] = var
        #print(self.getvar(var))
        #if var in self.tempSentence2:
        #    #var = str(self.getvar(var))
        #    self.tempSentence2["consoleLogVar"] = var
        #else:  
        #    self.tempSentence2["consoleLogVar"] = var
        

    def getconsoleerror(self,param):
        var = str(param)
        #if self.getvar(var):
        #    var = str(self.getvar(var))
        #    self.tempSentence2["consoleError"] = [var]
        #else:
        #print("////",var)  
        if "consoleError" in self.tempSentence2:
            self.countIf += 1
            name = "consoleError%s"%self.countIf
            self.tempSentence2[name] = var
        else:
            self.tempSentence2["consoleError"] = var
    #================================================================================
       
    @v_args(inline=False)    
    def getcon(self,param):

        var = (self.cleanTree(param)).split(",")
        var = " ".join(var)
        print(var)
        
        
    @v_args(inline=False)    
    def getwhile(self,param):

        #var.append(self.tempSentence2)
        var = self.logicOp
        #var.append(self.tempSentence2)
        self.logicOp = []
        #self.tempSentence2 = {}
        #self.arguments["while"] = var

        a = list(self.tempSentence2.keys())
        if "while" in self.arguments:
            self.countIf += 1
            name = "while%s"%self.countIf  
            if not(a == []):
                var.append(self.tempSentence2)
                #self.logicOp = []
                self.tempSentence2 = {}
                self.arguments[name] = var  
        elif not(a == []):
            var.append(self.tempSentence2)
            #self.logicOp = []
            self.tempSentence2 = {}
            self.arguments["while"] = var


    @v_args(inline=False)    
    def logicoperation(self,params):
        var = (self.cleanTree(params)).split(",")
        self.logicOp = var

    @v_args(inline=True)    
    def getcomant(self,param):
        self.tempSentence2["break"] = "break"

    @v_args(inline=False)  
    def getfor(self,param):
        var = (self.cleanTree(param)).split(",")
        op = self.logicOp
        if ((var[0] in op) and (var[0] == var[2])):
            array = [var[1],var[3]]
            array.append(op)
            self.logicOp = []

            a = list(self.tempSentence2.keys())
            if "for" in self.arguments:
                self.countIf += 1
                name = "for%s"%self.countIf  
                if not(a == []):
                    array.append(self.tempSentence2)
                    #self.logicOp = []
                    self.tempSentence2 = {}
                    self.arguments[name] = array  
            elif not(a == []):
                array.append(self.tempSentence2)
                #self.logicOp = []
                self.tempSentence2 = {}
                self.arguments["for"] = array
        else:
            print("MALO ")

    @v_args(inline=False)  
    def coment(self,param):
        pass

    
