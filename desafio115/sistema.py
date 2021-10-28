from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
        criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #opção de cadastrar uma pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)


    elif resposta == 3:
        print('Saindo do Sistema... Até logo. ')
        break
    else:
        print('\033[1;31mERRO. Digite uma opção válida.\033[m')
    sleep(2)
