class Dictionary:
    def __init__(self):
        self.json = {"return":"Function return",
                "while":"Bucle",
                "function":"Reserved word",
                "if":"Conditional sentence",
                "console.log":"Console print",
                "console.error":"Console print error",
                "else":"Conditional sentence",
                "false":"Boleean",
                "for":"Bucle",
                "null":"Reserved word",
                "break":"Stop bucle",
                "==":"Comparision equal",
                "++":"Adition",
                "--":"Substraction",
                "<=":"Less than or equal",
                ">=":"Greater than or equal",
                "!=":"Different",
                "true":"Boleean",
                "=":"Assignment",
                ";":"End of instruction",
                ",":"Separator",
                "(":"Aggrupation Start",
                ")":"Aggrupation End",
                "{":"Aggrupation Start Function",
                "}":"Aggrupation End Function",
                "[":"Aggrupation End",
                "]":"Aggrupation End",
                "length":"Reserved word"
            }
    
    def searchDict(self,token):

        for k,v in  self.json.items():
            if token == k:
                return (True,v)
        return (False,"")