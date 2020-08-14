class Dictionary:
    def __init__(self):
        self.json = {"return":"function return",
                "while":"cycle",
                "function":"Reserved word",
                "if":"Conditional",
                "console.log":"console print",
                "console.error":"console print error",
                "else":"Conditional",
                "false":"boleean",
                "for":"cycle",
                "null":"Reserved word",
                "break":"stop cycle",
                "==":"Comparision",
                "++":"Comparision",
                "--":"Comparision",
                "<=":"less than or equal",
                ">=":"greater than or equal",
                "!=":"different",
                "true":"boleean",
                "=":"Assignment",
                ";":"end of instruction",
                ",":"separator",
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