from uteis import numeros
#def fatorial(n):
#    f = 1
#    for c in range(1,n+1):
#        f *= c
#    return f


num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat} e seu dobro é {numeros.dobro(num)}')