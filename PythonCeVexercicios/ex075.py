# ANÁLISE DE DADOS NA TUPLA #

import os

nome_programa = 'análise de dados tupla'.upper()

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

interface()

print('Vamos analisar números!')

numeros = ()
numeros_pares = ()

for i in range(1,5):
    n = int(input('Digite um número: '))
    numeros += (n,)
    if n % 2 == 0:
        numeros_pares += (n,)
interface()

print(f'A) o valor 9 apareceu {numeros.count(9)} vezes!')
print(f'B) O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição!')
print(f'C) Os numeros pares digitados foram: {numeros_pares[0:]}')