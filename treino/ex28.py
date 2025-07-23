from math import factorial

num = int(input('Insira o número: '))
f = 1
for i in range(num, 0, -1):
    f *= i
    print(f'{i} -> Parcial: {f}')

print(f'O fatorial de {num} é {f}')