# TUPLAS COM TIMES DE FUTEBOL #

import os

nome_programa = 'times de futebol'.upper()

def interface():
    os.system('cls')
    print(80 * '=')
    print(f'{nome_programa:^80}')
    print(80 * '=')
    print()

brasileirao_2026 = (
    "São Paulo",
    "Palmeiras",
    "Fluminense",
    "Bahia",
    "Atlético-MG",
    "Flamengo",
    "Grêmio",
    "Coritiba",
    "Santos",
    "Corinthians",
    "Internacional",
    "Vasco",
    "RB Bragantino",
    "Cruzeiro",
    "Fortaleza",
    "Goiás",
    "Cuiabá",
    "Vitória",
    "Chapecoense",
    "Remo"
)

interface()

print('Digite de qual colocação até qual você quer ver os colocados do Brasileirão')
print()
posicao_inicial = int(input('Digite a posição inicial: '))
print()
posicao_final = int(input('Digite a posição final: '))
print()
interface()
print(80 * '-')
print('{:^80}'.format('TABELA BRASILEIRÃO'))
print(80 * '-')

for i in range(posicao_inicial, posicao_final+1):
    print(f'{i}ª posição: {brasileirao_2026[i-1]}')

input()
interface()

time = input('Digite um time: ').strip().lower()

for i, t in enumerate(brasileirao_2026):
    if t.lower() == time:
        print(f'O {t} está na {i+1}ª posição!')
        break
else:
    print(f'O {time} não está participando do campeonato!')