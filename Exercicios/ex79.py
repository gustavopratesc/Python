# Desafio 1 – Lista crescente manual
# Leia 5 números e insira no final da lista, depois mostre a lista.
# Sem ordenação.
# Use .append() apenas.

# numeros = []
# for i in range(1, 6):
#     n = int(input('Insira um número para armazenar na lista: '))
#     numeros.append(n)

# print(f'Lista de números: {numeros}')

# Desafio 2 – Evitar duplicatas
# Faça o usuário inserir números até digitar 0. Não deixe inserir número repetido.
# Use if n in lista para evitar repetição.

# nnumeros = []
# while True:
#     nn = int(input('Insira um número (não pode repetições) para armazenar na lista: '))
#     if nn in nnumeros:
#         print('Não pode repetições!')
#         print('=' * 20)
#         continue
#     if nn == 0:
#         print('Programa finalizado!!')
#         break

#     nnumeros.append(nn)

# print(f'Os números na lista são {nnumeros}')

# Após o usuário inserir 5 números, diga quais são os maiores e menores e em quais posições eles aparecem.
# Use enumerate().

numeros = []

for i in range(1, 6):
    n = int(input('Digite um número (nao pode repetir) ou (0 para finalizar antes) para armazenar na lista: '))
    if n in numeros:
        print('Não pode repetições')
        print('=' * 20)
        continue
    if n == 0:
        print('Programa finalizado!!')
        break

    numeros.append(n)

if numeros:
    maior = max(numeros)
    menor = min(numeros)

    print(f'O maior número foi {maior} nas posições: ', end=' ')
    for i, v in enumerate(numeros):
        if v == maior:
            print(f'{i} ', end='')

    print(f'O menor número foi {menor} nas posições: ', end=' ')
    for i, v in enumerate(numeros):
        if v == menor:
            print(f'{i} ', end='')
else:
    print('Nenhum número inserido!')



