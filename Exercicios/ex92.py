"""CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADOO 6 E TENHAM RESULTADOS ALEATORIOS. GUARDE ESSES RESULTADOS EM UM DICIONARIO. NO FINAL COLOQUE ESSE DICIONARIO EM ORDEM SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO DO DADO."""
from random import randint
from operator import itemgetter
from time import sleep
resultados = {}

# for i in range(1, 5):
#     numeros_aleatorios = randint(1, 6)
#     resultados[f'Jogador{i}'] = numeros_aleatorios # <-- aqui vai guardar os números na lista
#     print(f'O jogador{i} tirou {numeros_aleatorios}')
#     sleep(0.5)

# ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)

# print('Ranking de jogadores:')
# for pos, (jogador, valor) in enumerate(ranking, 1):
#     print(f'{pos}° lugar: {jogador}° com {valor}')
#     sleep(0.5)


## ou

jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteadors')
rank = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'Jogador vencedor!')

for i, v in enumerate(rank):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
