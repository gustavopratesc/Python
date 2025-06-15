primeiro_numero = int(input('Insira o primeiro número: '))
segundo_numero = int(input('Insira o segundo número: '))

if primeiro_numero > segundo_numero:
    print(f'O primeiro número {primeiro_numero} é maior que o segundo {segundo_numero}')
elif segundo_numero > primeiro_numero:
    print(f'O segundo número {segundo_numero} é maior que o primeiro {primeiro_numero}')
elif primeiro_numero == segundo_numero:
    print(f'Os dois números {primeiro_numero} e {segundo_numero} são iguais!!')
else:
    print('Opção invalida!!')