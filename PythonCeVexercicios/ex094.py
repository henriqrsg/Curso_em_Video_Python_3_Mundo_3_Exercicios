# UNINDO DICIONARIOS E LISTAS #

import os

nome_programa = 'cadastrando pessoas'.upper()

pessoas = []

pessoa = {}

mulheres = []

pessoas_idade_acima_media = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def cadastrando():
    i = 1
    while True:
        interface()
        pessoa['nome'] = input(f'Digite o nome da {i}ª pessoa cadastrada: ').strip().capitalize()
        pessoa['sexo'] = input(f'Digite o sexo de {pessoa['nome']} [M/F]: ').strip().upper()
        pessoa['idade'] = int(input(f'Digite a idade de {pessoa['nome']}: '))
        pessoas.append(pessoa.copy())
        print()
        resposta = input('Deseja cadastrar mais alguma pessoa ? [S/N]: ').upper()
        i += 1
        if resposta in ('NÃO', 'N', 'NAO'):
            interface()
            estatisticas()
            break

def estatisticas():
    soma_idades = 0
    media_idades = 0
    for p in pessoas:
        soma_idades += p['idade']
        if p['sexo'] == 'F':
            mulheres.append(p['nome'])
    media_idades = soma_idades / len(pessoas)
    print(f'A) Foram cadastradas {len(pessoas)} pessoas!')
    print(f'B) A média de idade das pessoas é de {media_idades} anos!')
    print(f'C) Aqui está todas as mulheres cadastradas: {', '.join(mulheres)}')
    for p in pessoas:
        if p['idade'] > media_idades:
            pessoas_idade_acima_media.append(p['nome'])
    print(f'D) Aqui estão todas as pessoas com idade acima da média: {', '.join(pessoas_idade_acima_media)}')

cadastrando()