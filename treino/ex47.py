from random import randint

numeros_aleatorios = randint(1, 5)

numero = int(input('Insira um número entre 1 a 5: '))

if numero == numeros_aleatorios:
    print(f'Acertou!! Numero: {numero} || Numero sorteado: {numeros_aleatorios}')
elif numero > 5:
    print('Insira um número entre 1 a 5!')
else:
    print(f'Errou!!')