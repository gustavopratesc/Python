from time import sleep
lista = []
pares = []
impares = []

while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['SIM', 'S']:
            break
        elif continuar in ['NÃO', 'NAO', 'N']:
            print('Respostas...')
            sleep(2)
            print(f'Todos os números inseridos: {lista}')
            print(f'Números pares {pares}')
            print(f'Números impares {impares}')
            exit()
        else:
            print('Escolha entre: [S/N] !!')
