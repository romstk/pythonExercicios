def leiaInt(msg):
    while True:
        try:
                numero = int(input(msg))
        except (ValueError, TypeError):
                print('\033[1;31mErro. O tipo de dado informado não corresponde a um número inteiro válido.\033[m')
                continue
        except (KeyboardInterrupt):
            print('\033[1;31mErro. O usuário desistiu de digitar.\033[m')
        else:
                return numero

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc



