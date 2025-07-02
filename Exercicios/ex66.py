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

## ou

v = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
            tipo = str(input('Par ou impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}', end='')
    print(f'Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
         if total % 2 == 0:
              print('Você ganhou!')
              v += 1
         else:
              print('Você perdeu!!')
              break
    elif tipo == 'I':
         if total % 2 == 1:
              print('Você ganhou')
              v += 1
         else:
              print('Você perdeu!')
              break
    print('Vamos jogar novamente? ...')
    print(f'GAME OVER!! Você ganhou {v} vezes')


