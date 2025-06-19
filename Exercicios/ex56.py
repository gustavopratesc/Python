from random import randint

numero_aleatorio = randint(1, 10)
contador_palpite = 0

while True:

    jogador_numero = int(input('Insira um número de 1 a 10: '))
    contador_palpite += 1

    if jogador_numero < 1 or jogador_numero > 10:
        print('Opção invalida insira novamente: ')
        continue

    elif jogador_numero == numero_aleatorio:
        print(f"""
              Você acertou!!
              Número jogado: {jogador_numero}
              Número sorteado: {numero_aleatorio}
              Palpites necessarios: {contador_palpite}""")
        break

    else:
        print('Você errou jogue novamente!')
    