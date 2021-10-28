from random import randint
from time import sleep
numero = randint(0,5)
print('-=-'*30)
print('O sistema irá pensar em número entre 0 e 5. O usuário deverá tentar acertar.')
print('-=-'*30)
usuario = int(input('Digite o número que você você quer apostar. '))
print('Processando...')
sleep(3)
if usuario >5:
    print('Número inválido')
else:
    if usuario==numero:
        print('Parabéns, você acertou!!!')
        print('O número escolhido pelo sistema foi {}'.format(numero))
        print('Você digitou o número {}'.format(usuario))
    else:
        print('Tente novamente, você não acertou!!!')
        print('O número escolhido pelo sistema foi {}'.format(numero))
        print('Você digitou o número {}'.format(usuario))
    print('Jogue novamente...')
