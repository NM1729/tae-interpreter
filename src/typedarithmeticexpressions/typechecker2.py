#Given an AST we check the type of the term

class TypeChecker:

    def __init__(self, AST):
        self.AST = AST
        self.message = ""
        self.no_error = True
    
    def _checkNodeType(self, node):

        #true or false
        if node.value == "TRUE" or node.value == "FALSE":
            node.type = "Bool"

        #0
        elif node.value == "ZERO":
            node.type = "Nat"

        #succ or pred
        elif node.value == "SUCC" or node.value == "PRED":
            
            if self.no_error:
                child = self._checkNodeType(node.child)

                if child.type == "Nat":
                    node.type = "Nat"
                else:
                    self.no_error = False
                    self.message = f"{node.value.lower()} is incompatible with type Bool"

        #iszero
        elif node.value == "ISZERO":
            
            if self.no_error:
                child = self._checkNodeType(node.child)

                if child.type == "Nat":
                    node.type = "Bool"
                else:
                    self.no_error = False
                    self.message = "iszero is incompatible with type Nat"

        else:
            if self.no_error:
                
                guard = self._checkNodeType(node.left)
                
                if guard.type == "Bool":    
                    then = self._checkNodeType(node.middle)
                    els = self._checkNodeType(node.right)

                    if then.type == els.type:
                        node.type = then.type
                    else:
                        self.no_error = False
                        self.message = "Incompatible types for then and else parts"
                else:
                    self.no_error = False
                    self.message = "if part must be of type Bool"
        
        return node
    
    def checkType(self):

        node = self._checkNodeType(self.AST)
        if not self.no_error:
            print(f"TypeError: {self.message}")
            return None
        else:
            return node
