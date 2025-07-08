"""CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VARIAS PESSOAS, GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO E TODOS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE:
A) QUANTAS PESSOAS FORAM CADASTRADAS
B) A MEDIA DE IDADE DO GRUPO
C) UMA LISTA COM TODAS AS MULHERES
D) UMA LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MEDIA"""

lista_pessoas = []
pessoa = {}
while True:
    pessoa['Nome'] = str(input('Nome: ')).strip().title()
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    lista_pessoas.append(pessoa.copy())
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in 'Ss':
            break
        elif c in 'Nn':
            print(f'Foram cadastradas {len(lista_pessoas)} pessoas')
            media_idades = sum(p['Idade'] for p in lista_pessoas) / len(lista_pessoas)
            # p['Idade'] for p in lista_pessoas → pega a idade de cada dicionário da lista.
            # sum(...) → soma todas as idades.
            # len(lista_pessoas) → divide pela quantidade de pessoas.
            print(f'Media de idades: {media_idades:.2f}')
            print('Todas as mulheres cadastradas: ')
            for p in lista_pessoas:
                if p['Sexo'] == 'F':
                    print(f'- {p["Nome"]}')
            
            print('Pessoas com idade acima da media: ')
            for p in lista_pessoas:
                if p['Idade'] > media_idades:
                    print(f'- {p["Nome"]}, {p["Idade"]} anos')

            exit()
        else:
            print('Opção invalida! Escolha [S/N]')

