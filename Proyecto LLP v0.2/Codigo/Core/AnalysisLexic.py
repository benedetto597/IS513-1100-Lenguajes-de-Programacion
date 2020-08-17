from Core.Dictionary import Dictionary
class Token:

    def __init__(self):
        self.formed = False
        self.inFormation = False
        self.value = []
        self.type = None
        self.op = False

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
        
    def add(self, value):
        self.value +=[value]

    def info(self):
        return ("".join(list(map(lambda x: chr(x), self.value))),self.type)




class Automata:

    def __init__(self,reader):
        self.text = reader.text
        self.dictionary = Dictionary()


    def infoOne(self,token):
        return ("".join(list(map(lambda x: chr(x), token))))

    def run(self):
        text = self.text
        #almacenar los tokens

        tokens= []
        i = 0
        token = None
        array=[]
        self.count = 1
        while i < len(text):
            
            i,token = self.tokenCreator(text,i,token)
            
            if token.formed:
                v,k = token.info()                 
                if(token.type == "Comment" or token.type ==  "Simple Comment" ):
                    #Comentarios ignorados
                    pass
                else: 
                    if(token.type == "Double String"):
                        #Lexemas y tokens
                        initString, type1 = v[0], "Start Double string"
                        string, type2 = v[1:-1], "String"
                        endString, type3 = v[-1] , "End Double string"
                        tokens += [[initString,type1]]
                        tokens += [[string,type2]]
                        tokens += [[endString,type3]]
                       

                    elif(token.type == "Simple String"):
                        #Lexemas y tokens
                        initString, type1 = v[0], "Start Simple string"
                        string, type2 = v[1:-1], "String"
                        endString, type3 = v[-1] , "End Simple string"
                        tokens += [[initString,type1]]
                        tokens += [[string,type2]]
                        tokens += [[endString,type3]]

                    elif(token.type == "Length"):
                        #Lexema y token
                        lexem = v.split('.')
                        userIdentifier, type1 = lexem[0], "User Identifier"
                        lengthWord, type2 = lexem[1], "Reserved word"
                        tokens += [[userIdentifier,type1]]
                        tokens += [[lengthWord,type2]]

                    else:
                        tokens += [[v,k]]
            if token.op:
                i = i-1
        #caso especial, para el ultimo caracter(final del tamanno del archivo.), agg token.
        if (i == len(text) and not token.formed):
            v,k = token.info() 
            tokens += [[v,k]]
       
            
        #print(self.count)
        #for i in range(len(tokens)):
        #    print("\n")
        #    print(self.infoOne(tokens[i]))   
        
        self.tokens = tokens
        return self

    def tokenCreator(self,text,i,token=None):
        
        if not token or token.formed:
            token = Token()

        #Siempre convertir de ordinales a char usando info del token
        char,pos = ord(text[i]),i                                        

        if(
            not token.inFormation
        ):
            #self.count += 1
            if(self.is_operator(char)):
                
                token.add(char)
                token.inFormation=True
                token.formed = False
                token.type = "Operator"
            elif(self.is_slash(char)):
                token.add(char)
                token.inFormation = True
                token.formed = False
                token.type = None

            elif(self.is_quote(char)):
                token.add(char)
                token.inFormation = True
                token.formed = False
                token.type = "Double String"
            
            elif(self.is_simpleQuote(char)):    
                token.add(char)
                token.inFormation = True
                token.formed = False
                token.type = "Simple String"

            elif(self.is_digit(char)):
                token.add(char)
                token.inFormation = True
                token.formed = False
                token.type = "Int"  
            
            elif(self.is_letter(char)):
                token.add(char)
                token.inFormation=True
                token.formed = False
                token.type = "Letter"
            elif self.is_denied(char):
                quit("\x1b[;31m"+"Error: en la línea, %d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))
            elif char == 10:
                self.count += 1
            

        elif(
            token.inFormation
        ): 
        #-------------
            #================Comentarios================================
            if(self.is_slash(token.atFist()) and self.is_asterisk(char) and (len(token.value) == 1)):
                # Aislando el caso /*
                token.add(char)
                token.type = "Comment"

            elif (self.is_slash(token.atFist()) and self.is_slash(char) and (len(token.value) == 1)):
                token.add(char)
                token.type = "Simple Comment"
            
            elif (token.type == "Simple Comment" and self.is_commentBreak(char)):
                token.formed = True    

            elif(self.is_asterisk(token.atLast()) and self.is_slash(char) and token.type == "Comment"):
                token.add(char)
                token.formed = True    
            
            elif token.type == "Comment" or token.type == "Simple Comment":
                token.add(char)          

            #------------------------------------------------------------------
            #=========================Cadenas=================================
            #Double
            if self.is_quote(token.atFist()) and self.is_quote(char):
                token.add(char)
                token.formed = True
            elif token.type == "Double String":
                token.add(char)
            #Simple
            if self.is_simpleQuote(token.atFist()) and self.is_simpleQuote(char):
                token.add(char)
                token.formed = True
            elif token.type == "Simple String":
                token.add(char)    
        #------

            #=============== Enteros y coma flotante ================================
            #1 
            #Usar esta forma de separar estados token.type
            #print((char,token.type))
            if token.type == "Int" or token.type == "Float":
                if(self.is_digit(token.atLast()) or token.type == "Float"):
                    
                    if (self.is_lineBreak(char)):
                        if(char == 10):
                            self.count += 1
                        if(token.type == "Float"):
                            if self.is_point(token.atLast()): 
                                quit("\x1b[;31m"+"Error: No se completo el flotante, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))
                            #token.add(char)
                            token.formed = True
                        else: 
                            #token.add(char)
                            token.formed = True
                            #token.type = "Int" 
                    
                    elif(self.is_point(char)):  
                        # and token.type != "Float"                                                                                     
                        if (self.is_point(token.atLast())):
                            quit("\x1b[;31m"+"Error: Doble punto no es permitido, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))
                        if token.type == "Float":
                            quit("\x1b[;31m"+"Error no se permite un segundo punto para un flotante, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))                                                                                          
                        token.add(char)
                        token.type = "Float"

                    elif(self.is_digit(token.atLast()) and self.is_letter(char)):
                        quit("\x1b[;31m"+"Error: Número incompleto, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))

                    elif(self.is_digit(char)):
                        token.add(char)

                    elif (not self.is_operator(char)):
                        #Asumimos que puede cualquier caracter que no es digito o un operador(letras y caracteres especiales)
                        quit("\x1b[;31m"+"Error: El caracter no es valido, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))
                    else:
                        #Es un nuevo token 1=
                        token.formed = True
                        token.op = True

            #--------------------------------------------------------------------
            #=========================Operadores=================================
            if token.type == "Operator":
                temp = ""
                if (self.is_digit(char) or self.is_letter(char)):
                    temp = chr(token.atLast())
                    v,k = self.dictionary.searchDict(temp)
                    if v:
                        token.type = k 
                    token.formed = True
                    token.op = True
                elif(self.is_operator(char)):
                    if chr(char) in [";","{",")"]:  #Agg. los caracteres necesarios.
                        v,k = self.dictionary.searchDict(chr(token.atLast()))
                        if v:
                            token.type = k
                            token.formed = True
                            token.op = True
                    else:     
                        temp = chr(char) 
                        temp = chr(token.atLast()) + temp
                        v,k = self.dictionary.searchDict(temp)
                        #print("%s, %s"%(v,temp))
                        if v:
                            token.type = k
                            token.add(char)
                            token.formed = True
                        else:
                            quit("\x1b[;31m"+"Error: Operador Inexistente, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))    
                elif self.is_lineBreak(char):
                    if(char == 10):
                        self.count += 1
                    temp = chr(token.atLast())
                    v,k = self.dictionary.searchDict(temp)
                    if v:
                        token.type = k 
                    token.formed = True
                elif self.is_quote(char) or self.is_simpleQuote(char):
                    token.formed = True
                    token.op = True
                else:
                    quit("\x1b[;31m"+"Error: Caracter no válido, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))
            #--------------------------------------------------------------------
            #========================= Letras =================================
            if(token.type == "Letter"):
                #print(token.value,chr(char))
                if(self.is_point(char)):
                    #print("11111")
                    current = ("".join(list(map(lambda x: chr(x), token.value))))
                    if current == "console":
                        token.add(char)
                    elif current: 
                        token.add(char)
                        token.type = "Length"
            
                
                elif self.is_letter(char):
                    token.add(char)
                
                elif self.is_operator(char):
                    current = ("".join(list(map(lambda x: chr(x), token.value))))
                    v,k = self.dictionary.searchDict(current)
                    if v:   
                        token.formed = True
                        token.type = k
                        token.op = True
                    else:
                        token.formed = True
                        token.type  = "User Identifier" 
                        token.op = True
                    
                elif self.is_lineBreak(char):
                    if(char == 10):
                        self.count += 1
                    current = ("".join(list(map(lambda x: chr(x), token.value))))
                    v,k = self.dictionary.searchDict(current)
                    if v:   
                        token.formed = True
                        token.type = k
                    else:
                        token.formed = True
                        token.type  = "User Identifier" 
                else:
                    quit("\x1b[;31m"+"Error: Caracter no identificado, en la línea ,%d en la posición %d, el caracter es: %s" %(self.count, pos , chr(char)))
            #-----------------------------------------------------------------------
            #========================= Largo de un objeto =================================
            if(token.type=="Length"):
                if char == 40:
                    
                    current = ("".join(list(map(lambda x: chr(x), token.value))))
                    #print((current))
                    pointPosition = current.index(".")
                    #print((pointPosition,current))
                    v,k = self.dictionary.searchDict(current[pointPosition+1:])
                    #print((current[pointPosition+1:],v))
                    if v:   
                        token.formed = True
                        token.type = "Length"
                        token.op = True 
                    else:
                        quit("\x1b[;31m"+"Error: Identificador de usuario no válido, en la línea ,%d en la posición %d, lexema: %s" %(self.count, pos , current))
                elif(char != 46):
                    token.add(char)
                
            #================================================
        else:
            #control de errores
            self.count += 1
            token = Token()

        pos = pos + 1
        return (pos, token)

    # /"[^"]*"/
    def is_letter(self,char):
        if(char > 64 and char<91) or (char>96 and char <123) or char == 95:
            return True
        return False

    def is_quote(self,char):
        if(
            char ==34
        ): return True
        return False

    def is_commentBreak(self,char):
        if(char == 10):
            return True
        return False

    def is_lineBreak(self,char):
        if(char in [10,32,9]):
            return True
        return False
    
    def is_digit(self,char):
       
        if(
            char > 47 and char < 58
        ): return True
        return False

    def is_point(self,char):
        if(
            char == 46 
        ): return True
        return False

    def is_slash(self,char):
        if(
            char == 47 
        ): return True
        return False

    def is_asterisk(self,char):
        if(
            char == 42
        ): return True
        return False
        
    def is_simpleQuote(self,char):
        if(
            char == 39
        ): return True
        return False

    def is_operator(self,char):
        #print(chr(char)+"*//")
        #Agregar en el arreglo los demas = < > , ;
        if (char in [42,43,45,47,59,60,61,62,44,33,40,41,123,125,91,93]):
            return True
        return False
    def is_denied(self,char):
        if char in [36,37,38,35,63,58,64,94,96,126,124,173,168]:
            return True
        return False