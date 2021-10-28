pessoas = {'nome':'Gustavo', 'idade':42, 'sexo':'M'}
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')

