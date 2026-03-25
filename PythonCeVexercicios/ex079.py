# VALORES ÚNICOS EM UMA LISTA #

import os

nome_programa = 'adicionando números na lista'.upper()

lista = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')

def adicionando_numeros():
    interface()
    while True:
        numero = int(input('Digite um número para adiciona-lo na lista: '))
        if numero not in lista:
            lista.append(numero)
        else:
            print('Este numero ja se encontra na lista!')
        continuar = input('Deseja adicionar mais números na lista? [S/N]: ').upper()
        interface()
        if continuar in ('NÃO','N', 'NAO'):
            break
    lista.sort()
    print(f'A lista que você criou em ordem decrescente fica da seguinte forma: {lista}')

adicionando_numeros()