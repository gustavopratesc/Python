lista = []
expressao = str(input('Digite uma expressão usando (): '))
lista.append(expressao)

if '(' in lista[0] and ')' in lista[-1]:
    print(f'Expressão valida {lista}')
else:
    print('Expressão invalida')