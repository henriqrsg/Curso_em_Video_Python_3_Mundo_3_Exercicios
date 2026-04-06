# FICHA DO JOGADOR #

import os

def interface(msg):
    msg = msg.upper()
    tamanho = len(msg) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')
    print()

def extraindo():
    while True:
        interface('FICHA DO JOGADOR')
        nome = input('Digite o nome do jogador: ').upper()
        quant_gols = input(f'Digite quantos gols {nome} marcou: ')
        ficha_jogador(nome, quant_gols)
        resposta = input('Deseja adicionar outro jogador ? [S/N]: ').upper()
        if resposta in ('NÃO', 'NAO', 'N'):
            break
            
def ficha_jogador(n, qg):
    if n == '':
        n = 'DESCONHECIDO'
    if qg == '':
        qg = 0
    interface(f'JOGADOR {n}')
    input(f'Quantidade de gols: {qg}')
    print()
        
extraindo()