"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador

o programa devera escrever na tela se o usuario venceu ou perdeu
"""

import random

numero_aleatorio = random.randint(0, 5) #<-- vai gerar um número aleatorio de 0 a 5
usuario_numero = int(input('Insira um número entre 0 e 5 para saber se acertou: '))

if usuario_numero > 5:
    print('INSIRA UM NÚMERO ENTRE 0 E 5!')
elif usuario_numero == numero_aleatorio:
    print(f'Parabens você acertou!! Numero inserido {usuario_numero} Numero sorteado {numero_aleatorio}')
else:
    print(f'Você não acertou!! Numero inserido {usuario_numero} Numero sorteado {numero_aleatorio}')