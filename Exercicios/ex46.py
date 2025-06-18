soma = 0
for i in range(0, 501):
    if i % 2 == 1:
        if i % 3 == 0:
            print(i)
            soma += i
print(soma)

# ou

soma = 0
for i in range(1, 501, 2):  # vai de 1 até 500 pulando de 2 em 2 (só ímpares)
    if i % 3 == 0:
        print(i)
        soma += i
print(soma)