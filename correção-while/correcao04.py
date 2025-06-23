"""Faça um programa que leia um número inteiro e leia seu factorial
    ex: 5! 5x4x3x2x1 = 120
"""
from math import factorial
while True:
    numero = int(input('Insira um número inteiro para fatorial, ou 0 para finalizar: '))
    if numero != 0:
        numero_factorial = factorial(numero)
        print(f'O número fatorial de {numero}! é igual a {numero_factorial}')
    else:
        print(f'Você finalizou o programa!')
        break




