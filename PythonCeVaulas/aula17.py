# APRENDENDO SOBRE LISTAS #

num = [2, 5, 9, 1]

num[2] = 6

print(num)

num.append(7)

print(num)

num.sort()

print(num)

print(f'Essa lista tem {len(num)} elementos')

num.insert(3, 4)

print(num)

num.pop()

print(num)

num.pop(0)

print(num)

for valor in num:
    print(f'{valor}', end =' ')

print()

for chave, valor in enumerate(num):
    print(f'Na posição {chave} encontrei o {valor}')

nova_lista = []

for numeros in range(1,6):
    nova_lista.append(int(input('Digite valores para ser colocados na lista: ')))
print('Sua lista ficou dessa forma:', end=' ')
for numero in nova_lista:
    print(f'{numero}', end=' ')

print()

lista1 = [1, 2, 4]
lista2 = lista1

print(lista1)
print(lista2)

lista2[2] = 2

print(lista1)
print(lista2)

lista2 = lista1[:]
lista2[2] = 7

print(lista1)
print(lista2)
