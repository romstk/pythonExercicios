from random import randint
from time import sleep
#Monta uma lista de variaveis que salva os parametros de cores para depois usar dentro do programa
cores = {'limpa':'\033[m',
         'cabecalho':'\033[7;30m',
         'acerto':'\033[30;42m',
         'erro':'\033[30;41m',
         'mensagem':'\033[1;33;44m'}

numero = randint(0,10)
#usa a formatação para colocar variáveis de cores nas strings.
print('{}-=-{}'.format(cores['cabecalho'],cores['limpa'])*30)
print('{}O sistema irá pensar em número entre 0 e 10. O usuário deverá tentar acertar.{}'.format(cores['mensagem'],cores['limpa']))
print('{}-=-{}'.format(cores['cabecalho'],cores['limpa'])*30)


usuario = int(input('Digite o número que você você quer apostar. '))
palpite=1
print('{}Processando...{}'.format(cores['mensagem'],cores['limpa']))
sleep(1)

while usuario!=numero:
      print('{}Número inválido{}'.format(cores['erro'],cores['limpa']))
      usuario = int(input('Digite o número que você você quer apostar. '))
      palpite+=1
print('{}Parabéns, você acertou!!!{}'.format(cores['acerto'],cores['limpa']))
print('{}O número escolhido pelo sistema foi {}{}'.format(cores['mensagem'],numero,cores['limpa']))
print('{}Você digitou o número {}{}'.format(cores['mensagem'],usuario,cores['limpa']))
print('{}Você precisou de {} para conseguir acertar.{}'.format(cores['mensagem'],palpite,cores['limpa']))
print('{}Jogue novamente...'.format(cores['cabecalho']))
