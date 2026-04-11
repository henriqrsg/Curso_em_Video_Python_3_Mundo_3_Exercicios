# ANALISANDO E GERANDO DICIONÁRIOS #

import os

alunos = []

aluno = {}

def interface(msg):
    os.system('cls')
    tamanho = len(msg) + 20
    print(tamanho * '=')
    print(f'{msg:^{tamanho}}')
    print(tamanho * '=')
    print()

def notas():
    i = 0
    while True:
        i += 1
        interface('EXTRAINDO NOTAS')
        aluno['nome'] = input(f'Digite o nome do {i}º aluno: ').capitalize()
        aluno['nota1'] = float(input(f'Digite a 1ª nota do aluno {aluno['nome']}: '))
        aluno['nota2'] = float(input(f'Digite a 2ª nota do aluno {aluno['nome']}: '))
        aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
        if aluno['media'] < 5:
            aluno['situacao'] = 'Reprovado'
        elif aluno['media'] > 7:
            aluno['situacao'] = 'Aprovado'
        else:
            aluno['situacao'] = 'Recuperação'
        alunos.append(aluno.copy())
        continuar = input('Deseja cadastrar mais notas de alunos? [S/N]: ').upper()
        if continuar in ('NÃO', 'N', 'NAO'):
            notas_alunos()
            estatisticas_alunos()
            break

def notas_alunos():
    for a in alunos:
        interface('SITUAÇÃO ALUNOS')
        print(f'NOME: {a['nome']}')
        print(f'1ª NOTA: {a['nota1']}')
        print(f'2ª NOTA: {a['nota2']}')
        print(f'MÉDIA: {a['media']}')
        print(f'SITUAÇÃO: {a['situacao']}')
        input()

def estatisticas_alunos():
    interface('ESTATISTICAS ALUNOS')
    soma_medias = 0
    maior_media = -1
    menor_media = 20
    nome_aluno_maior_media = ''
    nome_aluno_menor_media = ''
    for a in alunos:
        soma_medias += a['media']
        if a['media'] > maior_media:
            maior_media = a['media']
            nome_aluno_maior_media = a['nome']
        if a['media'] < menor_media:
            menor_media = a['media']
            nome_aluno_menor_media = a['nome']
    media_turma = soma_medias / len(alunos)
    print(f'A) A maior média dos alunos foi a de {nome_aluno_maior_media} com {maior_media} pontos!')
    print(f'B) A menor média dos alunos foi a de {nome_aluno_menor_media} com {menor_media} pontos!')
    print(f'C) A média da turma foi de {media_turma} pontos!')

notas()