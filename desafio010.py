reais = float(input('Quanto em reais você tem na carteira ? R$ '))
cambio = 3.27
dolar = reais/cambio
print('Com R${:.2f} que você possui você consegue comprar US${:.2f} considerando a cotação diária de R${:.2f}'.format(reais,dolar,cambio))