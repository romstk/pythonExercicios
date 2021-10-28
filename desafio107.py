import moeda
preco = float(input('Informe o preço: R$ '))

print(f'O preço com acréscimo de 10% fica R$ {moeda.aumentar(preco, 10)}')
print(f'O preço com desconto de 10% fica R$ {moeda.diminuir(preco, 10)}')
print(f'O dobro do preço é R$ {moeda.dobro(preco)}')
print(f'A metade do preço é R$ {moeda.metade(preco)}')
