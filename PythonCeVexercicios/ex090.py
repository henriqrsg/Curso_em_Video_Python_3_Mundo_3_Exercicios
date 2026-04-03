# NOTAS ALUNOS #

import os

nome_programa = 'cadastrando notas alunos'.upper()

aluno = {}

alunos = []

auxiliar = False

def interface(auxiliar):
    global nome_programa
    os.system('cls')
    print(60 * '=')
    if auxiliar == True:
        nome_programa = 'dados alunos'.upper()
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def lendo_dados():
    while True:
        interface(auxiliar)
        aluno['nome'] = input('Digite o nome do aluno: ')
        aluno['nota1'] = float(input(f'Digite a 1ª nota de {aluno['nome']}: '))
        aluno['nota2'] = float(input(f'Digite a 2ª nota de {aluno['nome']}: '))
        aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
        if aluno['media'] >= 7:
            aluno['situacao'] = 'Aprovado'
        elif aluno['media'] < 7 and aluno['media'] >= 5:
            aluno['situacao'] = 'Recuperação'
        else:
            aluno['situacao'] = 'Reprovado'
        alunos.append(aluno.copy())
        print()
        continuar = input('Deseja adicionar mais alunos ? [S/N]: ').upper()
        if continuar in ('NÃO', 'NAO', 'N'):
            mostrando_dados()
            break

def mostrando_dados():
    auxiliar = True
    interface(auxiliar)
    for a in alunos:
        print(f'Aluno(a) {a['nome']}; média {a['media']:.2f}; situação: {a['situacao']} ')
        print()

lendo_dados()