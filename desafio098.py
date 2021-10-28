from time import sleep
def contador(inicio, fim, passo):
    """
    -> Faz uma contagem e mostra na tela
    :param inicio: Início da contagem
    :param fim: Final da contagem
    :param passo: Passo de Contagem
    :return: sem retorno de valores.
    """


    print(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}. ')
    for c in range(inicio, fim+1, passo):
        print(f'{c}', end='-', flush=True)
        sleep(0.5)
    print('Fim!')

print('-*'*25)
contador(1, 10, 1)
print('-*'*20)
contador(10, 0, -2)
print('-*'*20)
print('Contagem personalizada: Escolha as variáveis. Para contagem decrescente o Passo deve ser negativo. ')
print('-*'*20)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
print('-*'*20)
help(contador)