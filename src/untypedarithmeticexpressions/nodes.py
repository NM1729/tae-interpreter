class IfNode():

    def __init__(self):
        self.value = "IF-THEN-ELSE"
        self.type = ""
        self.left = None
        self.middle = None
        self.right = None

class TermNode():

    def __init__(self, value):
        self.value = value
        self.type = ""

class SuccNode():

    def __init__(self, value):
        self.value = value
        self.type = ""
        self.child = None

if __name__=="__main__":
    print("Hello")