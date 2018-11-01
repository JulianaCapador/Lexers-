import ply.lex as lex

declaracionPrograma = ('iniciar-programa','inicia-ejecucion',
                       'termina-ejecucion','finalizar-programa')

declaracionProcedimiento =('define-nueva-instruccion','como')

expresion = ('apagate','gira-izquierda','avanza','coge-zumbador','deja-zumbador',
             'sal-de-instruccion','inicio','fin','SI','PARA','MIENTRAS')

funcionBooleana = ('frente-libre','frente-bloqueado','izquierda-libre',
                   'izquierda-bloqueada','derecha-libre','derecha-bloqueada',
                   'junto-a-zumbador','no-junto-a-zumbador','algun-zumbador-en-la mochila',
                   'ningun-zumbador-en-la mochila','orientado-al-norte','orientado-al-sur',
                   'orientado-al-este','orientado-al-oeste','no-orientado-al-norte',
                   'no-orientado-al-sur','no-orientado-al-este','no-orientado-al-oeste')

tokens = declaracionPrograma+declaracionProcedimiento+expresion+funcionBooleana+ ('PARENTESISA','PARENTESISC','LLAVEA','LLAVEC','CLAUSULAY','CLAUSULANO')


t_PARENTESISA = r'\('
t_PARENTESISC = r'\)'
t_LLAVEA = r'\{'
t_LLAVEC = r'\}'
t_CLAUSULAY = r'&&'
t_CLAUSULANO = r'!'

lista = []

def t_digit(t):
    r'[0-9]*'
    return t

def t_SI(t):
    r'si'
    return t

def t_PARA(t):
    r'para'
    return t

def t_MIENTRAS(t):
    r'mientras'
    return t
def t_declaracionPrograma(t):
    t['iniciar-programa']
    t['inicia-ejecucion']
    t['termina-ejecucion']
    t['finalizar-programa']
    return t
# Error handling rule
def t_error(t):
    lista.append("'%s' -> Illegal character " % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#lex.input("x = 3 - 4 + 5 * 6")

#lectura del archivo
fo = open("D:\expresiones.in","r")
lineas  = (fo.read().splitlines())
palabra = ''.join(lineas)
lex.input (palabra)

while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
