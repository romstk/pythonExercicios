print('Sequência de Fibonacci. ')
termos = int(input('Quantos termos quer analisar ? '))
contador=1
primeiro=0
segundo=1
proximo=0
while contador < termos:
    if contador==1:
        print(primeiro, end='->')
        print(segundo, end='->')
    else:
        proximo=primeiro+segundo
        primeiro=segundo
        segundo=proximo
        print(segundo, end='->')
    contador+=1
print('FIM.')