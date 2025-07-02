tabela_futebol = (
    'Flamengo',
    'Cruzeiro',
    'Bragantino',
    'Palmeras',
    'Bahia',
    'Fluminense',
    'Atlético-MG',
    'Botafogo',
    'Mirassol',
    'Corinthians',
    'Grêmio',
    'Ceará',
    'Vasco',
    'São Paulo',
    'Santos',
    'Vitória',
    'Internacional',
    'Fortaleza',
    'Juventude',
    'Sport'
)

print('---Campeonato Futebol Brasileiro!---')
print(f'Lista de times do campeonato brasileiro {tabela_futebol}')
print('+=' * 20)
print(f'Os cinco primeiros colocados {tabela_futebol[0:5]}')
print('+=' * 20)
print(f'Os quatro ultimos colocados {tabela_futebol[-4:]}')
print('+=' * 20)
print(f'Os times em ordem alfabetica {sorted(tabela_futebol)}')
print('+=' * 20)
if 'Chapecoense' in tabela_futebol:
    posicao = tabela_futebol.index('Chapecoense') + 1
    print(f'A chapecoense esta na posição {posicao} da tabela!')
else:
    print('A chapecoense não esta na tabela!')
