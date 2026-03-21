# LENDO NUMERO POR EXTENSO #

import os

nome_programa = 'número por extenso'.upper()

def interface():
    os.system('cls')
    print(50 * '=')
    print(f'{nome_programa:^50}')
    print(50 * '=')

lista_numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    interface()
    numero = int(input('Digite um número de 1 até 20: '))
    if numero <= 0 or numero > 20:
        input('Digite um número válido! ')
    else:
        print()
        print(f'O número {numero} por extenso se escreve: {lista_numeros[numero-1].upper()}')
        print()
        break