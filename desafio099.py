def maior(valores):
    maiorValor=0
    for c in valores:
        if c > maiorValor:
            maiorValor=c
    print(f'O maior valor informado é {maiorValor}')
valores=list()
while True:
    valor=int(input('Informe um valor: '))
    valores.append(valor)
    resp=str(input('Continuar? S/N')).strip().upper()[0]
    while resp not in 'SN':
          print('Resposta inválida. Informe S/N')
          resp = str(input('Continuar? S/N')).strip().upper()[0]
    if resp=='N':
        break
print(f'Foram informados {len(valores)}. Números informados. {valores}')
maior(valores)