numero = int(input('Insira um número inteiro qualquer: '))

termo_um = 1
termo_zero = 0
resultado = 0

while resultado <= numero:
    resultado = (numero - termo_um) + (numero - termo_zero)