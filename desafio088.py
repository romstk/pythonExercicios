from random import randint
from time import sleep
print('-'*30)
print('JOGO DA MEGA SENA')
print('-'*30)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
apostas= list()
aposta = list()
print(f'-=-=-=-SORTEANDO {jogos} JOGOS-=-=-=-')
for c in range(0,jogos):
    cont=0
    while True:
        if cont<6:
            numero = randint(1,60)
            if numero not in aposta:
               aposta.append(numero)
               cont+=1
        else:
            aposta.sort()
            apostas.append(aposta[:])
            aposta.clear()
            break
for pos, aposta in enumerate(apostas):
    sleep(1)
    print(f'Jogo {pos+1} {aposta}')