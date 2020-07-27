# -*- coding:utf-8 -*-
    # ? Los errores no representan un excenario fatal
    # ? Es tolerante a errores
    # ? Ignorará todo excepto cadenas, es decir solo se entienden cadenas
    # ? Es útil cuando se quiere hacer procesamiento de lenguaje natural
    # ? Ejemplo de otra forma de ejecutar ---> cat sample.lng | python3 main.py
    # ? Cuando  el programa no este preparado para fin de archivo ocurre el error 
    # ? EOFError ---> End of file error, este es el error a capturar en este programa

class Reader: 

    def __init__(self):
        pass
    
    def read(self):
        self.text = []
        #Capturar el error corriendo el programa para usar un try & except 
        try:
            text = input()
            while True:
                self.text += [text]
                text = input()
        except EOFError:
            pass
        
        #Cada fila será sustuida por un salto de línea al final
        self.text = "\n".join(self.text)
        return self


