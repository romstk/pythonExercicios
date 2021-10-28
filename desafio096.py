def area(l, c):
    area = l * c
    print(f'A área do terreno é {area}m2. ')


print('Calculando a área do terreno...')
print('-'*30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
