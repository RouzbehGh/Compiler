from lexer import Lexer

lexer = Lexer().build()
file = open('test1.txt')
text_input = file.read()
file.close()
lexer.input(text_input)
toks = []

while True:
    tok = lexer.token()
    toks.append(tok)
    if not tok: break
    print(tok)



