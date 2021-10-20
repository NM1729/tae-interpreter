# TOKENS = ["IF", "THEN", "ELSE", "TRUE", "FALSE", "OPPAR", "CLPAR", "INV"]

class LexicalAnalyser:

    TOKENS = {"if": "IF", "then": "THEN", "else": "ELSE", "true": "TRUE", "false": "FALSE", "(": "OPPAR", ")": "CLPAR", "everything else": "INV"}

    def __init__(self, sentence):
        self.sentence = sentence
    
    def _parse_sentence(self):
        word = ""
        tokens = []

        for character in self.sentence:
            token = ""

            if character == "(":
                token = self._assign_token(character)
                tokens.append(token)
            
            elif character == ")":
                token = self._assign_token(word)
                tokens.append(token)
                word = ")"
            
            elif character == " ":
                token = self._assign_token(word)
                word = ""
                tokens.append(token)
            
            else:
                word += character

        token = self._assign_token(word)
        tokens.append(token)

        self.tokens = tokens
    
    def _check_error(self):

        for token in self.tokens:
            if token == "INV":
                return True
        
        return False

    def _assign_token(self, word):

        if word in self.TOKENS:
            return self.TOKENS[word]
        else:
            return "INV"
    
    def return_tokens(self):

        self._parse_sentence()

        if self._check_error():
            print("LexicalError: Invalid term")
            return None
        else:
            return self.tokens

def main():
    print("Hello world")

if __name__ == "__main__":
    main()
