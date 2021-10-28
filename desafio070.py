total=0
menorpreco=0
produtomaisbarato=''
precosmaiordemil=0
while True:
    produto = str(input('Nome do produto: '))
    while True:
        preco = float(input('Preço: '))
        if preco>0:
            break
        else:
            print('Preço inválido. ')
    total+=preco
    if preco > 1000:
       precosmaiordemil += 1
    if menorpreco==0:
       menorpreco=preco
       produtomaisbarato=produto
    else:
        if preco<menorpreco:
            menorpreco=preco
            produtomaisbarato=produto
    while True:
        resp = str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
        if resp in 'SsNn':
           break
    if resp == 'N':
        break
print(f'O total das compras realizadas foi {total}, sendo que {precosmaiordemil} produtos custaram mais que R$ 1.000,00 e o menor preço foi do produto {produtomaisbarato}. ')