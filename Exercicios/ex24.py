"""FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA
    E MOSTRE O PRIMEIRO E O ULTIMO NOME DELA SEPARADAMENTE

    EX:
    ANA MARIA DE SOUZA
    PRIMEIRO = ANA
    ULTIMO = SOUZA
"""

nome = str(input('Digite seu nome completo: ')).strip().title()

nome_partes = nome.split()

primeiro_nome = nome_partes[0]
ultimo_nome = nome_partes[-1]

print(f'Seu primeiro nome: {primeiro_nome}')
print(f'Seu ultimo nome: {ultimo_nome}')