soma_numero = 0
estatistica_numero = []
contador = 0

while True:

    numero = int(input('Digite um número inteiro e 0 para acabar: '))

    if numero == 0:
        media = soma_numero / contador
        print('Vc finalizou o programa olhe as estatisticas')
        print(f'A media de números é: {media:.2f}')
        print(f'O maior número é {max(estatistica_numero)}')
        print(f'O menor número é {min(estatistica_numero)}')
        break

    contador += 1
    soma_numero += numero
    estatistica_numero.append(numero)
