import math

def menu(num):
    print('MENU DE OPERAÇÕES')
    print('-' * 30)
    print('1 para raiz')
    print('2 para potencia')
    print('3 para truncamento')
    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print('ERRO: Insira um número inteiro informado')
    else:
        if opcao == 1:
            raiz = math.sqrt(num)
            print(f'A raiz de {num} é {raiz:.2f}')
        elif opcao == 2:
            potencia = int(input('Quer qual número para elevar?: '))
            result = math.pow(num, potencia)
            print(f'A potencia do número {num} é igual a {result}')
        elif opcao == 3:
            trunc = math.trunc(num)
            print(f'O número truncado ficou {trunc}')
        else:
            print(f'Insira entre 1, 2, 3')


numero = float(input('Insira o número: '))
menu(numero)