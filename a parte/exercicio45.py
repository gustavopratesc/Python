lista = []
par = []
impar = []

while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in ['SIM', 'S']:
            break
        elif c in ['NÃO', 'NAO', 'N']:
            print('Respostas...')
            print(f'Lista completa {lista}')
            print(f'Lista números pares {par}')
            print(f'Lista números impares {impar}')
            exit()
        else:
            print('Escolha entre [S/N]')
