# CALCULANDO AREA DE UM TERRENO #

import os

import time

def interface(titulo):
    tamanho = len(titulo) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{titulo:^{tamanho}}')
    print(tamanho * '=')

def area(a, b):
    A = a * b
    interface('AREA CALCULADA')
    time.sleep(0.2)
    print(f'A área do terreno é de {A:.2f} m²')

def calculando():
    while True:
        interface('area terreno'.upper())
        largura = float(input('Qual a largura do seu terreno [m]: '))
        comprimento = float(input('Qual o comprimento do terreno [m]: '))
        area(largura, comprimento)
        print()
        continuar = input('Deseja calcualar a area de outro terreno ? [S/N]: ').upper()
        if continuar in ('NÃO', 'N', 'NAO'):
            break

calculando()