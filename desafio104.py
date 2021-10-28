def leiaInt(n):
    numero = n
    while True:
        if numero.isnumeric():
            numero=int(numero)
            break
        else:
            print('\033[1;31mErro. Digite um número inteiro válido.\033[m')
            numero = input('Digite um número: ')
    return numero


numero = leiaInt(input('Digite um número para validação: '))
print(f'Você acaba de digitar o número {numero}')
