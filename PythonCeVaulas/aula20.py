# APRENDENDO FUNÇÕES #

import math
import os

def baskhara(a, b, c):
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

def interface(titulo):
    os.system('cls')
    largura = len(titulo) + 20
    print(largura * '=')
    print(f'{titulo:^{largura}}')
    print(largura * '=')

def extraindo_valores():
    a = 0
    while True:
        interface('CALCULANDO RAÍZES DA EQUAÇÃO QUADRÁTICA')
        while a == 0:
            a = float(input('Digite o A da equação quadrática: '))
            if a == 0:
                input('Esta equação nao existe!')
                interface('CALCULANDO RAÍZES DA EQUAÇÃO QUADRÁTICA')
            else:
                break
        b = float(input('Digite o B da equação quadrática: '))
        c = float(input('Digite o C da equação quadrática: '))
        baskhara(a, b, c)
        print()
        continuar = input('Deseja resolver outra equação ? [S/N]:').upper()
        if continuar in ('NÃO','NAO','N'):
            break

extraindo_valores()