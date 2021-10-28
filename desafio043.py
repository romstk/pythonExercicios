peso = float(input('Informe seu peso: (Kg) '))
altura = float(input('Informe sua altura: '))
imc = (peso/altura**2)

if imc < 18.5:
    print('Seu IMC é {:.1f} e seu status é {} '.format(imc,'Abaixo do Peso.'))
elif imc<25:
    print('Seu IMC é {:.1f} e seu status é {} '.format(imc, 'Peso Ideal.'))
elif imc<30:
    print('Seu IMC é {:.1f} e seu status é {}  '.format(imc, 'Sobrepeso'))
elif imc<40:
    print('Seu IMC é {:.1f} e seu status é {}  '.format(imc, 'Obesidade.'))
else:
    print('Seu IMC é {:.1f} e seu status é {}  '.format(imc, 'Obesidade Mórbida.'))

