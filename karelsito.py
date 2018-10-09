import ply.lex as lex


declaracion = (
    'iniciar-programa','inicia-ejecucion','termina-ejecucion','finalizar-programa'
        
)
expresion = (
    'APAGATE',
    'GIRAIZQUIERDA',
    'AVANZA',
    'COGEZUMBADOR',
    'DEJAZUMBADOR',
    'SALINSTRUCCION',
    'SI',
    'ENTONCES',
    'SINO',
    'MIENTRAS',
    'HACER',
    'REPETIR',
    'VECES',
)

fbooleana=(
     'frente-libre',
     'frente-bloqueado',
     'izquierda-libre',
     'izquierda-bloqueada',
     'derecha-libre',
     'derecha-bloqueada',
     'junto-a-zumbador',
     'no-junto-a-zumbador',
     'algun-zumbador-en-la mochila',
     'ningun-zumbador-en-la mochila',
     'orientado-al-norte',
     'orientado-al-sur',
     'orientado-al-este',
     'orientado-al-oeste',
     'no-orientado-al-norte',
     'no-orientado-al-sur',
     'no-orientado-al-este',
     'no-orientado-al-oeste',
)

tokens =declaracion+expresion+fbooleana+('IDENTIFICADOR','TIPO','DECIMAL','ARGVACIO','TERMINO','CLAUSULAY','CLAUSULANO','ATOMICA','EQUALS','SEPARADOR','BLOQUEABIERTO','BLOQUECERRADO')

t_ignore = ' \t'
t_ARGVACIO = r'\(\)'
t_TERMINO=r'\|\|'
t_CLAUSULAY = r'&&'
t_CLAUSULANO = r'!'
t_TIPO=r'define' or r'void'
t_EQUALS = r'='
t_BLOQUEABIERTO =r'\{'
t_BLOQUECERRADO =r'\}'
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'

lista = []
def t_DECIMAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_APAGATE(t):
    r'apagate'
    return t

def t_GIRAIZQUIERDA(t):
    r'gira-izquierda'
    return t

def t_ENTONCES(t):
    r'entonces'
    return t

def t_SI(t):
    r'si'
    return t

def t_COGEZUMBADOR(t):
    r'coge-zumbador'
    return t

def t_DEJAZUMBADOR(t):
    r'deja-zumbador'
    return t

def t_SALINSTRUCCION(t):
    r'sal-de-instruccion'
    return t

def t_SINO(t):
    r'sal-de-instruccion'
    return t

def t_HACER(t):
    r'hacer'
    return t

def t_REPETIR(t):
    r'hacer'
    return t

def t_VECES(t):
    r'veces'
    return t
    
def t_PROGRAMA(t):
    r'program'
    return t


# Error handling rule
def t_error(t):
    lista.append("'%s' -> Illegal character " % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#lex.input("x = 3 - 4 + 5 * 6")

def tokens(expresion):
    lex.input(expresion)
    while True:
        tok = lex.token()
        if not tok: break
        lista.append(str(tok.value) + " -> " + str(tok.type))
    return lista
