from tabulate import tabulate
import sys,re

class SemanticAnalysis:

    def __init__(self): pass

    def help(self):
        print("")
        print("*"*80)
        print("*"*80) 
        print("\tSemantic Analysis (Analizador Semantico Demostrativo)")
        print("""
        \tPermite el reconocimiento de distintos aignificados de instrucción
        \t@author Benedetto
        \t@date 2020/07/13
        \t@version 1.0
        """)
        print("*"*80)
        print("*"*80)

    def clean(self, text):
        return ("%s".strip() % text).strip()

    def read(self):
        self.text = input()
        self.commands = re.split(r";",self.text)[0]
        return self

    #Convierte el json de la informacion en un arreglo para usar el 'tabulate'.
    def jsonToMatrix(self, json):
        result = []
        header = []
        count = 0

        for k,v in json.items():
            row = [k]
            for k1,v1 in v.items():
                count += 1
                #Se crea el encabezado usando lo que tiene el value del priimer key
                if count < 3:
                    header += [self.clean(k1)]
                row += [v1]
            
            result += [row]     
        print([["Name"]+header] + [["-"*5,"-"*5,"-"*5]] + result)
        return [["Name"]+header] + [["-"*5,"-"*5,"-"*5]] + result

    #Divide la las instrucciones diviendo lado izquierdo por derecho para obtener la variable y el valor.
    def splitInstruction(self, line):
        var,val = re.split(r"=", line)
        var = self.clean(var)
        val = self.clean(val)
        return (var,val)

    #Separa por fin de linea el contenido para poder extraer los datos deseados.
    def UDV(self):
        #User Defined Variables
        result = {}

        text = self.text
        #Separar instrucciones
        lines = re.split(r";", text)

        #Recorrer las instrucciones
        for i in range(len(lines)):

            line = self.clean(lines[i])
            
            if(i == 0): continue

            if len(lines[i])>0:
                #Identificando entero asignado a una variable.
                if re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*\d+$", line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":"int","value":val}
                
                #Identificando coma flotante asignado a una variable.
                elif re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*\d+(\.\d+)?$", line):
                    var,val = self.splitInstruction(line)
                    result[var] = {"type":"float","value":val}
                                
                #Identificando asignación de variable
                elif re.match(r"^[a-zA-Z][a-zA-Z\d_]*\s*=\s*[a-zA-Z][a-zA-Z\d_]*$", line):
                    var,val = self.splitInstruction(line)
                    variables = result.keys()
                    if val not in variables:
                        quit("Error semantico: no existe la variable o asignacion '%s'." % val)    
                    
                    result[var] = {"type":result[val]["type"],"value":val}


                else:
                    quit("Error semantico: no se ha encontrado la defincion '%s'" % line)    
        
        return result


#main
parser = (SemanticAnalysis()).read()
#User define variables
# ? Solo entiende instrucciones de asignacion a variables
UDV = parser.UDV()
print(tabulate(parser.jsonToMatrix(UDV)))

"""
    if(parser.commands.find("--verbose") != -1):
        print(parser.commands.find("--verbose"))
        print(tabulate(parser.jsonToMatrix(UDV)))
    else:
        print("El programa se ejecuto con exito!")
"""