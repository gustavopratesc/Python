# Funções + return
# Crie uma função dobro(n) que recebe um número e retorna o dobro dele.
# Crie uma função area_retangulo(l, h) que retorna a área de um retângulo.
# Crie uma função par_ou_impar(n) que retorna "Par" se o número for par ou "Ímpar" caso contrário.

def dobro(n):
    return n * 2

try:
    n = int(input('Digite um número: '))
    print(f'O dobro de {n} é: {dobro(n)}')
except ValueError:
    print('ERRO: Valor digitado não é número inteiro!')


def area_retangulo(b, a):
    area = b * a
    return area
try:
    base = float(input('Insira a base: '))
    altura = float(input('Insira a altura: '))
    print(f'A area do retangulo é {area_retangulo(base, altura)}')
except ValueError:
    print('ERRO: Valor inserido não númerico!')

def par_ou_impar(number):
    if number % 2 == 0:
        return f'Esse número {number} é par'
    else:
        return f'Esse número {number} é impar'
    
try:
    number = int(input('Insira o número: '))
    print(par_ou_impar(number))
except ValueError:
    print('ERRO: VALOR inserido não é NÚMERICO INTEIRO')