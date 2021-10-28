from builtins import sorted

times = (
'palmeiras', 'cruzeiro', 'gremio', 'santos', 'corinthians', 'flamengo', 'atletico mineiro', 'athletico paranaense',
'internacional', 'chapecoense', 'botafogo', 'sao paulo', 'fluminense', 'vasco da gama', 'bahia', 'sport', 'vitoria',
'ponte preta', 'america', 'coritiba')

print('Tabela do Campeonato Brasileiro: ')
print('Cinco Primeiros colocados: ')
print(times[0:5])
print('Quatro últimos colocados: ')
print(times[-4:])
print('Times em ordem alfabética: ')
print(sorted(times))
print('O time Chapecoense está na ordem {}ª da tabela.'.format(times.index('chapecoense')+1))
