print(12, 34, sep="-")
print(56, 78, sep="-") # sep de separador
print(56, 78, sep="-", end=" ") # end = final do print

name = 'Gustavo'
surname = 'Prates Caetano'
age = 21
birth_year = 2004
legal_age = age >= 18
heigth = 1.70

print(f'Nome: {name}')
print(f'Sobrenome: {surname}')
print(f'Idade: {age}')
print(f'Ano de nascimento: {birth_year}')
print(f'É maior de idade?: {legal_age}')
print(f'Altura em metros: {heigth:.2f}')

# + adição, - subtração, * multiplicação, / divisão, % resto divisão, // divisão inteira, ** potencia

# concatenação

concatenação = 'A' + 'B' + 'C'
print(concatenação)

# precedencia

# ()
# **
# * / // %
# + -

nome_imc = input('Insira seu nome: ').strip()
altura = float(input('Insira sua altura: '))
peso = float(input('Insira seu peso: '))

imc = peso / (altura * altura)

print(f'Seu nome é {nome_imc} seu IMC é {imc:.2f}')