# CADASTRO DE JOGADOR DE FUTEBOL #

import os

nome_programa = 'cadastrando jogador de futebol'.upper()

jogadores = []

jogador = {}

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def cadastro():
    
    while True:
        jogador['total_gols'] = 0
        jogador['media_gols'] = 0
        interface()
        jogador['nome'] = input('Digite o nome do jogador: ').capitalize()
        interface()
        jogador['posicao'] = input(f'Digite a posição do jogador {jogador['nome']}: ').capitalize()
        interface()
        while True:
            jogador['ncamisa'] = int(input(f'Digite o Nº da camisa do jogador {jogador['nome']}: '))
            if jogador['ncamisa'] > 0:
                interface()
                break
            else:
                print('Digite um número de camisa válido!')
            interface()
        jogador['quant_partidas'] = int(input(f'Digite quantas partidas o jogador {jogador['nome']} jogou: '))
        for i in range (1, jogador['quant_partidas'] + 1):
            interface()
            gols = int(input(f'Digite a quantidade de gols de {jogador['nome']} na {i}ª partida: '))
            jogador['total_gols'] += gols
        jogador['media_gols'] = jogador['total_gols'] / jogador['quant_partidas']
        jogadores.append(jogador.copy())
        interface()
        continuar = input('Deseja cadastrar outro jogador de futebol ? [S/N]: ').upper()
        if continuar in ('NÃO', 'N', 'NAO'):
            estatisticas()
            break

def estatisticas():
    interface()
    for j in jogadores:
        print(f'Nome: {j['nome']}')
        print(f'Posição: {j['posicao']}')
        print(f'Nº da camisa: {j['ncamisa']}')
        print(f'Partidas: {j['quant_partidas']}')
        print(f'Gols: {j['total_gols']}')
        print(f'Média de gols: {j['media_gols']:.2f}')
        input()
        interface()

cadastro()