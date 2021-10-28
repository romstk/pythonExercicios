print('Sistema de controle de velocidade')
vel = int(input('Informe a velocidade: '))

if vel>80:
    print('Velocidade máxima ultrapassada. Você foi multado')
    multa = (vel-80)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Velocidade permitida. ')
