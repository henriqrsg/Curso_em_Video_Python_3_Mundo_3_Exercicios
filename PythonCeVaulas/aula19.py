pessoas = {
    'nome': 'gustavo',
    'sexo': 'M',
    'idade': 22,
}

print(pessoas['nome'])

print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')

print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())

brasil = []

estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla':'RJ'
}

estado2 = {
    'uf': 'São Paulo',
    'sigla':'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])