# LISTA COM PARES E ÍMPARES #

import os

nome_programa = 'lista com pares e ímpares'.upper()

numeros = [[], []]

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def adicionando_numeros():
    interface()
    for i in range (1, 8):
        numero = int(input('Digite números para adiciona-los em uma lista: '))
        if numero % 2 == 1:
            numeros[0].append(numero)
        else: 
            numeros[1].append(numero)
    print(f'Os números ímpares digitados foram: {numeros[0]}')
    print(f'Os números pares digitados foram: {numeros[1]}')

adicionando_numeros()