print('x'*50)
print('x Cálculo de aluguel de carros                   x')
print('x Custo R$ 60,00 por dia e R$ 0,15 por Km rodado x')
print('x'*50)
km = float(input('Informe a quilometragem rodada: '))
dias = int(input('Informe quantos dias de uso do veículo: '))
total = ((km*0.15)+(dias*60))
print('O total a pagar pelo aluguel ficou em R$ {:.2f}, \n sendo que o carro foi alugado por {} dias e rodou {:.2f} km.'.format(total,dias,km))