"""Chega de trabalhar com datas! Agora vamos trabalhar com números aleatórios. Você está fazendo
um sistema de rifas. Você deve ler o número máximo da rifa, por exemplo: 30, 50, 100, assim
como o número da rifa apostado pelo usuário. Você deve fazer o sorteio e verificar se o número
que o usuário escolheu foi o sorteado. Procure como gerar números aleatórios na internet.
"""

from random import randint

numero_max_rifa = int(input('Insira o número maximo da rifa: 30, 50, 100: '))
numero_escolhido = int(input('Insira o número escolhido para ser sorteado: '))

numero_sorteado_rifa = randint(1, numero_max_rifa)

print('O número sorteado foi: {}'.format(numero_sorteado_rifa))
if numero_escolhido == numero_sorteado_rifa:
    print('Você acertou!! Número escolhido: {} || Número sorteado: {}'.format(numero_escolhido, numero_sorteado_rifa))
else:
    print('Que pena você não acertou!!')