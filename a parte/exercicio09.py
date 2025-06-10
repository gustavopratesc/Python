"""A sua professora de Física passou uma questão sobre velocidade média. Ela explicou que a
velocidade média de um corpo, por exemplo, um carro, é calculada dividindo a distância
percorrido (em metros) pela quantidade de tempo (em segundos).
Desse modo, a velocidade = distancia / tempo. Você que não é besta foi logo fazendo um
programa que calculasse a velocidade média, apenas lendo a distância percorrida e o tempo
gastado para percorrê-lo.
"""

print('CALCULADORA DE VELOCIDADE MEDIA!!')
distancia = float(input('Insira a distancia: '))
tempo = float(input('Insira o tempo: '))

velocidade = distancia / tempo

print('A distancia é {} O tempo é {} A velocidade média é {:.2f}'.format(distancia, tempo, velocidade))