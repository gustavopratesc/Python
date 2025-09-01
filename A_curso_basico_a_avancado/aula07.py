lista = ['Maria', 'Helena', 'Luiz']

for indice, nome in enumerate(lista):
    print(f'{indice + 1}° {nome}')

def escopo():
    variavel = 'Local'
    print(variavel)

def soma(a, b):
    s = a + b
    return s # o return vai parar tudo e vai retornar o s

def soma2(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return print(f'O total da multiplicação foi {total}')

multiplicar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def mult(number):
    dup = number * 2
    trip = number * 3
    quad = number * 4
    return print(f'{number} x 2 = {dup}, {number} x 3 = {trip}, {number} x 4 = {quad}')

number2 = int(input('Insira um número: '))

mult(number2)

# ou

def criar_multiplicar(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicar(2)
print(duplicar(2))