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



## mini validaçao de sexo
## if pessoa in ['MF']:
##      print('sexo aceito')

## codigo de outra forma

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).title().strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Porfavor digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    galera.append(pessa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
        if resp == 'N':
            break
print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas')
media = soma / len(galera)
print(f'A media de idade é de {media}')
print('As mulheres é cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da media: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
pessoa('Encerrado')