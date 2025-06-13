"""O número é par ou impar"""

numero = int(input('Insira um número para saber se é par ou impar: '))

if numero % 2 == 0:
    print(f'Esse número {numero} é par')
else:
    print(f'Esse número {numero} é impar')