# En comilla simple se va a recordar un menor que como pre last y last un espacio en blanco donde el espacio en blanco se aisla desde el principio para luego ponerle la condicional que implica el 
# el siguiente token lo que importara sera un salto de linea que sea distinto a la cantidad de lineas que tenga el archivo y por eso ocupmos el self.fileName 
# es recursivo desde el " <<" para que cuando este en la misma linea "hola /*'  'mundo"
# En bash el "<<" es igual que las letras nos vale pija cuando hace brake me entendes jajaja pporque lo limpias 
# self. = True
class Token:

    def __init__(self):
        self.formed = False
        self.inFormation = False
        self.value = []
        self.type = None

    def atFist(self):
        if len(self.value) == 0:
            return None
        else:
            return self.value[0]

    def atLast(self):
        if len(self.value) == 0:
            return None
        else:
            return self.value[-1]

    def preAtLast(self):
        if len(self.value) == 0:
            return None
        else:
            return self.value[-2]
        
    def add(self, value):
        self.value +=[value]

    def info(self):
        return ("".join(list(map(lambda x: chr(x), self.value))),self.type)

class Automata:

    def __init__(self,reader):
        self.reader = reader


    def run(self):
        text = self.reader.text
        #almacenar los tokens

        tokens= []
        i = 0
        token = None

        while i < len(text):

            i,token = self.tokenCreator(text,i,token)
            
            if token.formed:
                tokens += [token]

        
        self.tokens = tokens
        return self

    def tokenCreator(self,text,i,token=None):

        if not token or token.formed:
            token = Token()

        #Siempre convertir de ordinales a char usando info del token
        char,pos = ord(text[i]),i

        #formar nuevas cadenas
        #crear digit (not token.inFormation and token.digit(char))
        if(
            not token.inFormation and self.is_quote(char)
        ):
            token.add(char)
            token.inFormation = True
            token.formed = False
            token.type = "String"
       
        elif(
            token.inFormation
        ):
            if(
                self.is_quote(token.atFist()) and not self.is_quote(char)
            ):
                token.add(char)

            else:
                token.add(char)
                token.formed = True 
        else:
            token = Token()

        pos = pos + 1
        return (pos, token)

    # /"[^"]*"/
    def is_quote(self,char):
        if(
            char ==34
        ): return True
        return False
    
    def is_Digit(self,digit): 
        if[
            char < 58 and
            char > 47
        ]: return true
        return False
    



