"""Faça um programa que tenha uma função chamada ficha() que receba dois parametros opcionais: nome do jogador e quantos gols ele marcou. O programa devera ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente."""

def ficha(nome_jogador = '', gols=0):
    print('-' * 30)
    if nome_jogador.strip() == '':
        ## nome_jogador = '<desconhecido>'
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato'
    elif nome_jogador == ''.strip() and gols is None:
        gols = 0
        return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato'
    elif gols is None:
        return f'O jogador {nome_jogador} fez {gols} gol(s) no campeonato'
    else:
        return f'O jogador {nome_jogador} fez {gols} gol(s) no campeonato'

nome = str(input('Insira nome do jogador: ')).strip().title()
gols = input(f'Insira os gols do {nome}: ').strip()

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(ficha(nome, gols))

## ou o codigo mais otimizado

def ficha(nome_jogador='', gols=0):
    print('-' * 30)
    if nome_jogador.strip() == '':
        nome_jogador = '<desconhecido>'
    return f'O jogador {nome_jogador} fez {gols} gol(s) no campeonato'

# Entrada de dados com tratamento
nome = input('Insira o nome do jogador: ').strip().title()
gols_input = input(f'Insira os gols de {nome or "o jogador"}: ').strip()

# Verificação e conversão segura
if gols_input.isnumeric():
    gols = int(gols_input)
else:
    gols = 0

# Chamada da função
print(ficha(nome, gols))
