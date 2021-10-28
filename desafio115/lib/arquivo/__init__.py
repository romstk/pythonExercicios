from desafio115.lib.interface import *
def arquivoExiste(nomeArq):
    try:
        # open abre um arquivo, parametros nomedoarquivo e modo de abertura, neste caso rt = read text, leitura de texto
        a = open(nomeArq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nomeArq):
        try:
            # Open vai abrir um arquivo com o modo wt+ - > write text e o + significa se não tiver o arquivo ele cria
            a = open(nomeArq, 'wt+')
            a.close()
        except:
            print('Houve um erro na criação do arquivo.')
        else:
            print(f'Arquivo {nomeArq} criado com sucesso!')

def lerArquivo(nomeArq):
    try:
        a = open(nomeArq, 'rt')
    except:
        print('Erro ao tentar abrir o arquivo. ')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        print()
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') #abre o arquivo com os parâmetros a=append e t = tipo de arquivo txt
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um problema ao escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()