lista = []
contador = 0
while True:
    n = int(input('Insira um número: '))
    lista.append(n)
    contador += 1
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
        if continuar in ['SIM', 'S']:
            break
        elif continuar in ['NÃO', 'NAO', 'N']:
            print(f'Resultados')
            print(f'Numeros digitados = {contador}')
            lista.sort(reverse=True)
            print(f'Lista números em forma decrescente = {lista}')
            if 5 in lista:
                print(f'O valor 5 esta na posição {lista.index(5) + 1}')
            else:
                print('O valor 5 não esta na lista!!')
            exit()
        else:
            print('Opção incorreta digite entre [S/N]')
    