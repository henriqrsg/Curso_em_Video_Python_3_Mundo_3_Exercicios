# MAIOR E MENOR VALORES TUPLA # 

import random

valores_aleatorios = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

print(f'Os valores escolhidos foram: {sorted(valores_aleatorios)}')
print(f'O maior valor escolhido foi o {max(valores_aleatorios)}')
print(f'O menor valor escolhido foi o {min(valores_aleatorios)}')