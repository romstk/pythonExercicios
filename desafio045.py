from random import randint
from time import sleep

cores = {
    'limpa' : '\033[m',
    'cabecalho':'\033[7:30m',
    'opcoes':'\033[7:33:44m',
    'venceu' :'\033[1:30:42m',
    'perdeu' :'\033[1:30:41m',
    'empate': '\033[7:30m'
}

escolhas  = ('Pedra', 'Papel', 'Tesoura')

print('{}='.format(cores['cabecalho'])*20+'PEDRA PAPEL TESOURA'+'='*20)
print('''{}ESCOHA UMA DAS OPÇÕES 
      [0] PEDRA 
      [1] PAPEL 
      [2] TESOURA  
'''.format(cores['opcoes']))
jogador = int(input('{}Sua escolha: '.format(cores['limpa'])))
maquina = randint(0,2)
print('*-*'*20)
sleep(1)
print('PEDRA')
sleep(1)
print('*-*'*20)
print('PAPEL')
sleep(1)
print('*-*'*20)
print('TESOURA')
sleep(1)
print('*-*'*20)

if jogador==0:
    if maquina==0:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}EMPATE'.format(cores['empate']))
    elif maquina==1:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}Você perdeu. PAPEL ganha de PEDRA'.format(cores['perdeu']))

    elif maquina==2:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}Você venceu. PEDRA ganha de TESOURA'.format(cores['venceu']))


elif jogador==1:
    if maquina == 1:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}EMPATE'.format(cores['empate']))
    elif maquina == 0:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}Você venceu. PAPEL ganha de PEDRA'.format(cores['venceu']))

    elif maquina == 2:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}Você perdeu. TESOURA ganha de PAPEL'.format(cores['perdeu']))

elif jogador==2:
    if maquina == 2:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}EMPATE'.format(cores['empate']))
    elif maquina == 0:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}Você perdeu. PEDRA ganha de TESOURA'.format(cores['perdeu']))

    elif maquina == 1:
        print('Sua escolha foi {}'.format(escolhas[jogador]))
        print('O sistema escoheu {}'.format(escolhas[maquina]))
        print('{}Você venceu. TESOURA ganha de PAPEL'.format(cores['venceu']))

else:
   print('Opção inválida')
