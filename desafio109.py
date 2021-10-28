import moeda
preco = float(input('Informe o preço: R$ '))

print(f'O preço com acréscimo de 10% fica {moeda.aumentar(preco, 10,True)}')
print(f'O preço com desconto de 10% fica {moeda.diminuir(preco, 10,True)}')
print(f'O dobro do preço é {moeda.dobro(preco,True)}')
print(f'A metade do preço é {moeda.metade(preco,True)}')
