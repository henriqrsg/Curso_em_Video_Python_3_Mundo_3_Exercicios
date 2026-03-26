# PALPITES PARA A MEGA SENA #

import os
import random

nome_programa = 'sorteando números mega sena'.upper()

lista_numeros = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def sorteando():
    quant_jogos = 0
    interface()
    quant_jogos = int(input('Digite quantos jogos você quer que eu sorteie? '))
    for i in range(quant_jogos):
        for j in range(7):
            lista_numeros.append(random.randint(1, 60))
        print(f'Jogo {i+1}: {lista_numeros}')
        lista_numeros.clear()

sorteando()