
# print('----Mega sena----')

# lista = []

# contador = 0
# palpite = int(input('Quantos palpiptes você quer dar?: '))
# print(f'Serão gerados {palpite} jogos')
# while contador < palpite:
#     contador += 1
#     for palpite in range(6):
#         numero_sorteado = [randint(1, 60)]
#         print(f'Numero sorteado {numero_sorteado}')
#         lista.append(numero_sorteado)

# print(lista)

## ou do jeito certo

from random import randint
from time import sleep

lista = []
jogos = []

print('-' * 30)
print('       JOGA NA MEGA SENA       ')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 0

print('\nSorteando os jogos...')
while tot < quantidade:
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
    lista.sort()
    jogos.append(lista[:])  # copia a lista
    lista.clear()
    tot += 1
    sleep(0.5)

# Imprime todos os jogos gerados
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')

