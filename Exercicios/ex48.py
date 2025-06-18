soma = 0

for i in range(1, 7):
    numero = int(input('Digite qualquer número inteiro: '))
    soma += numero
if soma % 2 == 0:
    print(f'O número par é esse {soma}')
else:
    print('Não quereros número impar')