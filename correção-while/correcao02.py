"""Melhore o jogo do desafio 28 onde o computador vai 'pensar'
    em um número aleatorio entre 1 e 10. So que agora o jogador
    vai tentar adivinhar ate acertar. Mostrando no final quantos
    palpites foram necessarios para vencer
"""
from random import randint

contador = 1
numero_aleatorio = randint(0, 10)

print('Insira um número de 0 a 10 para ver se vc acerta o número aleatorio!')
print('+=' * 20)

while True:
    numero = int(input('0 a 10: '))
    contador += 1
    if numero == numero_aleatorio:
        print(f"""
        Você acertou!!!      
        Foram necessarios {contador} palpites
        Número jogado {numero}
        Número sorteado {numero_aleatorio}
        """)
        break
    #else:
    #    if numero > numero_aleatorio:
    #        print('Menos... tente mais uma vez')
    #    elif numero < numero:
    #        print('Mais... tente mais uma vez')
        