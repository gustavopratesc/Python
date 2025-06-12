"""FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA SEUS DIGITOS SEPARADOS
    EX:
    DIGITE UM NÚMERO: 1834
    UNIDADE: 4
    DEZENA: 3
    CENTENA: 8
    MILHAR: 1
"""
# FORMA COM MATEMATICA!!

numero = int(input('Insira um número de 0 a 9999: '))

unidade = numero % 10
dezena = (numero // 10) % 10
centeza = (numero // 100) % 10
milhar = numero // 1000

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centeza}')
print(f'Milhar: {milhar}')

# FORMA COM STRING
# VAI DAR ERRO SE NAO TIVER NUMERO DE MILHAR POIS N POSSUI 4 UNIDADES
numero_string = str(input('Insira um número de 0 a 9999: '))

print(f'Unidade: {numero_string[3]}')
print(f'Dezena: {numero_string[2]}')
print(f'Centena: {numero_string[1]}')
print(f'Milhar: {numero_string[0]}')

