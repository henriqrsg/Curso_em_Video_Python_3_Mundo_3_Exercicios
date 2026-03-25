# EXTRAINDO DADOS DE UMA LISTA #

import os

nome_programa = 'extraindo dados de uma lista'.upper()

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

print(f'A) Você digitou {len(lista_n)} elementos!')
lista_n.sort(reverse=True)
print(f'B) Os valores digitados em ordem decrescente são: {lista_n}')
if 5 in lista_n:
    print(f'C) O valor 5 faz parte da lista!')
else:
    print(f'C) O valor 5 não faz parte da lista!')