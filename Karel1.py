import ply.lex as lex
import codecs 

programa = ['INICIAR_PROGRAMA','INICIA_EJECUCION','TERMINA_EJECUCION','FINALIZAR_PROGRAMA']
reservadas = ['SI','NETONCES','SINO','MIENTRAS','HACER','REPETIR','VECES']
tokens = reservadas+programa + ['LETRA','NUMBER','PLUS','TIMES','DIVIDE', 'EQUALS','SEMICOLON','CADENA','COMMENT_SAME_LINE_PASCAL','COMMENT_SAME_LINE_JAVA']

t_ignore = ' \t'
t_PLUS = r'\+'
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

    if t.value.upper() in tokens:
        t.value = t.value.upper()
        t.type = t.value
        return t
#solo lo reconoce  
def t_COMMENT_SAME_LINE_PASCAL(t):
    r'[(* *)[\]{}]'
    pass
def t_COMMENT_SAME_LINE_JAVA(t):
    r'[/* */]'
    pass

def t_SPACE(t):
    r'\s+'
    pass

def t_CADENA(t):
    r'\".*'
    return t

#def t_INICIAR(t):
    #r'\coge-zumbador'
    #return t

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
    print str(tok.value) + " -> " + str(tok.type)

