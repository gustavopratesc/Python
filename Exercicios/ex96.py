"""CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONARIO INCLUINDO O TOTAL DE GOLS FEITO DURANTE O CAMPEONATO
APRIMORE O DESAFIO PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, INCLUINDO UM SISTEMA DE VISUALIZAÇAO DE DETALHES DE APROVEITAMENTO DE CADA JOGADOR.
"""
## gols vai ser guardado na lista
lista_jogadores = []

while True:
    print('-' * 20)
    jogador = {}
    quantidade_gols = []

    jogador['Nome'] = str(input('Insira o nome do jogador: ')).strip().title()
    jogador['Partidas'] = int(input('Quantas partidas ele jogou: '))

    for i in range(jogador['Partidas']):
        gols = int(input(f'Quantos gols ele fez na {i + 1} partida?: '))
        quantidade_gols.append(gols)
    
    jogador['Gols'] = quantidade_gols[:]
    jogador['Total'] = sum(quantidade_gols)

    lista_jogadores.append(jogador.copy())

    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in ['SIM', 'S']:
            break
        elif c in ['NÃO', 'NAO', 'N']:
            print('----- VIZUALIZAÇÃO DE JOGADORES -----')  
            for i, j in enumerate(lista_jogadores):
                print(f'{i} Nome: {j["Nome"]} - Gols: {j["Gols"]} - Total: {j["Total"]}')
                
            exit()
        else:
            print('Escolha entre [S/N]!!')