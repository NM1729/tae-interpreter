from booleans.lexical_analyser import LexicalAnalyser

sentence = input("Enter a term")

analyser = LexicalAnalyser(sentence)

tokens = analyser.return_tokens()

if tokens != None:
    for token in tokens:
        print(token)