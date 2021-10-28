numeros = ('zero','um', 'dois','tres','quatro','cinco','seis', 'sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Informe um número de zero a vinte: '))
    if numero>=0 and numero <=20:
        break
    else:
        print('Número inválido. Tente novamente.')
print(f'O número digitado escrito por extenso é {str(numeros[numero]).upper()} .')