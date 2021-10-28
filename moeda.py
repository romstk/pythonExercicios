"""
Este módulo moeda.py está replicado também no pacote utilidadescev.
A finalidade de possuir dois módulos iguais é simplesmente didática visto que no desafio 111 usamos pacotes
Nos desafios anteriores utilizamos módulos separados.
"""
def aumentar(numero, taxa=10, f=False):
    numero += ((numero * taxa)/100)
    if f==True:
        return moeda(numero)
    else:
        return numero

def diminuir(numero, taxa=10, f=False):
    numero-=((numero*taxa)/100)
    if f == True:
        return moeda(numero)
    else:
        return numero

def metade(numero, f=False):
    numero = numero/2
    if f == True:
        return moeda(numero)
    else:
        return numero

def dobro(numero, f=False):
    numero += numero
    if f == True:
        return moeda(numero)
    else:
        return numero

def moeda(numero=0, moeda='R$'):
    return str(f'{moeda} {numero:.2f}'.replace('.',','))

def resumo(numero, aumento, desconto):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(numero)}')
    print(f'Dobro do preço é \t{dobro(numero,True)}')
    print(f'Metade do preço é \t{metade(numero,True)}')
    print(f'{aumento}% de aumento \t\t{aumentar(numero, aumento,True)}')
    print(f'{desconto}% de desconto \t{diminuir(numero, desconto,True)}')
    print('-'*30)


