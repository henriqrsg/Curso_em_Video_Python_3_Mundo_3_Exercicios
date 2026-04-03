# JOGO DE DADOS #

import os
import random
import time

nome_programa = 'jogo de dados'.upper()

jogadores = []

jogador = {}

def interface(nome_programa):
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def nome_jogadores():
    global nome_programa
    i = 1
    while True: 
        interface(nome_programa)
        jogador['nome'] = input(f'Digite o nome do {i}º jogador: ')
        jogador['numero'] = random.randint(1, 6)
        jogadores.append(jogador.copy())
        i += 1
        continuar = input('Deseja adicionar mais jogadores ? [S/N]: ').upper()
        if continuar in ('NÃO', 'NAO', 'N'):
            nome_programa = 'números sorteados'.upper()
            interface(nome_programa)
            vencedor1 = ''
            numero_maior = 0
            for j in jogadores:
                print(f'O jogador {j['nome']} tirou: {j['numero']}')
                time.sleep(1)
                if j['numero'] > numero_maior:
                    numero_maior = j['numero']
                    vencedor1 = j['nome']
                    vencedor2 = None
                elif j['numero'] == numero_maior:
                    vencedor2 = j['nome']
            print()
            if vencedor2 != None:
                print(f'Os vecedores foram {vencedor1} e {vencedor2}')
            else:
                print(f'O vencedor foi o {vencedor1}')
            break

nome_jogadores()