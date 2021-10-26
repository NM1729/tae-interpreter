# Grammar for Syntax Analysis
# S -> A
# A -> if A then A else A
# A -> (A)
# A -> true
# A -> false

class AST:

    def __init__(self, tokens):
        self.tokens = tokens
        
        self.productions = {
            "IF":self.ifproduction,
            "TRUE":self.trueproduction,
            "FALSE":self.falseproduction,
            "OPPAR":self.parenproduction
        }

    
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
    
    def trueproduction(self, index):

        root = TermNode("TRUE")
        rule = ["TRUE"]

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

    def falseproduction(self, index):
        
        root = TermNode("FALSE")
        rule = ["FALSE"]

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
                node, index = self.productions[self.tokens[index]](index)
            
            else:
                return None, -1
        
        if node == None:
            return None, -1
        
        if paren_open:
            return None, -1
        
        return node, index 
    
    def construct(self):
        index = 0

        root, index = self.productions[self.tokens[index]](index)
        if root == None or index < len(self.tokens):
            print("SyntaxError")
            return None

        return root


class IfNode():

    def __init__(self):
        self.value = "IF-THEN-ELSE"
        self.left = None
        self.middle = None
        self.right = None

class TermNode():

    def __init__(self, value):
        self.value = value


        



        

                        
            



