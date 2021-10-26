#Given an AST we check the type of the term
#An "invalid" type is added to indicate a type error, for simplicity

class TypeChecker:

    def __init__(self, AST):
        self.AST = AST
    
    def _checkNodeType(self, node):

        if node.value == "TRUE" or node.value == "FALSE":
            node.type = "Bool"

        elif node.value == "ZERO":
            node.type = "Nat"

        elif node.value == "SUCC" or node.value == "PRED":
            
            if node.child != "TypeError":
                child = self._checkNodeType(node.child)

                if child.type == "Nat":
                    node.type = "Nat"
                else:
                    return "TypeError"
            else:
                return "TypeError"

        elif node.value == "ISZERO":
            
            if node.child != "TypeError":
                child = self._checkNodeType(node.child)

                if child.type == "Nat":
                    node.type = "Bool"
                else:
                    return "TypeError"
            else:
                return "TypeError"

        else:
            if node.left != "TypeError" and node.right != "TypeError" and node.middle != "TypeError":
                
                guard = self._checkNodeType(node.left)
                if guard.type == "Bool":
                    then = self._checkNodeType(node.middle)
                    els = self._checkNodeType(node.right)

                    if then.type == els.type:
                        node.type = then.type
                    else:
                        return "TypeError"
                else:
                    return "TypeError"
        
        return node
    
    def checkType(self):

        node = self._checkNodeType(self.AST)
        if node == "TypeError":
            print("TypeError")
        else:
            return node
