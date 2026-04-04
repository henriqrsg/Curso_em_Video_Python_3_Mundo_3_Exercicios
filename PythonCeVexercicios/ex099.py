# FUNÇÃO QUE DESCOBRE MAIOR #

import os

def interface(msg):
    msg = msg.upper()
    tamanho = len(msg) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')

def extraindo_numeros():
    while True:
        numeros = []
        interface('digite os números')
        quant_numeros = int(input('Digite quantos números a sua lista tera: '))
        for i in range(quant_numeros):
            interface('digite os números')
            numeros.append(int(input(f'Digite o {i+1}º número: ')))
        maior(numeros)
        resposta = input('Deseja analisar outra lista de números ? [S/N]: ').upper()
        numeros.clear()
        if resposta in ('NAO', 'NÃO', 'N'):
            break

def maior(lista):
    print(f'A sua lista tem {len(lista)} números')
    print(f'O maior número é o: {max(lista)}!')
    print()

extraindo_numeros()
