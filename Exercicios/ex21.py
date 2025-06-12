"""CRIE UM PROGRAMA QUE LEIA SE A CIDADE COMEÇA OU NÃO COM NOME SANTO"""

cidade = str(input('Insira o nome da cidade: ')).strip()

if 'Santo'in(cidade[0:6].lower()):
    print('Sim a cidade possui o primeiro nome Santo')
else:
    print('Não a cidade não possui o nome Santo')

print(f'Nome de sua cidade: {cidade}')
"""
OU ASSIM TAMBEM VERSION GPT

cidade = input('Insira o nome da cidade: ').strip()

if cidade[:5].lower() == 'santo':
    print('Sim, a cidade começa com o nome "Santo".')
else:
    print('Não, a cidade não começa com o nome "Santo".')

"""
