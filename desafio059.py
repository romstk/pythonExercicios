print('=+'*20,'TRANSAÇÕES COM NÚMEROS','=+'*20)
n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
controle = 0
resultado=0
while controle !=5:
        print('''
                [1] Somar
                [2] Multiplicar
                [3] Maior
                [4] Novos Números
                [5] Sair do programa
                ''')
        controle = int(input('Informe uma das opções: '))
        if controle==1:
           resultado=n1+n2
           print('SOMA = {}'.format(resultado))
        elif controle==2:
           resultado = n1 * n2
           print('MULTIPLICAÇÃO = {}'.format(resultado))
        elif controle==3:
             if n1>n2:
                print('MAIOR = {}'.format(n1))
             else:
               print('MAIOR = {}'.format(n2))
        elif controle==4:
             n1=float(input('Informe novos valores para o prímeiro número: '))
             n2=float(input('Informe novos valores para o segundo número: '))
        else:
            print('Opção inválida. Tente Novamente. ')
print('FIM')