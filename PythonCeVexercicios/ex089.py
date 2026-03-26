# BOLETIM COM LISTAS COMPOSTAS #

import os

nome_programa = 'boletim alunos'.upper()

alunos = []
pessoa = []

def interface():
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def cadastrando_alunos():
    while True:
        nota = 0
        snota = 0
        interface()
        pessoa.append(input('Digite o nome do aluno: '))
        for i in range(2):
            nota = float(input(f'Digite a {i+1}ª nota de {pessoa[0]}: '))
            snota += nota
        media = round(snota/2, 2)
        pessoa.append(media)
        alunos.append(pessoa[:])
        pessoa.clear()
        continuar = input('Deseja cadastrar mais alunos ? [S/N]: ').upper()
        if continuar in ('NÃO','NAO','N'):
            interface()
            boletim_alunos()
            break
def boletim_alunos():
    print(60 * '-')
    print('{:<29} {:>29}'.format(' NOME', 'MÉDIA'))
    print(60 * '-')
    for na in range(len(alunos)):
        for e in range(2):
            print(f' {alunos[na][e]:<53}', end=' ')
        print()

cadastrando_alunos()