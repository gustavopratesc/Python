"""CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO E CARTEIRA DE TRABALHO E CADASTRE-OS (COM IDADE) EM UM DICIONARIO SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, O DICIONARIO RECEBERÁ TAMBEM O ANO DE CONTRATAÇÃO E O SALÁRIO. CALCULE E ACRESCENTE ALEM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR"""
from datetime import datetime
ano_atual = datetime.now().year

pessoa_trabalhadora = {}

pessoa_trabalhadora['Nome'] = str(input('Insira seu nome: ')).strip().title()
pessoa_trabalhadora['Ano_nascimento'] = int(input('Insira o seu ano de nascimento: '))
idade = ano_atual - pessoa_trabalhadora['Ano_nascimento']
pessoa_trabalhadora['CTPS'] = int(input('Insira o número da sua carteira de trabalho [0 se não tiver]: '))
if pessoa_trabalhadora['CTPS'] != 0:
    pessoa_trabalhadora['Contratacao'] = int(input('Insira o ano de contratação: '))
    pessoa_trabalhadora['Salario'] = float(input('Salário: R$ '))
    idade_aposentadoria = (pessoa_trabalhadora['Contratacao'] - pessoa_trabalhadora['Ano_nascimento']) + 30 
    print('=-' * 30)
    print(f'O seu nome é: {pessoa_trabalhadora["Nome"]}')
    print(f'A sua idade é: {idade}')
    print(f'CTPS: {pessoa_trabalhadora["CTPS"]}')
    print(f'Primeiro ano de contratação: {pessoa_trabalhadora["Contratacao"]}')
    print(f'Seu salário atual: R${pessoa_trabalhadora["Salario"]}')
    print(f'Você vai se aposentar com: {idade_aposentadoria} anos')
elif pessoa_trabalhadora['CTPS'] == 0:
    print(f'O seu nome é: {pessoa_trabalhadora["Nome"]}')
    print(f'A sua idade é: {idade}')
    print('Você não possui CTPS ainda!')
else:
    print('Digite valores corretos!')

