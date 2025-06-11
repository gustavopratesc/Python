"""Par ou ímpar é uma forma tradicional de resolver alguns problemas quando você é criança, seja
numa brincadeira ou em algum conflito. Como as duas mãos juntas temos dez dedos, como cada
pessoa pode usar as duas mãos, vamos ter o máximo de 20 dedos. Então, vamos ensinar as
crianças a contarem todos os números pares e ímpares entre 0 e 20"""

for i in range(0, 21):
    if i % 2 == 0:
        print('Os números pares são: {}'.format(i))

for j in range(0, 21):
    if j % 2 == 1:
        print('Os números impares são: {}'.format(j))

"""pares = []
impares = []

for i in range(0, 21):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

print('Números pares entre 0 e 20:', pares)
print('Números ímpares entre 0 e 20:', impares)""" # <-- forma melhor de resolução