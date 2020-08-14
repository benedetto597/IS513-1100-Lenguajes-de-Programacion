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
        self.temp = {}
        self.arguments = {} # {"nombre de la funcion":{"return": [a], "console.log":""},
        self.countIf = 1
                                        
    def printFun(self, param):
        param = (str(param[0])).strip("\"")
        print("%s"%(param))

    def assingvar(self,name,value): 
        self.variables[name] = value
        #print("%s \n %s" %(name,value))
        
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
       
        self.temp[array[0]] = var
        self.functions[array[0]] = array[1:]
        self.cleanParams(array[1:])
        
        
    @v_args(inline=False) #<nombre>(argumento);
    def showfunction(self,param):
        
        #print((self.arguments,self.functions))
        cont = self.cleanTree(param)
        cont = cont.split(",")
#print(cont)
        #print(self.variables)
        #integrar dinamismo
        #probar caso con string
        if cont[1] in self.variables:
            cont[1] = self.variables[cont[1]]
        else:
            if re.match(r"\d+(\.\d+)?",cont[1]):
                cont[1] = float(cont[1])
            elif re.math(re.match(r"^((\"[^\"]*\"?)*|(\'?[^\']*\')*)$",cont[1])):
                pass
            else:
                quit("\x1b[;31m"+"Error")

        
        params = cont[1:]
        print(params)
        if cont[0] in self.functions:
            if len(params) == len(self.getParamsFunction(cont[0])):
                self.runFunction(cont[0],params)
            else:
                quit("\x1b[;31m"+"Error, Cantidad de parametros ingresada, no valida.")
        else:
            quit("\x1b[;31m"+"Error, Funcion, inexistente.")
        
        

    @v_args(inline=True)
    def cleanParam(self, param):
        param = str(param)
        if (re.match(r"^((\"[^\"]*\"?)*|(\'?[^\']*\')*)$",param)):
            if param2:
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
        return params[count]


    #print console error, solo para strings y numeros.
    def printConsoleError(self,argument):
        if isinstance(argument,int):
            #agregar quit()
            print("\x1b[;31m"+"%s" %(argument))
            return self
        var = (str(argument[0])).strip("\"")
        print("\x1b[;31m"+"%s" %(var))

    #print console error, solo para strings y numeros.
    def printConsoleLog(self, argument):
        if isinstance(argument,int):
            #agregar quit()
            #texto sin efecto.
            print("\x1b[;0m"+"%s" %(argument))
            return self
        var = (str(argument[0])).strip("\"")
        print("\x1b[;0m"+"%s" %(var))

    def runFunction(self,name,params):
        #print(self.functions)
        #print(self.temp)
        print(name)
        var = self.temp[name]
        print(var)
        self.countIf = 1
        self.funcion()
        for i,j in var.items():
            if i == "returntree":
                self.printFun(j)
                #brake
            elif i == "return":
                self.printFun(j)
            elif i == "returntwo":
                self.printFun(j)
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

            elif i == "consoleError":
                self.printConsoleError(j)
                #self.printConsoleError(22)
            elif i == "consoleLog":
                self.printConsoleLog(j)
            elif i == "if":
                if self.countIf == 1:
                    #implementar la otra clase, de operaciones
                    #[n,==,1,{"return":"1"}]
                    self.countIf +=1
                else:
                    #implementar la otra clase, de operaciones
                    
                    cont = self.arguments["if"]
                    self.countIf +=1


                



        print("\n\n")

            #print((i,self.arguments[i]))
            
        #print("corriendo funcion....")
    
    #=========================metodos de la funcion================================

    @v_args(inline=True)    
    def getreturn(self,param):
        va = str(param)
        self.arguments["return"]= [(va)]
        

    def getreturntwo(self,param):
        va = str(param)

        self.arguments["returntwo"]= [va]
        #print(self.arguments)

    def getreturnthre(self,param):
        va = str(param)
        self.arguments["returntree"]= [va]
        #print(self.arguments)

    @v_args(inline=False)    
    def getreturnfunction(self,param):
        #print(param)
        arg = self.cleanTree(param)
        #print(arg)

        #self.arguments["returnFunction"] = arg.split(",")
        #print(self.arguments)
    
#======================resultado recursividad====================
    @v_args(inline=True)    
    def getshowrecursin(self,param,param2):
        pass


    @v_args(inline=True)    
    def getconsole(self,param):
        #pendiente caso numeros.
        var = str(param)
        self.arguments["consoleLog"] = [var]

    @v_args(inline=False)    
    def getif(self,param):
        #{if :[n,==,1,1,],[n,<,1,1]}
        var = self.cleanTree(param)
        var = var.split(",")
        if "if" in self.arguments:
            self.countIf += 1
            name = "if%s"%self.countIf
            self.arguments[name] = var
        else:
            self.arguments["if"] = var
            #print(self.arguments)


  #===========verificacion en caso de inexistencia de variable, verificar en los parametros=============      
    def getconsolevar(self,param): #z
        #tomar en cuenta sobreescritura de metodos.
        var = str(param)
        #print(self.getvar(var))
        if var in self.variables:
            var = str(self.getvar(var))
            self.arguments["consoleLogVar"] = [var]
        else:  
            self.arguments["consoleLogVar"] = [var]
        

    def getconsoleerror(self,param):
        var = str(param)
        if self.getvar(var):
            var = str(self.getvar(var))
            self.arguments["consoleError"] = [var]
        else:  
            self.arguments["consoleError"] = [var]
    #================================================================================
       
    @v_args(inline=False)    
    def coment(self,param):
        pass
        
        


   

    
   
  
