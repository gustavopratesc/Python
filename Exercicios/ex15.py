angulo = float(input('Insira um angulo qualquer para saber seu seno, cosseno, tangente: '))

from math import cos, sin, tan, radians

anguloRadians = radians(angulo)

cosseno = cos(anguloRadians)
seno = sin(anguloRadians)
tangente = tan(anguloRadians)

print('O angulo fornecido foi {}°\nO cosseno é {:.2f}\nO seno é {:.2f}\nA tangente é {:.2f}'.format(angulo, cosseno, seno, tangente))