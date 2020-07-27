# -*- coding:utf-8 -*-
    # ? Lectura caracter por caracter 
    # ? Obtener unicamente cadenas 
    # ? Expresion regular utilizada para identificar cadenas 
    # ? INCORRECTO ---> /"[a-zA-Z0-9\n]"/ | CORRECTO ---> /"[^"]*"/
    # ? Identifica con nomenclatura ASCII o Unicode la numeración de cada caracter para evaluar rangos

class Token: 
    def __init__(self):
        self.formed = False
        self.inFormation = False
        #Guardar todos los caracteres que se van letendo en el token
        self.value = []
        self.type = None

    def info(self):
        return (
            #Transformación: Arreglo de ordinales ---> Arreglo de caracteres ---> Cadena de texto
            "".join(list(map(lambda x: chr(x),self.value))), 
            self.type
        )
    #Devolver lo que se encuentre al inicio del  arreglo 
    def atFirst(self):
        if(len(self.value == 0)): return None
        return self.value[0]

    def add(self,value):
        self.value += [value]

class Automata:
    def __init__(self, reader):
        self.reader = reader

    def run(self):
        text = self.reader.text
        tokens = []

        i = 0 
        token = None
        while(i < len(text)):
            i,token = self.tokenCreator(text,i,token)

            if token.formed: 
                tokens += [token]

        self.tokens = tokens
        return self

    def tokenCreator(self, text, i, token = None):
        if not token or token.formed:
            token = Token()

        char,pos = ord(text[i]), i
        
        #Formar nuevas cadenas
        if(
            not token.inFormation and
            self.is_quote(char)
        ):
            token.add(char)
            token.inFormation = True
            token.formed = False
            token.type = "string"
        
        #Formar nuevo entero (not token.inFormation and self.is_digit(char))
        #Formar nuevo variable (not token.inFormation and self.is_w(char)) ---> w en expresiones regulares es:
        #Letra, numero, guión bajo, mayusculas y minusculas
        elif(
            token.inFormation
        ):
            if(
                self.is_quote(token.atFirst()) and 
                not self.is_quote(char)
            ):
                token.add(char)
            
            else:
                token.add(char)
                token.formed = True

        else:
            token = Token()

        pos += 1
        return (pos, token)

    #La comilla '"' en ASCII o utf-8 se reconoce con el valor 34
    def is_quote(self,char):
        if(
            char == 34
        ): return True
        return False

