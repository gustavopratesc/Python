print('Calculo fatorial')
from math import factorial

numero = int(input('Insira um número: '))

numero_fatorial = factorial(numero)

print(numero_fatorial)

##

print('Cálculo de Fatorial')

numero = int(input('Insira um número: '))
contador = numero
fatorial = 1

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f'O fatorial de {numero} é {fatorial}')