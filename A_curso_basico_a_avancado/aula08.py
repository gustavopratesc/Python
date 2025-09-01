# revisando dicionairos

# pessoa = {
#     'nome': 'Gustavo',
#     'sexo': 'M',
#     'idade': 21,
#     'altura': 1.70,
#     'endereços': [
#         {'rua': 'Palmares', 'numero': 35}
#     ]
# }

# print(pessoa['endereços'][0]['rua'])
# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])

# metodos uteis dos dicionarios em python
# len - quuantas chaves
# keys - itera sobre as chaves
# values - itera sobre os valores
# items - itera sobre as chaves e os valores
# setdefault - adiciona um novo item
# copy - retorna uma copia rasa (shallow copy)
# get - obtem uma chave
# pop - apaga um item
# popitem - apaga o ultimo item
# update - atualiza um dicionario

perguntas = [
    {
        'pergunta': 'Quanto e 2 + 2?',
        'opçoes': ['1', '2', '3', '4'],
        'resposta': '4'

    },
    {
        'pergunta': 'Quanto é 5 * 5?',
        'opçoes': ['25', '55', '10', '51'],
        'resposta': '25'
    },
    {
        'pergunta': 'Quanto é 10 / 2?',
        'opçoes': ['4', '5', '6', '2'],
        'resposta': '5'
    },
]

def jogar():
    for pergunta in perguntas:
        print('Pergunta:', pergunta['pergunta'])
        print('Opções: ')
        for i, opcao in enumerate(pergunta['opçoes']):
            print(f'{i + 1}) {opcao}')
        escolha = int(input('Resposta: ')) - 1
        resposta = pergunta['opçoes'][escolha]

        if resposta == pergunta['resposta']:
            print('Acertou')
        else:
            print('Errou')
        print()

jogar()

# def jogar():
#     for pergunta in perguntas:
#         print('Pergunta:', pergunta['pergunta'])
#         print('Opções: ')
#         for i, opcao in enumerate(pergunta['opçoes']):
#             print(f'{i + 1}) {opcao}')

#         escolha = int(input('Digite o número da opção: ')) - 1
#         resposta = pergunta['opçoes'][escolha]

#         if resposta == pergunta['resposta']:
#             print('Acertou!')
#         else:
#             print('Errou!')
#         print()

# jogar()
