from datetime import date
ano = date.today().year
maior = 0
menor= 0
for c in range(1, 8):
    nascimento = int(input('Qual o ano de seu nascimento? '))
    idade=ano - nascimento
    if idade >= 18:
       maior+=1
    else:
       menor+=1
print('Das pessoas analisadas de acordo com os anos de nascimeto informados {} pessoas são maiores de idade e {} são menores. '.format(maior,menor))