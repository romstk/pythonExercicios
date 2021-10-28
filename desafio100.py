from random import randint
from time import sleep
def sorteio(lst):
    print('Sorteando 5 valores para lista...', end='')
    for x in range(0,5):
        sleep(0.5)
        valor = randint(1,10)
        print(f'{valor}', end=' ', flush=True)
        lst.append(valor)
    print()

def somaPar(valores):
    soma=0
    for n in valores:
        if n % 2 ==0:
            soma+=n
    print(f'Valor da soma dos pares da lista {valores} -> {soma}')
numeros = list()
sorteio(numeros)
somaPar(numeros)
