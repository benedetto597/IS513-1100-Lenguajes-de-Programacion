# -*- coding: utf-8 -*-
"""
    ! Lector de parametros por consola y de archivos de texto plano
    * Lectura de los parametros envíados por consola.
    * Lectura del contenido del archivo enviado como parametro.
    * Inplementa control de errores, para archivos no encontrados, parametros faltante y parametros no reconocidos.
    ? Impresión del control de errores con color rojo (ANSI)
    @author Edgar Benedetto
    @author Bryan Gonzáles
    @author David Jácome
    @author Luis Banegas
    @date 2020/08/18
    @version 1.0
"""
import sys

#---------------------------------
#    token          lexema
#  palabra reservada    
# capt 4, pag 4
#---------------------------------
class Reader:
    def __init__(self):
        self.param = None
        self.text = ""
        self.option = (1,0)
        self.ext = None

    def read(self):

        args = sys.argv[1:]

        #Casos particulares 
        if len(args) > 1:
            if(args[0] == "--what-language-is-this"):
                try:
                    fileName = args[1]
                    self.ext = fileName.split(".")[1]

                    f = open(fileName, "r")
                    self.text = f.read() 
                    f.close()
                    self.option = (0,0)
                    return self
                except Exception as e:
                    quit("\x1b[;31m"+"Error el archivo No Existe.")
            elif(args[0] == "--symbols-table"):
                try:   
                    fileName = args[1]
                    f = open(fileName, "r")
                    self.text = f.read()
                    f.close()
                    self.option = (1,1)
                    return self
                except Exception as e:
                    quit("\x1b[;31m"+"Error el archivo No Existe.")
            else: 
                quit("\x1b[;31m"+"Error: Parametro(s) no reconocido.")
            
        #Caso general
        elif len(args) != 0:
            try:
                fileName = args[0]
                f = open(fileName, "r")
                self.text = f.read() #Lee la completitud del programa
                f.close()
                return self
            except Exception as e:
                quit("\x1b[;31m"+"Error el archivo No Existe.")
        else: 
            quit("\x1b[;31m"+"Error, No ha definido un archivo o programa a ejecutar")

        return self
    def analysis(self,error):
        if e != "bool":
            return True
        return False
