def somar(a=0,b=0,c=0):
    """
    Função utilizada para soma de três valores.
    Esta função é desenvolvida com parâmetros opcionais,
    Portanto os três parâmetros são declarados com valor padrão Zero, pois se não forem informados na chamada da funcão assumirão o valor padrão
    :param a: Primeiro valor
    :param b: Segundo valor
    :param c: Terceiro valor
    :return: Sem retorno
    """
    soma = a+b+c
    print(f'Soma = {soma}')
def teste(b):

    
    a=8
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')




a=5
teste(a)
print(f'A fora vale {a}')
#somar(2,4,6)