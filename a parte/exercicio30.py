"""Em um jogo de buraco, a soma dos pontos é importante para saber a equipe vencedora. Deste
modo, vamos fazer um programa que some todos os pontos de um jogador e ao fim imprima a
pontuação total. A leitura deve terminar quando uma pontuação negativa for informada"""

soma_pontos = 0

while True:
    pontos_jogador = int(input('Insira seus pontos / Número negativo para somar tudo: '))
    if pontos_jogador < 0:
        break
    soma_pontos += pontos_jogador

print('O total dos seus pontos foram {}'.format(soma_pontos))