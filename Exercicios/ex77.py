valor = []

while True:
    try:
        numero = int(input('Digite um número: '))
        if numero in valor:
            print('Número ja cadastrado digite novamente!')
            continue
        valor.append(numero)
    except ValueError:
        print('Digite um número valido')
        continue

    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar in ['S', 'SIM', 'SI']:
        continue
    elif continuar in ['N', 'NAO', 'NÃO']:
        print('Programa fechado!')
        print(f'Valores digitados {valor.sort()}')
        break
    else:
        print('Digite [S/N]: ')
    
    
  