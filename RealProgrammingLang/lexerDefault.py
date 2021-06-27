from rply import LexerGenerator


class LexerDefault():
    def __init__(self):
        self.lexerDefault = LexerGenerator()

    def _add_tokens(self):
        #Print
        self.lexerDefault.add('PRINT', r'idiNahoi')
        #Parenthesis
        self.lexerDefault.add('OPEN_PAREN', r'\?')
        self.lexerDefault.add('CLOSE_PAREN', r'\!')
        #Semi-colon
        self.lexerDefault.add('SEMI_COLON', r'\|')
        #Operators SUM SUB
        self.lexerDefault.add('SUM', r'\-')
        self.lexerDefault.add('SUB', r'\=+')
        #Number
        self.lexerDefault.add('NUMBER', r'\d')
        #Ignore spaces
        self.lexerDefault.ignore('\s')

    def get_lexer(self):
        self._add_tokens()
        return self.lexerDefault.build()


