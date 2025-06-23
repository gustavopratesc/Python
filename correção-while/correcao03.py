"""Crie um programa que leia dois valores
    e mostre um menu como ao lado da tela:
    [1] soma
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    Seu programa devera realizar a operação solicitada do caso
    """
from time import sleep
primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))



while True:
    operacao = int(input("""Digite: 
                            [1] soma
                            [2] multiplicar
                            [3] maior
                            [4] novos números
                            [5] sair do programa
                     """))
    if operacao == 1:
        resultado = primeiro_numero + segundo_numero
        print(f'O resultado da soma entre {primeiro_numero} + {segundo_numero} = {resultado}')
    elif operacao == 2:
        resultado_mult = primeiro_numero * segundo_numero
        print(f'O resultado entre {primeiro_numero} * {segundo_numero} = {resultado_mult}')
    elif operacao == 3:
        if primeiro_numero > segundo_numero:
            print(f'O número {primeiro_numero} é maior que o {segundo_numero}')
        elif primeiro_numero == segundo_numero:
            print(f'São números iguais: {primeiro_numero} e {segundo_numero}')
        else:
            print(f'O {segundo_numero} é maior que o {primeiro_numero}')
    elif operacao == 4:
        print('Insira novamente os números!')
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))
    elif operacao == 5:
        sair = str(input('Deseja sair do programa? [S/N]')).upper().strip()
        if sair in 'S':
            print('Saindo do programa...')
            sleep(2)
            print('Programa fechado')
            break
        elif sair in 'N':
            print('Voltando para o menu!')
            continue
    else:
        print('Digite uma opção entre 1 e 5 informadas acima!!')