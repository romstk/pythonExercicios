lista = list()
while True:
    lista.append(int(input('Inira um número: ')))
    resposta = str(input('Deseja continuar ? S/N')).strip().upper()[0]
    if resposta in 'Nn':
        break

print(f'Listagem de números inseridos {lista}')
print(f'A lista contém {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem descrecente {lista}')

if 5 in lista:
    print('O número 5 consta na lista.')
else:
    print('O número 5 não consta na lista.')

