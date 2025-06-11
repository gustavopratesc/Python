"""Em um jogo de tabuleiro, um jogador pode movimentar uma peça apenas se o número do seu
dado for maior que o do seu adversário. Faça um programa que informe se o jogador pode ou não
jogar aquela partida. Leia o número do dado do jogador e do seu adversário e informe quem deve
jogar. No caso de empate, nenhum dos jogadores joga."""

primeiro_jogador = int(input('Insira o número do dado jogado: '))
segundo_jogador = int(input('Também insira o número do dado jogado: '))

if primeiro_jogador > segundo_jogador:
    print('O primeiro jogador jogou {} o segundo jogou {} Então o primeiro começa'.format(primeiro_jogador, segundo_jogador))
elif segundo_jogador > primeiro_jogador:
    print('O segundo jogador jogou {} o primeiro jogou {} Então o segundo começa'.format(segundo_jogador, primeiro_jogador))
else:
    print('EMPATE!!!')
    