lista = [[], []]

for i in range(7):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    elif n % 2 == 1:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()
print(f'Numeros pares: {lista[0]}')
print(f'Numeros impares: {lista[1]}')

## ou


