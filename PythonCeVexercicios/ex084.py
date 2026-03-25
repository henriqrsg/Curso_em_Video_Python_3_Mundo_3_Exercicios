# LISTA COMPOSTA E ANÁLISE DE DADOS #

import os

nome_programa = 'lista composta e análise de dados'.upper()

pessoas = []

temp = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def extraindo_dados():
    mais_pesado = ''
    peso_maior = 0
    peso_menor = 10000
    mais_leve = ''
    while True:
        interface()
        temp.append(input('Digite o nome da pessoa: '))
        temp.append(float(input(f'Digite o peso de {temp[0]}: ')))
        if temp[1] > peso_maior:
            peso_maior = temp[1]
            mais_pesado = temp[0]
        if temp[1] < peso_menor:
            peso_menor = temp[1]
            mais_leve = temp[0]
        pessoas.append(temp[:])
        temp.clear()
        print()
        resposta = input('Deseja adicionar mais pessoas ? [S/N]: ').upper()
        if resposta in ('N', 'NÃO', 'NAO'):
            interface()
            analisando(mais_pesado, mais_leve, peso_maior, peso_menor)
            break

def analisando(mais_pesado, mais_leve, peso_maior, peso_menor):
    print(f'A) Foram cadastradas {len(pessoas)} pessoas')
    print(f'B) A pessoa mais pesada é {mais_pesado} com {peso_maior}kg')
    print(f'C) A pessoa mais leves é {mais_leve} com {peso_menor}kg')

extraindo_dados()