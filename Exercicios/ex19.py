"""O NOME COM TODAS AS LETRAS MAIUSCULAS
NOME COM TODAS MINUSCULAS
QUANTAS LETRAS AO TOTAL SEM CONSIDERAR ESPAÇOS
QUANTAS LETRAS POSSUI O PRIMEIRO NOME
"""

nome = str(input('Insira seu nome completo: ')).strip()

print('Seu nome com letras maiusculas: {}'.format(nome.upper()))
print('Seu nome com letras minusculas: {}'.format(nome.lower()))
nome_sem_espaco = nome.replace(" ", "")
print('Contagem de caracteres: {}'.format(len(nome_sem_espaco)))
print('Contagem de caracteres: {}'.format(nome[0:7]))
#print('Contagem de caracteres primeiro nome: {}'.format(nome.find(' ')))
# ou
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]}, e a contagem de caracteres é {len(separa[0])}') # <-- mais didatico