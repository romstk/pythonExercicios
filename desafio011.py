print('Em seguida informe os dados da parede em metros.')
l = float(input('Largura: '))
a = float(input('Altura: '))
area = l*a
print('Para pintar uma parede com altura {} e largura {} totalizando uma área de {}m² precisamos de {:.2f} litros de tinta.'.format(a,l,area,area/2))