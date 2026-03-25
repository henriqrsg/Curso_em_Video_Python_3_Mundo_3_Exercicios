# MAIOR E MENOR VALORES NA LISTA #

import os

nome_programa = 'leitor de valores numéricos'.upper()

lista = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')

def lendo_valores():
    interface()
    for i in range(1, 6):
        lista.append(int(input(f'Digite o {i}º valor da lista: ')))
        interface()

lendo_valores()
print(f'O maior valor digitado foi o: {max(lista)} que se encontra na posição {lista.index(max(lista)) + 1}')
print(f'O menor valor digitado foi o: {min(lista)} que se encontra na posição {lista.index(min(lista)) + 1}')