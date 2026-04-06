# VOTO OBRIGATÓRIO #

import os

from datetime import datetime

def interface(msg):
    msg = msg.upper()
    tamanho = len(msg) + 20
    os.system('cls')
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')
    print()

def voto(i):
    if i < 16:
        print(f'Com {i} anos não é possível votar!')
    elif i >= 16 and i <= 18:
        print(f'Com {i} anos o voto é opcional!')
    else:
        print(f'Com {i} anos o voto é obrigatório!')
    print()

def extraindo_idade():
    while True:
        interface('EXTRAINDO IDADE')
        ano_nascimento = int(input('Digite o seu ano de nascimento: '))
        ano_atual = datetime.now().year
        idade = ano_atual - ano_nascimento
        voto(idade)
        resposta = input('Deseja verificar a obrigatoriedade de votação novamente [S/N]: ').upper()
        if resposta in ('NÃO', 'NAO', 'N'):
            break

extraindo_idade()