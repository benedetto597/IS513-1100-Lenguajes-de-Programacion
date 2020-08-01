#-*- coding:utf-8 -*- 
import sys
class Reader:
    def __init__(self):
        self.param = None
        self.text = ""

    #Agregar parametros --help, --verbose, etc.
    def read(self):

        #python3 lexicalAnalysis.py sample1.lng
        args = sys.argv[1:]

        #Casos particulares 
        if len(args) > 1:
            if(args[0] == "--what-language-is-this"):
                self.
            elif(args[0] == "--symbols-table"):
                pass
            else: 
                quit("Error: Parasmsetro no reconocido")
            
        #Caso general
        if len(args) != 0:
            fileName = args[0]
            f = open(fileName, "r")
            self.text = f.read() #Lee la completitud del programa
            f.close()
        else: 
            quit("Error: N--what-language-is-thiso se ha definido un programa a ejecutar")
            
        return self
