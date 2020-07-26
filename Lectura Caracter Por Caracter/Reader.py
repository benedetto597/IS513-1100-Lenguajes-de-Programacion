# -*- coding:utf-8 -*-
class Reader: 

    def __init__(self):
        pass
    
    def read(self):
        self.text = input("Ingrese una palabra o frase > ")
        return self

    def run(self):
        text = self.text
        for i in range(len(text)):
            print("The letter '%s' at position '%d'" % (text[i], i))
