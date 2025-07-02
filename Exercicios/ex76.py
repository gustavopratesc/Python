numeros = []
for i in range(0, 6):
    numeros.append(int(input('Digite um valor númerico: ')))

print(f'O maior valor foi {max(numeros)} Sua posição foi {numeros.index(max(numeros)) + 1}..')
print(f'O menor valor foi {min(numeros)} Sua posição foi {numeros.index(min(numeros)) + 1}..')

## ou

numeros = []
for i in range(0, 6):
    numeros.append(int(input('Digite um valor numérico: ')))

maior = max(numeros)
menor = min(numeros)

print(f'\nO maior valor foi {maior}. Sua(s) posição(ões):', end=' ')
for i, valor in enumerate(numeros):
    if valor == maior:
        print(i + 1, end=' ')

print(f'\nO menor valor foi {menor}. Sua(s) posição(ões):', end=' ')
for i, valor in enumerate(numeros):
    if valor == menor:
        print(i + 1, end=' ')

