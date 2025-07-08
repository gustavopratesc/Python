## tive que criar uma lista [] para armazenar os gols !!

jogador = {}
numero_gols = []
nome = str(input('Insira o nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {nome} jogou?: '))
for i in range(partidas):
    gols = int(input(f'Quantos gols na partida {i + 1}: '))
    numero_gols.append(gols)

jogador['Nome'] = nome
jogador['Partidas'] = partidas
jogador['Gols'] = numero_gols
jogador['Total'] = sum(numero_gols)

print(f'Nome do jogador: {jogador["Nome"]}')
print(f'Gols feitos: {jogador["Gols"]}')
print(f'Total de gols feitos: {jogador["Total"]}')
print('=-' * 30) 

for i, g in enumerate(jogador['Gols']): # i de indice, o g de gols
    print(f'=> Na partida {i + 1}, fez {g} gols.')

print(f'Foi um total de {jogador["Total"]} gols.')