from datetime import date
ano = int(input('Informe um ano para sabermos se o mesmo é bissexto. Coloque zero para verificar o ano atual: '))

if ano == 0:
    ano = date.today().year

#parênteses não é obrigatório, usei para organizar melhor.
if ( (ano%4==0 and ano%100 !=0) or (ano%400 == 0) ):
           print('O ano {} é BISSEXTO.'.format(ano))
else:
         print('O ano {} não é BISSEXTO.'.format(ano))
