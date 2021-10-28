
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota : '))
media = (n1+n2)/2

print('Sua média final foi {:.2f}. '.format(media))

if media< 5:
    print('Você foi REPROVADO. ')
elif media>=5 and media <7:
    print('Você ficou em RECUPERAÇÃO. ')
elif media >7:
    print('Você foi APROVADO. ')