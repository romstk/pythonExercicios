from math import cos, sin, tan,radians
angulo = float(input('Digito um ângulo :'))
seno = sin(radians(angulo))
print('O ângulo de {}° tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print('O ângulo de {}° tem o COSSENO de {:.2f}'.format(angulo,cosseno))
tangente = tan(radians(angulo))
print('O ângulo de {}° tem a TANGENTE de {:.2f}'.format(angulo,tangente))
