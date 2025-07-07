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


print('-' * 10, 'Matriz', '-' * 10)
lista = []
pares = []
for linha in range(3):
    nova_linha = []
    for coluna in range(3):
        valor = int(input(f'Digite o valor para [{linha}, {coluna}]: '))
        nova_linha.append(valor)
        if valor % 2 == 0:
            pares.append(valor)
    lista.append(nova_linha)

for linha in lista:
    for valor in linha:
        print(f'{valor:^5}', end='')
    print()
print(f'Soma de valores pares: {sum(pares)}')
soma_terceira_coluna = sum(linha[2] for linha in lista)
print(f'Soma de valores da terceira coluna: {soma_terceira_coluna}')
maior = max(lista[1])
print(f'Maior valor da segunda linha: {maior}')
