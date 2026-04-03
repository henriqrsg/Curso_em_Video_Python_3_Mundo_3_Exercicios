# CADASTRO DE TRABALHADOR #

import os

from datetime import datetime

nome_programa = 'cadastrando'.upper()

trabalhadores = []

trabalhador = {}

def interface(nome_programa):
    os.system('cls')
    print(60 * '=')
    print(f'{nome_programa:^60}')
    print(60 * '=')
    print()

def extraindo_dados():
    global nome_programa
    data_atual = datetime.today()
    while True:
        interface(nome_programa)
        trabalhador['nome'] = input('Digite o nome do trabalhador: ')
        ano_nascimento = input(f'Digite o ano de nascimento de {trabalhador['nome']} [dd/mm/aaaa]: ')
        ano_nascimento = datetime.strptime(ano_nascimento, "%d/%m/%Y")
        idade = data_atual.year - ano_nascimento.year
        trabalhador['idade'] = idade
        trabalhador['carteira_trabalho'] = int(input('Digite o número da sua carteira de trabalho (se nao tiver digite 0): '))
        if trabalhador['carteira_trabalho'] != 0:
            ano_contratacao = input('Digite o ano de contratação [dd/mm/aaaa]: ')
            trabalhador['ano_contratacao'] = ano_contratacao
            ano_contratacao = datetime.strptime(ano_contratacao, "%d/%m/%Y")
            trabalhador['ano_aposentadoria'] = ano_contratacao.year + 35
            trabalhador['salario'] = float(input('Digite seu salário: '))
        else:
            trabalhador['carteira_trabalho'] = 'sem carteira'
            trabalhador['ano_contratacao'] = 'sem contratação'
            trabalhador['ano_aposentadoria'] = 'sem trabalho prévio'
            trabalhador['salario'] = 'sem salário'
        trabalhadores.append(trabalhador.copy())
        continuar = input('Deseja adicionar mais pessoas ? [S/N]: ').upper()
        if continuar in ('NÃO', 'NAO', 'N'):
            nome_programa = 'dados trabalhadores'.upper()
            interface(nome_programa)
            for t in trabalhadores:
                print(f'{t['nome']} -> idade: {t['idade']}; nº CT: {t['carteira_trabalho']} ; ano contratação: {t['ano_contratacao']} ; ano aposentadoria: {t['ano_aposentadoria']} ; salario: {t['salario']}')
            break

extraindo_dados()