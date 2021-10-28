from math import hypot
catetoo = float(input('Digite o comprimento do cateto oposto do tringulo retangulo: '))
catetoa = float(input('Digite o comprimento do cateto adjacente do triangulo retangulo: '))
print('A fórmula da hipotenusa é a raiz quadrada da soma do cateto oposto elevado ao quadrados e cateto adjacente elevado ao quadrado')
hipotenusa = hypot(catetoo,catetoa)
print('A hipotenuza é {:.2f}, considerando o cateto oposto {} e o cateto adjacente {}'.format(hipotenusa,catetoo, catetoa))
