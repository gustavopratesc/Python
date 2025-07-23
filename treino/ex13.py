try:
    numero = int(input('Insira um número: '))
except ValueError:
    print('Insira um número inteiro!')
    exit()

dobro = numero * 2
triplo = numero * 3
raiz = numero ** 0.5

print(f'Dobro do número: {dobro}')
print(f'Triplo do número: {triplo}')
print(f'Raiz do número: {raiz}')
