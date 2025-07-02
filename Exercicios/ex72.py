import random

numeros_aleatorios = tuple(random.randint(0, 100) for _ in range(5))

print(f'Numeros aleatorios {numeros_aleatorios}')
print(f'O maior número: {max(numeros_aleatorios)}')
print(f'O menor número: {min(numeros_aleatorios)}')

# O underscore (_) é apenas uma convenção em Python que significa:

# "Eu sei que tem um valor aqui, mas eu não vou usá-lo."

# Em outras palavras: você está dizendo que não se importa com o número do loop, só quer repetir algo 5 vezes.

# Gere 5 números aleatórios entre 0 e 100, sem se importar com o número da repetição, e coloque tudo em uma tupla