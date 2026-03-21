# APRENDENDO SOBRE TUPLAS #

lanche = ('hambúrguer', 'suco', 'pizza', 'pudim')

print(lanche[1])

print(lanche[-1])

print(lanche[0:-2])

print(lanche[1:3])

for comida in lanche:
    contador = 1
    print(f'A {contador}ª comida é o(a) {comida}')
    contador += 1

for cont in range(0, len(lanche)):
    print(f'A {cont+1}ª comida é o(a) {lanche[cont]}')

print(sorted(lanche))

tupla_1 = (1, 2, 3, 5)
tupla_2 = (4, 4, 4,)

tupla_3 = tupla_1 + tupla_2

print(tupla_3)

print(tupla_2 + tupla_1)

print(tupla_3.count(4))

print(tupla_3.index(4))

lista_aleatoria = ('pessoa', 49, True)