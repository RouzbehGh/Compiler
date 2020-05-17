from ply import lex

reserved = {
    "int": 'INTEGER',
    "float": 'FLOAT',
    "bool": 'BOOLEAN',
    "void": 'VOID',
    "true": 'TRUE',
    "false": 'FALSE',
    "print": 'PRINT',
    "return": 'RETURN',
    "main": 'MAIN',
    "if": 'IF',
    "else": 'ELSE',
    "elif": 'ELIF',
    "while": 'WHILE',
    "for": 'FOR',
    "Error": 'ERROR',
}


class Lexer:
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'VOID', 'TRUE', 'FALSE', 'PRINT', 'RETURN', 'MAIN',
        'IF', 'ELSE', 'ELIF', 'WHILE', 'FOR', 'AND', 'OR', 'NOT', 'ASSIGN',
        'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE', 'LCB',
        'RCB', 'LRB', 'RRB', 'LSB', 'RSB', 'SEMICOLON', 'COMMA', 'ERROR',
    ]

    t_AND = r'\&&'
    t_OR = r'\|\|'
    t_NOT = r'!'
    t_ASSIGN = r'\='
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_MOD = '%'
    t_GT = r'\>'
    t_GE = r'\>='
    t_LT = r'\<'
    t_LE = r'\<='
    t_EQ = r'\=='
    t_NE = r'\!='
    t_LCB = r'\{'
    t_RCB = r'\}'
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LSB = r'\['
    t_RSB = r'\]'
    t_SEMICOLON = r'\;'
    t_COMMA = r'\,'
    t_ignore = '\n \v \t\r\f'

    def t_ERROR(self, t):
        r"""([0-9]+[a-zA-Z_]+)
            |([\*\+\-\%\/][\s]*[\*\+\-\%\/][\*\+\-\%\/ ]*)
            |([\w\d]*(\.[\w\d]*){2,})
            """
        t.type = 'ERROR'
        return t

    def t_FLOATNUMBER(self, t):
        r"""\d+\.\d+"""
        before, after = str(t.value).split('.')
        if len(before) >= 10:
            t.type = 'ERROR'
            return t
        else:
            t.value = float(t.value)
            return t

    def t_INTEGERNUMBER(self, t):
        r"""[0-9]+"""
        p = int(t.value)
        t.value = int(t.value)
        if p > 999999999:
            t.type = 'ERROR'
            return t
        else:
            return t

    def t_newline(self, t):
        r"""\n+"""
        t.lexer.lineno += len(t.value)

    def t_ID(self, t):
        r"""[a-zA-Z\x80-\xff_][a-zA-Z0-9\x80-\xff_]*"""
        if t.value in reserved:
            t.type = reserved[t.value]
        return t

    def t_error(self, t):
        raise Exception('Error', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
