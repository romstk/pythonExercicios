print('-=-'*20)
print('Analizador de Triângulos')
print('-=-'*20)

r1 = float(input('Digite o valor do segmento 1: '))
r2 = float(input('Digite o valor do segmento 2: '))
r3 = float(input('Digite o valor do segmento 3: '))

if r1 < r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1==r2==r3:
        print('EQUILÁTERO')
    elif r1!=r2!=r3!=r1:
        print('ESCALENO')
    else :
        print('ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo.')
