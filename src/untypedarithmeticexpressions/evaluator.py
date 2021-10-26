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

        elif node.value == "ZERO":
            return "0"

        elif node.value == "SUCC":
            child = self._evaluateNode(node.child)
            return "succ " + child

        elif node.value == "PRED":
            child = self._evaluateNode(node.child)
            if child.startswith("succ"):
                return child[5:]
            elif child == "0":
                return "0"
            else:
                return "pred " + child

        elif node.value == "ISZERO":
            child = self._evaluateNode(node.child)
            if child.startswith("succ"):
                return "false"
            elif child == "0":
                return "true"
            else:
                return "iszero " + child

        else:
            guard = self._evaluateNode(node.left)
            if guard == "true":
                return self._evaluateNode(node.middle)
            elif guard == "false":
                return self._evaluateNode(node.right)
            else:
                return "if " + guard + " then " + self._evaluateNode(node.middle) + " else " + self._evaluateNode(node.right)
    
    def evaluate(self):
        return self._evaluateNode(self.AST)
