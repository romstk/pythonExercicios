produtos= ('Arroz', 5.25, 'Feijão', 4.89, 'Massa', 2.35, 'Farinha', 3.25, 'Tomate', 5.89, 'Queijo', 5, 'Óleo', 5.6)

print('-'*40)
#Print formatado com o texto centralizado e com 40 caracteres sendo preenchido os caracteres faltants com vazio
print(f'{"LISAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(produtos)):
    if pos%2==0:
        #Print formatado alinhando a variável a esquerda completando os 30 caracteres com um ponto
        print(f'{produtos[pos]:.<30}',end='')
    else:
        # Print formatado alinhando a variável a direita completando os 10 caracteres com vazio
        print(f'R$ {produtos[pos]:>10.2f}')