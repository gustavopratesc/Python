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

# pares = []
# impares = []

# for i in range(1, 11):
#     n = int(input('Insira números para saber par e impar: '))
#     if n % 2 == 0:
#         pares.append(n)
#     else:
#         impares.append(n)

# pares.sort()
# impares.sort()

# print(f'Números pares {pares}')
# print(f'Números impares {impares}')


# contador = 0
# soma = []

# while True:
#     n = int(input('Insira um número: '))
#     contador += 1
#     soma.append(n)
#     continuar = int(input('Insira 1 para continuar 0 para fechar: '))
#     if continuar == 1:
#         continue
#     else:
#         media = sum(soma) / contador
#         print(f'A media da lista forcenida é {media:.2f}')
#         break



# lista = []

# while True:
#     entrada = str(input('Insira um valor ou (fim para terminar:) ')).strip().lower()
#     if entrada in ['fim']:
#         for i in range(len(lista)-1, -1, -1):
#             print(lista[i])
#         break
#     else:
#         lista.append(entrada)
#         print('Você resolveu continuar insira mais um valor!')

# Desafio 10 – Ranking de pontuação

# O usuário digita nomes e notas de 5 pessoas. Ao final, mostre a lista de nomes ordenada da maior para a menor nota, sem usar .sort().

ranking = []

for i in range(1, 6):
    nome_pessoa = str(input('Insira o nome: ')).strip().title()
    nota_pessoa = float(input('Insira a nota: '))
    pessoa = [nome_pessoa, nota_pessoa]

    if not ranking or nota_pessoa < ranking[-1][1]:
        ranking.append(pessoa)
        print('Essa pessoa foi para ultimo da lista! ')
    else:
        for i in range(len(ranking)):
            if nota_pessoa > ranking[i][1]:
                ranking.insert(i, pessoa)
                print(f'O nome foi {nome_pessoa} A nota foi {nota_pessoa} sua posição {i}')
                break
        
print('Ranking final: ')
for i, aluno in enumerate(ranking, 1):
    print(f'{i}° lugar: {aluno[0]} com nota {aluno[1]}')

    