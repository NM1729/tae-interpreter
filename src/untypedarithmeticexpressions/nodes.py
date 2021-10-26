class IfNode():

    def __init__(self):
        self.value = "IF-THEN-ELSE"
        self.left = None
        self.middle = None
        self.right = None

class TermNode():

    def __init__(self, value):
        self.value = value

class SuccNode():

    def __init__(self, value):
        self.value = value
        self.child = None

if __name__=="__main__":
    print("Hello")