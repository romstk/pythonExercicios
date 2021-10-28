from datetime import date
atual = date.today().year
nascimento = int(input('Informe o ano de seu nascimento: '))
idade = atual - nascimento
if idade==18:
    print('Você tem {}. É hora de se alistar no serviço militar'.format(idade))
elif idade<18:
    saldo = 18-idade
    print('Você tem {}. Ainda faltam {} anos par se alistar no serviço militar. '.format(idade, saldo))
    ano = saldo +atual
    print('Você vai se alistar em {} '.format(ano))
else :
    saldo = idade - 18
    print('Você tem {}.Já se passaram {} anos do prazo de seu alistamento no serviço militar.'.format(idade,saldo))
    ano = atual - saldo
    print('Você deveria ter se alistado no ano {}'.format(ano))