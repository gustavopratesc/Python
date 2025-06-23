soma = 0
count = 0
while True:
    numero = int(input('Insira um número: e digite 999 para parar e somar: '))
    if numero == 999:
        break
    soma += numero
    count += 1
    
print(f'A soma de números é igual a: {soma}')
print(f'Números inseridos: {count}')