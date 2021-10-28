soma = quant = 0
while True:
    n = int(input('Informe um número inteiro: [Digite 999 para parar]'))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Foram lidos {quant} números totalizando um valor de {soma} .')
