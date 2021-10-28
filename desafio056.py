mediaidade=0
idademaisvelho=0
homemmaisvelho=''
contmenores=0
for p in range(1, 5):
    print('-----{} ª PESSOA -----'.format(p))
    nome= str(input('Nome: ')).strip().upper()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: '))

    mediaidade+=idade

    if sexo in 'Mm':
       if idademaisvelho==0:
          idademaisvelho=idade
          homemmaisvelho=nome
       elif idade>idademaisvelho:
            idademaisvelho=idade
            homemmaisvelho=nome
    elif sexo in 'Ff':
         if idade<20:
            contmenores+=1

mediaidade=mediaidade/4
print('A média de idade do grupo é {} anos. '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(idademaisvelho,homemmaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(contmenores))






