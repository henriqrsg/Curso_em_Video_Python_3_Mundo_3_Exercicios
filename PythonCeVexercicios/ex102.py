# FATORIAL #

import os

def interface(msg):
    msg = msg.upper()
    tamanho = len(msg) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')
    print()

def extraindo_numero_e_mostrar():
    while True:
        interface('FATORIAL')
        numero = int(input('Digite o número que deseja ver o fatorial: '))
        mostrar = input('Deseja que o processo de cálculo do fatorial seja mostrado ? [S/N]: ').upper()
        fatorial(numero, mostrar)
        resposta = input('Deseja calcular outro fatorial ? [S/N]: ').upper()
        if resposta in ('NÃO', 'NAO', 'N'):
            break

def fatorial(n, m):
    interface('CALCULANDO')
    if m not in ('NÃO', 'N', 'NAO'):
        f = 1
        for i in range (1, n + 1):
            f *= i
            if i < n: 
                print(f'{i} x', end=' ')
            else:
                print(f'{i} = {f}', end='')
    else:
        f = 1
        for i in range (1, n + 1):
            f *= i
        print(f'O fatorial de {n} é {f}', end='')
    input()
    print()

extraindo_numero_e_mostrar()