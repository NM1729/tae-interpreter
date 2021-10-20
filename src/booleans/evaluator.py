#Given an AST we evaluate the term
#Input- IFNode(IFNode(true, false, true), false, true)

class Evaluator:

    def __init__(self, AST):
        self.AST = AST
    
    def _evaluateNode(self, node):

        if node.value == "TRUE":
            return "true"
        elif node.value == "FALSE":
            return "false"
        else:
            guard = self._evaluateNode(node.if_part)
            if guard == "true":
                return self._evaluateNode(node.then_part)
            else:
                return self._evaluateNode(node.else_part)
    
    def evaluate(self):
        return self._evaluateNode(self.AST)
