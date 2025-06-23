from random import randint
 
while True:

    numero = int(input('Insira um número: '))
    escolha = str(input('Você quer par ou impar? [P/I]: ')).strip().upper()

    if escolha not in ['P', 'I']:
        print('Opção invalida!')
        continue

    numero_aleatorio = randint(1, 10)
    soma = numero + numero_aleatorio
    resultado = 'P' if soma % 2 == 0 else 'I'

    print(f'Você jogou {numero} e a maquina {numero_aleatorio} somando da {soma}')
    print('Resultado: Par' if resultado == 'P' else 'Resultado: Impar')

    if escolha == resultado:
        print('Você ganhou')
        break
    else:
        print('Você perdeu!')




