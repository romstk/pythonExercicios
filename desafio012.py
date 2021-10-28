preco = float(input('Informe o preço do produto R$ '))
desc = 5
print('O produto de R$ {:.2f} com desconto de {}% fica com o novo preço de R$ {:.2f}'.format(preco,desc,(preco-(preco*desc/100))))
