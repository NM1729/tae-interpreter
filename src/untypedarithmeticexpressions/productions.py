from untypedarithmeticexpressions.nodes import IfNode, TermNode, SuccNode

class Productions:

    def __init__(self, tokens):
        self.tokens = tokens
        
        self.productions = {
            "IF":self.ifproduction,
            "TRUE":self.trueproduction,
            "FALSE":self.falseproduction,
            "ZERO":self.zeroproduction,
            "SUCC":self.succproduction,
            "PRED":self.predproduction,
            "ISZERO":self.iszeroproduction,
            "OPPAR":self.parenproduction
        } 
    
    def nochildproduction(self, index, value):
        
        root = TermNode(value)
        rule = [value]

        for term in rule:
            
            if index == -1 or index >= len(self.tokens):
                return None, -1
            else:
                token = self.tokens[index]

            if term == token:
                index += 1
            else:
                return None, -1
        
        return root, index
    
    def onechildproduction(self, index, value):

        rule = [value, "A"]

        root = SuccNode(value)

        for term in rule:

            if index == -1 or index >= len(self.tokens):
                return None, -1
            else:
                token = self.tokens[index]

            if token == term:
                index += 1
            elif term == "A":
                if self.tokens[index] in self.productions:
                    node, index = self.productions[self.tokens[index]](index)
                    root.child = node
                else:
                    return None, -1
            else:
                return None, -1
            
        if root.child == None:
            return None, -1
        else:
            return root, index
    
    def ifproduction(self, index):  

        root = IfNode()
        rule = ["IF", "A", "THEN", "A", "ELSE", "A"]
        if_val = 0 #1 for if, 2 for if-then, 3 for if-then-else
            
        for term in rule:

            if index == -1 or index >= len(self.tokens):
                return None, -1
            else:
                token = self.tokens[index]

            if term == token:

                index += 1

                if token == "IF":
                    if_val = 1
                elif token == "THEN":
                    if_val = 2
                elif token == "ELSE":
                    if_val = 3
                else:
                    return None, -1
            
            elif term == "A":

                if index == -1:
                    return None, -1
                
                elif self.tokens[index] in self.productions:
                    node, index = self.productions[self.tokens[index]](index)

                    if(if_val == 1):
                        root.left = node
                    elif(if_val == 2):
                        root.middle = node
                    elif(if_val == 3):
                        root.right = node
                    else:
                        return None, -1
                
                else:
                    return None, -1
            
            else:
                return None, -1
        
        if root.left == None or root.middle == None or root.right == None:
            return None, -1
        
        return root, index

    def parenproduction(self, index):
        
        paren_open = False

        rule = ["OPPAR","A","CLPAR"]

        node = None

        for term in rule:

            if index == -1 or index >= len(self.tokens):
                return None, -1
            else:
                token = self.tokens[index]

            if token == term:
                if token == "OPPAR" and paren_open == False:
                    paren_open = True
                elif token == "CLPAR" and paren_open == True:
                    paren_open = False
                else:
                    return None, -1
                index += 1
            
            elif term == "A":
                if self.tokens[index] in self.productions:
                    node, index = self.productions[self.tokens[index]](index)
                else:
                    return None, -1
            
            else:
                return None, -1
        
        if node == None:
            return None, -1
        
        if paren_open:
            return None, -1
        
        return node, index
    
    def trueproduction(self, index):

        return self.nochildproduction(index, "TRUE")
    
    def falseproduction(self, index):

        return self.nochildproduction(index, "FALSE")
    
    def zeroproduction(self, index):

        return self.nochildproduction(index, "ZERO")
    
    def succproduction(self, index):

        return self.onechildproduction(index, "SUCC")
    
    def predproduction(self, index):

        return self.onechildproduction(index, "PRED")
    
    def iszeroproduction(self, index):

        return self.onechildproduction(index, "ISZERO")