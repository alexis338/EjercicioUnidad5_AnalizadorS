import ply.yacc as yacc
from AnalizadorLexicoS import tokens
import sys
import ply.lex as lex 
import re

resultado_gramatica = []

precedence = (
    ('right', 'ASIGNACION'),
    ('right', 'ARITMETICA'),
    ('right', 'BOOLMENMAY'),
    ('right', 'BOOLMENMAYEQUALS'),
    ('right', 'BOOLDIF'),
    ('right', 'FORMULAS'),
    ('right', 'STRING'),
    ('right', 'ESTRUCTURA'),
)
nombres = {}

def p_declaracion_asignacion(t):
    'declaracion : ASIGNACION'
    t[0] = t[1]

def p_declaracion_aritmetica(t):
    'declaracion : ARITMETICA'
    t[0] = t[1]

def p_declaracion_boolmenmay(t):
    'declaracion : BOOLMENMAY'
    t[0] = t[1]

def p_declaracion_boolmenmayequals(t):
    'declaracion : BOOLMENMAYEQUALS'
    t[0] = t[1]

def p_declaracion_booldif(t):
    'declaracion : BOOLDIF'
    t[0] = t[1]

def p_declaracion_formulas(t):
    'declaracion : FORMULAS'
    t[0] = t[1]

def p_declaracion_string(t):
    'declaracion : STRING'
    t[0] = t[1]

def p_declaracion_estructura(t):
    'declaracion : ESTRUCTURA'
    t[0] = t[1]

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado)

parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
   
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    return resultado_gramatica

try:
    file_name = sys.argv[1]
    archivo = open(file_name, "r")
except:
    print("No se encontro ningun archivo con ese nombre")
    quit()

text = ""
for linea in archivo:
    text += linea

