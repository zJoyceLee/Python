#! /usr/bin/python3
# python3 ./calculate.py

# Token types
#
# EOF token is used to indicate that
# there is no more input left for lexical analysis

INTEGER, MUL, DIV, EOF = 'INTEGER', 'MUL', 'DIV', 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, MUL, DIV, or EOF
        self.type = type
        # token value:  non-negative integer value, '*', '/', or None
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type = self.type,
            value = repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def  skip_whitspace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)


    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitspace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '*':
                self.advance()
                return Token(MUL,  '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)


class Parser(object):
    def __init__(self,  lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise  Exception('Invalid syntax')
nnnn
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        self.eat('INTEGER')

    def expr(self):
        self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token

            if token.type == MUL:
                self.eat(MUL)
                self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                self.factor()

    def parse(self):
        self.expr()

def main():
    while True:
        try:
            text = input("calc>> ")
        except EOFError:
            break
        if not text:
            continue

        parser = Parser(Lexer(text))
        parser.parse()


if __name__ == '__main__':
    main()
