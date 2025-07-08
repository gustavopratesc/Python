# print('-' * 10, 'Matriz', '-' * 10)
# lista = []
# for linha in range(3):
#     nova_linha = []
#     for coluna in range(3):
#         valor = input(f'Digite o valor para [{linha}, {coluna}]: ')
#         nova_linha.append(valor)
#     lista.append(nova_linha)

# for linha in lista:
#     for valor in linha:
#         print(f'{valor:^5}', end='')
#     print()


# print('-' * 10, 'Matriz', '-' * 10)
# lista = []
# pares = []
# for linha in range(3):
#     nova_linha = []
#     for coluna in range(3):
#         valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
#         nova_linha.append(valor)
#         if valor % 2 == 0:
#             pares.append(valor)
#     lista.append(nova_linha)

# for linha in lista:
#     for valor in linha:
#         print(f'{valor:^5}', end='')
#     print()
# print(f'Soma de valores pares: {sum(pares)}')
# soma_terceira_coluna = sum(linha[2] for linha in lista)
# print(f'Soma de valores da terceira coluna: {soma_terceira_coluna}')
# maior = max(lista[1])
# print(f'Maior valor da segunda linha: {maior}')


## fazendo com explicação

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para  [{linha}, {coluna}]:'))

# print('-' * 30)
# for i in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[i][c]:^5}]', end='')
#     print()


##

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior = soma_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para  [{linha}, {coluna}]:'))

print('-' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end='')
        if matriz[i][c] % 2 == 0:
            soma_par += matriz[i][c]
    print()

print(soma_par)
for l in range(0, 3):
    soma_coluna += matriz[i][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')