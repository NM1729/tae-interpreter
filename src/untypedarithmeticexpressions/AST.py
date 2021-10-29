# Grammar for Syntax Analysis
# S -> A
# A -> if A then A else A
# A -> (A)
# A -> true
# A -> false

from untypedarithmeticexpressions.productions import Productions

class AST:

    def __init__(self, tokens):

        productions = Productions(tokens)

        self.tokens = tokens
        
        self.productions = {
            "IF":productions.ifproduction,
            "TRUE":productions.trueproduction,
            "FALSE":productions.falseproduction,
            "ZERO":productions.zeroproduction,
            "SUCC":productions.succproduction,
            "PRED":productions.predproduction,
            "ISZERO":productions.iszeroproduction,
            "OPPAR":productions.parenproduction
        }         
    
    def construct(self):
        index = 0

        production = self.productions[self.tokens[index]]
        root, index = production(index)

        if root == None or index < len(self.tokens):
            print("SyntaxError")
            return None

        return root


        



        

                        
            



