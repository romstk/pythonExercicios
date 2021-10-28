distancia = int(input('Digite a distância de sua viagem: '))

if distancia > 200:
    print('O custo total de sua passagem é R${:.2f}'.format(0.45*distancia))
else:
    print('O custo total de sua passagem é R${:.2f}'.format(0.50 * distancia))