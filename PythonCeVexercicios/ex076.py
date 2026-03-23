# LISTAGEM DE PREÇO #

import os

nome_programa = 'listagem de preços'.upper()

lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')

interface()

for i in range (0, 17, 2):
    print(f'{lista[i].upper():<28} -> {lista[i+1]:>28}')
print(60 * '=')