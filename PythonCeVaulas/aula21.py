# APRENDENDO FUNÇÕES 2 #

import math

import os

def baskhara(a, b, c):

    """
    -> Cálculo das raízes de bhaskara
    a = número acompanha x²
    b = número acompanha x
    c = número sozinho

    return = sem retorno

    Autor: Luiz Henrique Romualdo da Silva Guedes

    """

    delta = b**2 - 4 * a * c
    if delta < 0:
        print('A equação não possui raízes reais!')
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        if x1 == x2:
            print(f'A única resolução da equação é o {x1}!')
        else:
            print(f'As raízes da equação sao {x1} e {x2}!')

def somar (a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

help(baskhara)
somar(3, 2)

def interface(nome):
    tamanho = len(nome) + 20
    os.system('cls')
    print('=' * tamanho)
    print(f'{nome:^{tamanho}}')
    print('=' * tamanho)
    print()

def extraindo():
    while True:
        interface('FATORIAL')
        numero = int(input('Digite o número que deseja calcular o fatorial: '))
        fat = fatorial(numero)
        print(f'O fatorial de {numero} é igual a: {fat}')
        resposta = input('Deseja calcular o fatorial de outro número ? [S/N]:').upper()
        if resposta in ('NÃO', 'NAO', 'N'):
            break

def fatorial(n):
    f = 1
    interface('CALCULANDO')
    for i in range(1, n + 1):
        f *= i
    return f

extraindo()