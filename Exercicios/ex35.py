"""Escreva um programa que leia um número inteiro
    e peça para o usuario escolher qual sera a
    base de conversão
    1 = para binario
    2 = para octal
    3 = hexadecimal
"""
print('Transformação de int para binario, octal e hexadecimal')

numero = int(input('Insira um número: '))
conversao = int(input('1 = binario, 2 = octal, 3 = hexadecimal: '))
print('=' * 20)
if conversao == 1:
    resultado = bin(numero)
elif conversao == 2:
    resultado = oct(numero)
elif conversao == 3:
    resultado = hex(numero)
else:
    print('Insira um número conversão 1, 2 ou 3')

print(f'A conversão escolhida foi: {conversao}')
print(f'O número nessa versão fica {resultado[2:]}')