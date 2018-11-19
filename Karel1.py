import ply.lex as lex
import codecs 

programa = ['INICIAR-PROGRAMA']
tokens = reservadas + ['LETRA','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','SEMICOLON' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_SEMICOLON = r';'


def t_NUMBER(t):
    r'\d+'
    #Reconociendo solo parte entera
    t.value = int(t.value)
    return t

def t_LETRA(t):
    r'[a-z][a-zA-Z0-9_]*'

    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
        return t
    
def t_COMMENT_SAME_LINE_PASCAL(t):
    r'\{.*'
    pass

def t_SPACE(t):
    r'\s+'
    pass

def EXPRESION(t):
    r'APAGATE'
    r'IZQUIERDA'
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer


#lectura del archivo
fo = codecs.open("prueba.in","r","utf-8")
palabra = fo.read()
fo.close
lex.input (palabra)

while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)

