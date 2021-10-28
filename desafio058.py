from random import randint
sistema=randint(0,10)
print('O sistema escolheu um número de 0 a 10. ')
jogador=int(input('Informe um número para tentar adivinhar a jogada do sistema: '))
palpite=1
while jogador!=sistema:
      print('Não acertou. Tente novamente.')
      jogador=int(input('Informe um número novamente: '))
      palpite+=1

print('Final do jogo. ')
print('O sistema escolheu o número {} '.format(sistema))
print('Você precisou de {} palpites para conseguir acertar. '.format(palpite))

