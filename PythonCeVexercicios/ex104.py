# VALIDANDO ESTRUTURA DE DADOS #

import os
import time

def interface(msg):
    msg = msg.upper()
    tamanho = len(msg) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')
    print()

def extraindo_numero():
    while True:
        interface('EXTRAINDO NUMERO')

        try:
            numero = int(input('Digite um número: '))
            
        except:
            print()
            print('Digite um número inteiro!')
            time.sleep(1)
            continue

        continuar = input('Deseja digitar outro número ? [S/N]: ').upper()
        if continuar in ('NÃO', 'N', 'NAO'):
            break

extraindo_numero()