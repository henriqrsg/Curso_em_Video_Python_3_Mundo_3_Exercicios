# VALIDANDO EXPRESSÕES MATEMÁTICAS #

import os

nome_programa = 'validando expressão'.upper()

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def pegando_expressao():
    interface()
    expressao = input('Digite a sua expressão a seguir: ').strip()
    if expressao.count('(') != expressao.count(')'):
        print('Sua expressão é inválida!')
    else:
        print('Sua expressão é válida!')

pegando_expressao()