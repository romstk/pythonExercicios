while True:
    print('=+' * 10, 'TABUADA', '=+' * 10)

    n = int(input('''Quer mostrar a tabuada de qual número?
    Número negativo para a execução Informe aqui >>> '''))
    if n < 0:
        break
    c=1
    while c!= 11:
        print(f'{n} x {c} = {n*c}')
        c+=1
print('Programa da tabuada encerrado. Volte sempre. ')