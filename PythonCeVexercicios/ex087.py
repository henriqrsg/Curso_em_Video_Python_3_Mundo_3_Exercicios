# MAIS SOBRE MATRIZ EM PYTHON #

import os

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

maiors = 0

somatc = 0

nome_programa = 'matriz mais complexa'.upper()

def interface():
    os.system('cls')
    print(80 * '=')
    print(f'{nome_programa:^80}')
    print(80 * '=')
    print()

def extraindo_valores():
    somap = 0
    interface()
    for l in range(3):
        for c in range(3):
            matriz[l][c] = int(input(f'Digite o número que entrará  na linha {l+1} e coluna {c+1} da matriz: '))
            if matriz[l][c] % 2 == 0:
                somap += matriz[l][c]
            interface()
    return somap

somap = extraindo_valores()

print('Sua matriz ficou da seguinte forma: ')
print()

for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end =' ')
    print()
print()

for l in range(3):
    somatc += matriz[l][2]

for c in range(3):
    if matriz[1][c] > maiors:
        maiors = matriz[1][c]

print(f'A) A soma dos valores pares é de {somap}')
print(f'B) A soma dos valores da terceira coluna é de {somatc}')
print(f'O maior valor da segunda linha é o {maiors}')