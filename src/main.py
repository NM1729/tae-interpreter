from untypedarithmeticexpressions.lexical_analyser import LexicalAnalyser
from untypedarithmeticexpressions.AST import AST
from typedarithmeticexpressions.typechecker2 import TypeChecker
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

    sentence = ""
    print("Enter a term(enter quit to exit)")

    while(sentence != "quit"):

        sentence = input()

        if sentence != "quit" and sentence != "":

            analyser = LexicalAnalyser(sentence)

            tokens = analyser.return_tokens()

            syntax_tree = AST(tokens)

            if tokens != None:
                tree = syntax_tree.construct()
            else:
                tree = None

            type_checker = TypeChecker(tree)

            if tree != None:
                tree = type_checker.checkType()

            if tree != None:
                evaluator = Evaluator(tree)
                print(evaluator.evaluate())
        
        print("")

if __name__ == "__main__":
    main()