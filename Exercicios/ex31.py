"""FAÇA UM PROGRAMA QUE LEIA 3 NUMEROS E DIGA QUEM É MAIOR OU MENOR"""

primeiro_numero = int(input('Insira o primeiro número: '))
segundo_numero = int(input('Insira o segundo número: '))
terceiro_numero = int(input('Insira o terceiro número: '))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    print(f'O {primeiro_numero} é o maior')
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    print(f'O {segundo_numero} é o maior')
else:
    print(f'O {terceiro_numero} é o maior')

##

primeiro = int(input('Insira o primeiro número: '))
segundo = int(input('Insira o segundo número: '))
terceiro = int(input('Insira o terceiro número: '))

# Maior número
maior = primeiro
if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

# Menor número
menor = primeiro
if segundo < menor:
    menor = segundo
if terceiro < menor:
    menor = terceiro

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')