"""CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA POSSUI
    O NOME SILVA EM SEU NOME
"""

nome = str(input('Insira seu nome completo: ')).strip().title()

palavra_a_procurar = 'Silva'

if palavra_a_procurar in nome:
    print(f'O nome Silva esta presente: {nome}')
else:
    print(f'O nome Silva não esta presente: {nome}')



## TOMA CUIDADO COM O AS LETRAS MAIUSCULAS E MINUSCULAS
teste = input('NOME: ')

silva = 'Silva'in(teste)

print(silva)