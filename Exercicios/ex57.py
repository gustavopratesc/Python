from time import sleep

print('Menu de calculadora!!')
print('+=' * 20)

primeiro_numero = int(input('Insira o primeiro número: '))
segundo_numero = int(input('Insira o segundo número: '))
print('+=' * 20)


while True:
    menu = int(input("""Escolha a operação:
      [1] SOMA
      [2] MULTIPLICAÇÃO
      [3] MAIOR
      [4] NOVOS NÚMEROS               
      [5] SAIR DO PROGRAMA
      """))
    print('+=' * 20)
     
    if menu == 1:
        resultado_soma = primeiro_numero + segundo_numero
        print(f'O resultado entre {primeiro_numero} e {segundo_numero} e igual a {resultado_soma}')

    elif menu == 2:
        resultado_mult = primeiro_numero * segundo_numero
        print(f'O resultado entre {primeiro_numero} e {segundo_numero} e igual a {resultado_mult}')
        
    elif menu == 3:
        if segundo_numero > primeiro_numero:
            print(f'O segundo número {segundo_numero} é maior que o primeiro {primeiro_numero}')
        else:
            print(f'O primeiro número {primeiro_numero} é maior que o segundo {segundo_numero}')
    elif menu == 4:
        primeiro_numero = int(input('Novo primeiro número: '))
        segundo_numero = int(input('Novo segundo número: '))

    elif menu == 5:
        sair_menu = 'S'
        sair_menu = str(input('Você quer sair do programa? [S/N]: ')).upper().strip()
        if sair_menu == 'S':
            print('Saindo do menu...')
            sleep(2)
            print('Menu fechado!!')
            break
        elif sair_menu == 'N':
            print('Voltando pro menu...')
            sleep(1)
        else:
            print('Opção invalida insira entre [S/N]')
    else:
        print('Opção invalida!! Escolha entre 1, 2, 3, 4, 5')
    