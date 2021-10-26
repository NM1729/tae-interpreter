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
            guard = self._evaluateNode(node.left)
            if guard == "true":
                return self._evaluateNode(node.middle)
            else:
                return self._evaluateNode(node.right)
    
    def evaluate(self):
        return self._evaluateNode(self.AST)
