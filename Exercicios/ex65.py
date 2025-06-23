## Insira um número para tabuada e um número negativo para finalizar o programa

while True:
    numero = int(input('Insira o número para tabuada e número negativo para parar: '))
    if numero > 0:
        for i in range(1, 11):
            print(f'A tabuada de {numero} x {i} = {numero * i}')
    else:
        print('O programa foi fechado!')
        break        