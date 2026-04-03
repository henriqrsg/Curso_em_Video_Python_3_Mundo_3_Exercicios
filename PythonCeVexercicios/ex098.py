# FUNÇÃO DE CONTADOR #

import os

def interface(titulo):
    tamanho = len(titulo) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{titulo:^{tamanho}}')
    print(tamanho * '=')

def extraindo():
    while True:
        interface('extraindo valores'.upper())
        inicio = int(input('Digite o número de início da contagem: '))
        fim = int(input('Digite o número de fim da contagem: '))
        passo = int(input('Digite o número de passos da contagem: '))
        contador(inicio, fim, passo)
        print()
        continuar = input('Deseja contar mais ? [S/N]: ').upper()
        if continuar in ('NÃO', 'N', 'NAO'):
            break

def contador(a, b, c):
    interface('contando ...'.upper())
    if b > a:
        for i in range(a, b+1, c):
            print(i, end=' ')
    else:
        for i in range(a, b-1, c):
            print(i, end=' ')
    
extraindo()