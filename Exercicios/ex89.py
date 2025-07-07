from random import randint
print('----Mega sena----')

lista = []

contador = 0
palpite = int(input('Quantos palpiptes você quer dar?: '))
print(f'Serão gerados {palpite} jogos')
while contador < palpite:
    contador += 1
    for palpite in range(6):
        numero_sorteado = [randint(1, 60)]
        print(f'Numero sorteado {numero_sorteado}')
        lista.append(numero_sorteado)

print(lista)