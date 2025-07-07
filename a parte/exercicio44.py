lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in ['SIM', 'S']:
            break
        elif c in ['NÃO', 'NAO', 'N']:
            print('Resultados...')
            print(f'Números digitados: {len(lista)}')
            lista.sort(reverse=True)
            print(f'Valores em ordem decrescente: {lista}')
            if 5 in lista:
                print(f'O valor 5 esta na lista e esta na posição {lista.index(5) + 1}')
            else:
                print('O valor 5 não esta na lista')
            exit()
        else:
            print('Escolha entre [S/N]!!')