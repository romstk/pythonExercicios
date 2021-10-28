import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('\033[1;31mO site pudim não está acessível.\033[m ')
else:
    print('O site pudim está acessível.' )
finally:
    print('Teste finalizado.')
    print(site.read())