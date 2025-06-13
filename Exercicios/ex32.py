"""
ESCREVA UM PROGRAMA QUE PERGUNTE
O SALARIO DE UM FUNCIONARIO E CALCULE
O VALOR DE SEU AUMENTO

PARA SALÁRIOS SUPERIORES A R$1250,00
CALCULE UM AUMENTO DE 10%

PARA INFERIORES OU IGUAIS, O AUMENTO É DE 15%
"""

salario = float(input('Insira o seu salario para receber aumento: R$'))

if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

print(f'Seu salario antigo era: R${salario}')
print(f'Seu novo salario é: R${(salario + aumento):.2f}')