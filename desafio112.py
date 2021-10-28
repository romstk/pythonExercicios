import moeda
from utilidadescev import dado

numero = float(dado.leiaDinheiro('Digite o preço: R$ '))

moeda.resumo(numero,35,22)
