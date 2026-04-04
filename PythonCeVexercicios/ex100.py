# FUNÇÕES PARA SORTEAR E SOMAR #

import os

import random

def interface(msg):
    msg = msg.upper()
    tamanho = len(msg) + 40
    os.system('cls')
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')

def principal():
    numeros = []
    while True:
        interface('pegando os números')
        for i in range(5):
            numeros.append(int(input(f'Digite o {i+1}º número para adicionarmos na lista: ')))
            interface('pegando os números')
        sortear(numeros)
        soma_par(numeros)
        print()
        resposta = input('Deseja analisar outra lista de números ? [S/N]: ').upper()
        numeros.clear()
        if resposta in ('NAO', 'NÃO', 'N'):
            break

def sortear(numeros):
    numero_sorteado = random.choice(numeros)
    print(f'O número sorteado foi o {numero_sorteado}')

def soma_par(numeros):
    somapares = 0
    for n in numeros:
        if n % 2 == 0:
            somapares += n
    print(f'A soma dos números pares digitados foi de {somapares}')

principal()
