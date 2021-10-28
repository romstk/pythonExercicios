def fatorial(numero=1, show=False):
    """
    - > Programa calcula o fatorial de um número
    :param numero: Número para calcular o fatorial
    :param show: Opcional. Se for True mostra o descritivo do cálculo executado.
    :return: O resultado do cálculo do fatorial.
    """
    print('-='*20)
    print(f'Cálculo do Fatorial de {numero}')
    f = 1
    for c in range(numero, 0,-1):
        if show==True:
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
        f *= c

    return f

def dobro(numero):
    return numero * 2

def triplo(numero):
    return numero * 3











