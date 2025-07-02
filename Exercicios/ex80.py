# Desafio 4 – Inserção ordenada simples
# Leia 5 números. Cada um deve ser inserido já em ordem crescente (sem .sort()).
# Mesmo que o que você já fez

# numeros = []

# for i in range(5):
#     num = int(input('Insira um número: '))
#     if not numeros or num > numeros[-1]:
#         numeros.append(num)
#         print(f'Esse número foi para o final da lista!')
#     else:
#         for i in range(len(numeros)):
#             if num <= numeros[i]:
#                 numeros.insert(i, num)
#                 print(f'Esse número foi para a posição {i}')
#                 break

# print(f'Lista formatada: {numeros}')

# Desafio 5 – Inserção ordenada com verificação de repetição
# Agora só insira se o número não existir na lista. Se repetir, avise e ignore.
# Similar ao último código que você fez.

# lista = []

# for i in range(6):
#     n = int(input('Insira números para armazenar na lista: '))
#     if n in lista:
#         print('Número repetido insira novamente!!')
#         print('=-' * 20)
#         continue
#     if not lista or n > lista[-1]:
#         lista.append(n)
#         print('Foi para o final da lista!')
#     else:
#         for i in range(len(lista)):
#             if n <= lista[i]:
#                 lista.insert(i, n)
#                 print(f'Esse número {n} foi para a posição {i}')
#                 break

# print(f'Lista formatada {lista}')

# Desafio 6 – Inserção ordenada com limite

# O usuário pode inserir quantos quiser, mas apenas números entre 10 e 99 serão aceitos e inseridos de forma ordenada.

# lista = []

# while True:
#     n = int(input('Insira números entre 10 e 99: '))
#     if n in lista:
#         print('Número repetido digite outro!!')
#         print('-=' * 20)
#         continue
#     if n < 10 or n > 99:
#         print('Insira novamente!!!!')
#         print('=-' * 20)
#         continue
#     if not lista or n > lista[-1]:
#         lista.append(n)
#         print('Adicionado ao final da lista!')
#     else:
#         for i in range(len(lista)):
#             if n <= lista[i]:
#                 lista.insert(i, n)
#                 print(f'O numero {n} foi para a posição {i}')
#                 break

#     while True:
#         continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
#         if continuar in ['s', 'sim', 'si']:
#             break
#         elif continuar in ['n', 'nao', 'não']:
#             print('Programa finalizado!!')
#             print(f'Lista formatada {lista}')
#             exit()
#         else:
#             print('Insira entre [S/N]!')

##

# Foco: Controle de lista, lógica condicional, criatividade

# Desafio 7 – Separar pares e ímpares

# Peça 10 números. Depois, separe-os em duas listas: uma com pares e outra com ímpares. Mostre ambas ordenadas (com .sort() desta vez, só pra treinar).

# Desafio 8 – Inserção com soma acumulada

# A cada número inserido, mostre a soma total da lista e sua média.

# Desafio 9 – Lista reversa interativa

# O usuário insere valores até digitar "fim". Ao final, exiba a lista do último para o primeiro, sem usar .reverse().

# Desafio 10 – Ranking de pontuação

# O usuário digita nomes e notas de 5 pessoas. Ao final, mostre a lista de nomes ordenada da maior para a menor nota, sem usar .sort().

pares = []
impares = []




