from untypedarithmeticexpressions.lexical_analyser import LexicalAnalyser
from untypedarithmeticexpressions.AST import AST
from typedarithmeticexpressions.typechecker import TypeChecker
from untypedarithmeticexpressions.evaluator import Evaluator

def display_tree(tree):

    if tree.value == "IF-THEN-ELSE":
        print("IF-THEN-ELSE")
        display_tree(tree.left)
        display_tree(tree.middle)
        display_tree(tree.right)
    elif tree.value == "SUCC" or tree.value == "PRED" or tree.value == "ISZERO":
        print(tree.value)
        display_tree(tree.child)
    else:
        print(tree.value)

def main():

    sentence = input("Enter a term")

    analyser = LexicalAnalyser(sentence)

    tokens = analyser.return_tokens()

    syntax_tree = AST(tokens)

    tree = syntax_tree.construct()

    type_checker = TypeChecker(tree)

    if tree != None:
        tree = type_checker.checkType()

    if tree != None:
        evaluator = Evaluator(tree)
        print(evaluator.evaluate())

if __name__ == "__main__":
    main()