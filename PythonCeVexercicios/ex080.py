# LISTA ORDENADA SEM REPETIÇÕES #

import os

nome_programa = 'lista ordenada'.upper()

lista = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def adicionando():
    interface()
    for i in range(1, 6):
        lista.append(int(input(f'Digite o {i}º valor para adicionar na lista: ')))
    a = 0
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                a = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = a
    print(lista)

adicionando()