from booleans.lexical_analyser import LexicalAnalyser
from booleans.AST import AST
from booleans.evaluator import Evaluator

def display_tree(tree):

    if tree.value == "IF-THEN-ELSE":
        print("IF-THEN-ELSE")
        display_tree(tree.left)
        display_tree(tree.middle)
        display_tree(tree.right)
    else:
        print(tree.value)

def main():

    sentence = input("Enter a term")

    analyser = LexicalAnalyser(sentence)

    tokens = analyser.return_tokens()

    syntax_tree = AST(tokens)

    tree = syntax_tree.construct()

    if tree != None:
        evaluator = Evaluator(tree)
        print(evaluator.evaluate())

if __name__ == "__main__":
    main()