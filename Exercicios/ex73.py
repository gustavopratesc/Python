quatro_valores = []
for i in range(1, 5):
    valores = int(input('Digite um valor 4 vezes: '))
    quatro_valores.append(valores)

tuple(quatro_valores) # <-- tuple serve para converter algo em tupla
if 9 in quatro_valores:
    posicao = quatro_valores.count(9)
    print(f'Apareceu o valor (9) {posicao} vezes')
else:
    print('O 9 não apareceu dessa vez')

if 3 in quatro_valores:
    print(f'Apareceu o valor (3) na posição {quatro_valores.index(3)}°')
else:
    print('O 3 não esta em nenhuma posição')

pares = 0
for num in quatro_valores:
    if num % 2 == 0:
        pares += 1

print(f'Contagem de números pares {pares}')


## ou de outra forma

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite um ultimo númeroo: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 aparaceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na posição {num.index(3) + 1}° posição')
else:
    print('Não apareceu o 3')
print('Os valores pares digitados foram', end='')
for n in num:
    if num % 2 == 0:
        print(n, end='')