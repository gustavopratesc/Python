## REVISÃO DE CONTEUDOS

# nome = 'Gustavo Prates Caetano'
# idade = 21
# cidade = 'Vitoria da conquista'

# print(f'Olá meu nome é {nome}. Eu tenho {idade} anos e moro em {cidade} ')

# ##

# numeros = [10, 20, 30, 40, 50]

# soma = 0

# for numero in numeros:
#     soma += numero

# media = soma / len(numeros)

# print(f'A media é: {media}')

## 

# n1 = int(input('Insira o primeiro número: '))
# n2 = int(input('Insira o segundo número: '))

# soma = n1 + n2

# print(f'A soma entre {n1} e {n2} é igual a {soma}')

##

# nome = str(input('Insira seu nome: ')).strip().title()
# idade = int(input('Insira a sua idade: '))

# print(f'Olá, {nome}! Você tem {idade} anos.')

##

# numero = int(input('Insira um número para saber se é par ou impar: '))
# if numero % 2 == 0:
#     print(f'Esse número {numero} é par')
# else:
#     print(f'Esse número {numero} é impar')

##

# senha = str(input('Insira a sua senha: ')).strip()
# while True:
#     confirme_senha = str(input('Confirme sua senha: '))

#     if senha == confirme_senha:
#         print('Senha confirmada com sucesso!!')
#         break
#     else:
#         print('Senha errada insira novamente!')
#         continue

##
# soma = 0
# for i in range(1, 6):
#     numero = int(input('Insira 5 números para saber a media: '))
#     soma += numero

# media = soma / 5

# print(f'A media dos 5 números inseridos é {media}')

##
# numero = int(input('Insira o número para saber sua tabuada: '))
# print(f'A tabuada do número {numero} é:')    

# for i in range(1, 11):
#     print(f'{numero} x {i} = {numero * i}')
##

# count = 0
# while count < 10:
#     count += 1
#     print(count)

##

# count = 0
# while True:
#     numero = int(input('Insira números inteiros se for negativo o programa fecha: '))
#     if numero < 0:
#         print('Programa fechado!!')
#         break
#     count += 1 # <-- a ordem influencia a contagem de números
# print(f'Números inteiros inseridos {count}')

##

# numeros = []
# for i in range(1, 11):
#     numero = int(input('Insira números: '))
#     numeros.append(numero)



# print(f'Maior {max(numeros)}')
# print(f'Menor {min(numeros)}')

## ou

# maior = menor = None  # Começa sem valor

# for i in range(1, 11):
#     numero = int(input(f'Digite o {i}º número: '))
    
#     if maior is None or numero > maior: # se maior estiver sem valor ou numero for maior que valor
#         maior = numero # ai maior vai receber número
#     if menor is None or numero < menor: # mesma coisa que de cima
#         menor = numero

# print(f'Maior número: {maior}')
# print(f'Menor número: {menor}')

print('CAIXA ELETRONICO')
valor = int(input('Valor a sacar: '))
cedulas = [50, 20, 10, 1]

for cedula in cedulas:
    qtd, valor = divmod(valor, cedula)
    if qtd > 0:
        print(f'{qtd} de cedulas de R${cedula}')

print('Fim do saque')