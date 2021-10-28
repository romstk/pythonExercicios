from datetime import date
ano = date.today().year
nasc =int(input('Digite o ano de seu nascimento: '))
idade = ano - nasc

if idade <=9:
    print('Sua idade é {} e sua categoria é MIRIN'.format(idade))
elif idade<=14:
    print('Sua idade é {} e sua categoria é INFANTIL'.format(idade))
elif idade <=19:
    print('Sua idade é {} e sua categoria é JUNIOR'.format(idade))
elif idade <=25:
    print('Sua idade é {} e sua categoria é SENIOR'.format(idade))
else:
    print('Sua idade é {} e sua categoria é MASTER'.format(idade))
