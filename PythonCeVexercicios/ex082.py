# DIVIDINDO VALORES EM VÁRIAS LISTAS #

import os

nome_programa = 'dividindo a lista'.upper()

lista_impares = []

lista_pares = []

lista_n = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')

def extraindo_valores():
    while True:
        interface()
        lista_n.append(int(input('Digite um valor: ')))
        resposta = input('Quer continuar ? [S/N]: ').upper()
        if resposta in ('NÃO', 'N', 'NAO'):
            break

extraindo_valores()

print(f'A) Você digitou os seguintes elementos: {lista_n} elementos!')

for item in lista_n:
    if item % 2 == 0:
        lista_pares.append(item)
    else:
        lista_impares.append(item)

print(f'B) Os valores pares digitados foram: {lista_pares}')

print(f'B) Os valores pares digitados foram: {lista_impares}')