# numeros = []

# for i in range(1, 6):
#     valores_n = int(input('Insira os valores númericos: '))

#     if not numeros:
#         numeros.append(valores_n)
#         print(f'{numeros} adicionado como primeiro valor')
#     else:
#         inserido = False
#         for i in range(len(numeros)):
#             if valores_n < numeros[i]:
#                 numeros.insert(i, valores_n)
#                 print(f'{valores_n} adicionado na posição {i}')
#                 inserido = True
#                 break
#         if not inserido:
#             numeros.append(valores_n)
#             print(f'{valores_n} adicionado no final da lista')


# print(f'\nLista ordenada: {numeros}')

# lista = []

# for _ in range(1, 6):
#     numero = int(input('Insira um número: '))
    
#     if not lista:
#         lista.append(numero)
#         print('Adicionado ao final da lista')
#     else:
#         posicao = 0
#         while posicao < len(lista):
#             if numero < lista[posicao]:
#                 lista.insert(posicao, numero)
#                 print(f'Adicionado na posição {posicao} da lista')
#                 break
#             posicao += 1

# print(f'Lista ordenada {lista}')

##

lista = []

while True:
    n = int(input('Insira um número: '))
    if n in lista:
        print('Numero repetido insira novamente')
        continue
    if not lista:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(lista):
            if n < lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
        else:
            lista.append(n)
            print('Adicionado ao final da lista')
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'S':
        continue
    elif continuar in 'N':
        break
    else:
        print('Insira entre [S/N]')
        continue

print(f'Lista ordenada {lista}')
                

