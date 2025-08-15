# while
# operadores de atribuição 
# = += -= *= /= //= **= %= 

# continue
#  Mostrar apenas números ímpares de 1 a 10
# n = 0

# while n < 10:
#     n += 1
#     if n % 2 == 0:  # Se for par, pula pro próximo
#         continue
#     print(n)
# O que acontece aqui:

# n começa em 0 e vai aumentando até 10.

# Quando n é par, o continue ignora o print() e volta para o início do loop.

# Assim, só os ímpares são mostrados na tela: 1, 3, 5, 7, 9.

# nome = 'Gustavo Prates Caetano'

# indice = 0
# while indice < len(nome):
#     print(nome[indice])
#     letra = nome[indice]
#     novo_nome += f'*{letra}'
#     indice += 1

# print(novo_nome)

def calculator(first_n, second_n, operator):
    if operator == '+':
        result = first_n + second_n
    elif operator == '-':
        result = first_n - second_n
    elif operator == '*':
        result = first_n * second_n
    elif operator == '/':
        result = first_n / second_n
    else:
        print('ERRO: Digite apenas os operadores citados!')
        return
    print(f'{first_n} {operator} {second_n} = {result}')

def remain():
    while True:
        value = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if value == 'S':
             return True # True → "Sim, continue rodando o programa"
        elif value == 'N':
            print('Programa finalizado!')
            return False # False → "Não, pare o programa"
        else:
            print('Escolha entre [S/N]!')

# programa principal
while True:
    try:
        first_number = float(input('Insira um número: '))
        second_number = float(input('Insira o segundo número: '))
    except ValueError:
        print('ERRO: Valor inserido não é númerico!')
        continue

    operator = input('Insira um operador +, -, *, /  ').strip()
    if not operator:
        print('ERRO: Nenhum valor digitado')
        continue
    calculator(first_number, second_number, operator)
    if not remain():
        break

"""OU VERSÃO DO PROFESSOR"""

""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break

