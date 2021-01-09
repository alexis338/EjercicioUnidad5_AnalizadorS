import ply.lex as lex
import re
import sys

resultado_lexema = []


tokens = [
    'ASIGNACION',
    'ARITMETICA',
    'BOOLMENMAY',
    'BOOLMENMAYEQUALS',
    'BOOLDIF',
    'FORMULAS',
    'STRING',
    'ESTRUCTURA'
]

def t_ASIGNACION(t):
    r'(\w+\s\=\s(\d+|\w+))'
    return t

def t_ARITMETICA(t):
    r'(\w+\=(\d+|\w+)[+*/-](\d+|\w+))'
    return t

def t_BOOLMENMAY(t):
    r'\w+\s([<>])\s(\d+|\w+)'
    return t

def t_BOOLMENMAYEQUALS(t):
    r'(\s|\S)\w+\s((\<\=)|(\>\=))\s(\d+|\w+)'
    return t

def t_BOOLDIF(t):
    r'\w+\s((\=\=)|(\!\=))\s\d+'
    return t

def t_FORMULAS(t):
    r'(\w+\s\=\s)(\(\d[+*/-]\d\)[*/+-]\d)|(\w+\=)(\(\w+[/*+-]\d[*/+-]\d\)[/*+-]\w+)'
    return t

def t_ESTRUCTURA(t):
    r'if|while|case|for|else|end'
    return t

def t_STRING(t):
    r'\w+|:'
    return t

t_ignore = '\t'

def t_espacio(t):
    r"\s"
    pass

def t_error(t):
    global resultado_lexema
    estado = "  ¡Este Token no es Valido! {:4}".format(str(t.lineno))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:4} Equivale {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value))
        resultado_lexema.append(estado)

    return resultado_lexema

analizador = lex.lex()

try:
    file_name = sys.argv[1]
    archivo = open(file_name, "r")
except:
    print("No se encontro ningun archivo con ese nombre")
    quit()

text = ""
for linea in archivo:
    text += linea
prueba(text)
print('\n'.join(list(map(''.join, resultado_lexema))))