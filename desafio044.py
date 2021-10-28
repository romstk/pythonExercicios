print('=+='*20)
preco = float(input('Informe o preço do produto. R$ '))
print('''Condição de pagamento:
        [1] A vista Dinheiro - 10% de desconto
        [2] A vista Cartão - 5% de desconto 
        [3] Em 2x no Cartão - Preço normal
        [4] Em 3x ou mais Cartão - 20% de juros   ''')
opt = int(input('Sua escolha: '))
if opt==1:
    preco = preco-(preco*0.10)
    print('O preco do produto a ser cobrado é R$ {:.2f}.'.format(preco))
elif opt==2:
    preco = preco - (preco * 0.05)
    print('O preco do produto a ser cobrado é R$ {:.2f}.'.format(preco))
elif opt==3:
    print('O preco do produto a ser cobrado é R$ {:.2f}.'.format(preco))
elif opt==4:
    preco = preco + (preco * 0.20)
    print('O preco do produto a ser cobrado é R$ {:.2f}.'.format(preco))
else:
    print('Opção inválida, informe os dados novamente')