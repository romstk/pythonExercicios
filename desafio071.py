print('-'*15,'CAIXA ELETRÔNICO','-'*15)
while True:
    print('''Menu de Opções 
        [1] Saque
        [2] Extrato
        [3] Sair
        ''')
    opcao = int(input('Escolha a opção: '))
    print('-' * 50)
    if opcao==1:
        while True:
            valor = int(input('Valor do Saque: R$ '))
            print(f'Saque de R$ {valor} selecionado. Processando...Aguarde...')
            if valor>=50:
               inteiros = valor // 50
               valor-=(inteiros*50)
               print(f'{inteiros} notas de R$ 50,00 - total R$ {inteiros*50}')
            if valor>=20:
               inteiros = valor //20
               valor -=(inteiros*20)
               print(f'{inteiros} notas de R$ 20,00 - total R$ {inteiros*20}')
            if valor >= 10:
               inteiros = valor // 10
               valor -= (inteiros * 10)
               print(f'{inteiros} notas de R$ 10,00 - total R$ {inteiros*10}')
            if valor >= 5:
               inteiros = valor // 5
               valor -= (inteiros * 5)
               print(f'{inteiros} notas de R$ 5,00 - total R$ {inteiros*5}')
            if valor >= 1:
               inteiros = valor // 1
               valor -= (inteiros * 1)
               print(f'{inteiros} notas de R$ 1,00 - total R$ {inteiros*1}')
            print('Retire seu valor. Obrigado. ')
            print('-' * 50)
            break
    elif opcao==2:
        print('-' * 50)
        print('Emissão de Extrato concluída. ')
        print('-' * 50)
    elif opcao==3:
        print('Operação encerrada. ')
        break