# PRINT ADAPTÁVEL #

import os

def interface(titulo):
    tamanho = len(titulo) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{titulo:^{tamanho}}')
    print(tamanho * '=')

os.system('cls')
msg = input('Digite qualquer mensagem: ')

interface(msg)