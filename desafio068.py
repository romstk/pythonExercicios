from random import randint
vitorias=0
print('VAMOS JOGAR PAR OU IMPAR ? ')
while True:
    print('-'*20)
    computador = randint(0, 10)
    while True:
        jogador = int(input('Jogue um número: [0 a 10 ] '))
        if jogador >=0 and jogador <=10:
            break
    while True:
        escolha = str(input('Escolhe Par ou Impar ? ')).strip().upper()[0]
        if escolha in 'PI':
            break
    total = jogador+computador
    print(f'Você escolheu {jogador} e o computador {computador}. Total {total}')
    if escolha == 'P':
       if total % 2 == 0:
          print('Você venceu!!!')
          vitorias += 1
       else:
           print('Você perdeu!!!')
           break
    elif escolha == 'I':
       if total % 2 != 0:
           print('Você venceu!!!')
           vitorias +=1
       else:
           print('Você perdeu!!!')
           break
print(f'Game Over!!! Você venceu {vitorias} vezes.')
