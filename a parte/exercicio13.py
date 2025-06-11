"""Você sabe que o “par ou ímpar” é o modo tradicional de escolher algo pela sorte. Normalmente, as
duas pessoas usam apenas uma mão e escolhem o número de dedos que desejam. Você soma o
total de dedos e verifica se o número é ímpar ou par. Um número é par se a sua divisão inteira por
2 resta zero, um número é ímpar no caso contrário. Então, faça isso. Leia o número de dedos da
mão de cada jogador e diga se o resultado deu ímpar ou par.
"""

numero_dedos = int(input('Insira o número de dedos para saber se é par ou impar: '))

if (numero_dedos % 2) == 0:
    print('O número {} é par!!'.format(numero_dedos))
else:
    print('O número {} é impar!!'.format(numero_dedos))