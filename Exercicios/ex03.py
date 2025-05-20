import math

numero = int(input('Insira algum número para saber seu dobro, triplo e sua raiz quadrada: '))

dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero) # <-- biblioteca math para facilidade de calculos (como raiz e entre outros)
# ou raiz = numero ** (1/2) <-- outra forma de calcular raiz

print('O número escolhido foi {}\n O dobro é {}\n O triplo é {}\n A raiz é {}'.format(numero, dobro, triplo, raiz))