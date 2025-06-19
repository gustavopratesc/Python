soma = 0
count = 0
for i in range(1, 7):
    numero = int(input('Digite qualquer número inteiro: '))
if soma % 2 == 0:
    soma += numero
    count += 1

print(f'São {count} pares e a soma é {soma}')