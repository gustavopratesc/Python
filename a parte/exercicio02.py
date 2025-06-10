"""Você está começando na academia hoje e a sua instrutora fez um levantamento do seu biotipo,
além de outras informações suas. Ela para calcular o seu IMC (Índice de Massa Corporal), mediu o
seu peso e sua altura. Com essas informações em mãos, ela calculou o seu IMC usando a seguinte
fórmula: imc = peso / (altura * altura). Com o valor calculado, ela te apresentou a sua ficha de
acompanhamento. Você resolveu ajudar a sua instrutora e vai fazer um programa para calcular o
imc.
"""
from math import ceil
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))

imc = peso / (altura * altura)

print('Seu peso é {}kg sua altura é {}m e seu IMC é {:.2f}'.format(peso, altura, imc))
