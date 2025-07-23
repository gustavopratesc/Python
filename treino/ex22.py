from math import ceil, floor

n = float(input('Insira um número decimal: '))

cima = ceil(n)
baixo = floor(n)

print(f'Arredondamento do numero {n} para cima {cima}')
print(f'Arredondamento do numero {n} para baixo {baixo}')