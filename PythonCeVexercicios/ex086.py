# MATRIZ EM PYTHON #

import os

nome_programa = 'criando uma matriz'.upper()

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

interface()

for i in range (0, 3):
    for j in range (0, 3):
        matriz[i][j] = int(input(f'Digite o elemento da linha {i+1} e coluna {j+1} da matriz: '))

interface()

print('Sua matriz ficou da seguinte forma: ')

for i in range (0, 3):
    for j in range (0, 3):
            print(f'[{matriz[i][j]:^5}]', end=' ')
    print()