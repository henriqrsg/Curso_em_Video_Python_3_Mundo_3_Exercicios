# CONTADOR DE VOGAIS #

import os

nome_programa = 'contador de vogais'.upper()

lista = ('Lapis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')

interface()

for item in lista:
    vogais = ()
    for letra in item.lower():
        if letra in 'aeiou':
            if letra not in vogais:
                vogais += (letra,)
    print(f'A palavra {item.upper()}, tem as vogais: {', '.join(vogais).upper()}')