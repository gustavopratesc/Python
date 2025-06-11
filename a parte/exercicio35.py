"""Em uma mesa de apostas, o jogador que tirar o maior número vence a rodada. Cada mesa de
apostas tem o máximo de 6 jogadores. Após lido as jogadas, você deve informar a face de maior
valor, assim como o jogador que fez essa jogada.
"""

maior_valor = 0
jogador_vencedor = 0

for jogador in range(1, 7):
    valor = int(input(f'Jogador {jogador}, digite o valor tirado (1 a 6): '))

    while valor < 1 or valor > 6:
        print('Insira numeros corretos entre 1 a 6:')
        valor = int(input(f'Jogador {jogador}, digite novamente: '))

    if valor > maior_valor:
        maior_valor = valor
        jogador_vencedor = jogador

print(f'\nJogador vencedor: {jogador_vencedor}')
print(f'Maior valor tirado: {maior_valor}')
