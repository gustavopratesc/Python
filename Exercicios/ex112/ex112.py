"""CRIE UM PEQUENO SISTEMA MODULARIZADO QUER PERMITE CADASTRAR PESSOAS PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES. O SISTEMA SO VAI TER 2 OPÇÕES: CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS"""

from modulos import nova_pessoa, nova_mensagem
from time import sleep
from dados import pessoas

while True:
        nova_mensagem('MENU PRINCIPAL')
        print('\033[34m1 - Ver pessoas cadastradas\033[m')
        print('\033[34m2 - Cadastrar nova Pessoa\033[m')
        print('\033[34m3 - Sair do sistema\033[m')
        print('-' * 30)
        while True:
            try:
                opcao = int(input('\033[33mSua Opção: \033[m'))
                if opcao == 1:
                    if len(pessoas) == 0:
                        print('Nenhuma pessoa cadastrada!')
                    else:
                        nova_mensagem('PESSOAS CADASTRADAS')
                        for p in pessoas:
                            print(f'Nome: {p[0]} | Idade: {p[1]}')
                            print('-' * 30)
                elif opcao == 2:
                    nova_mensagem('NOVO CADASTRO')
                    nome = str(input('Nome: ')).strip().title()
                    idade = int(input('Idade: '))
                    nova_pessoa(nome, idade)
                elif opcao == 3:
                    print('Saindo do sistema...')
                    sleep(0.5)
                    print('Programa fechado')
                    exit()
                else:
                    print('\033[31mOpção invalida!! Digite 1, 2 ou 3\033[m')
            except ValueError:
                print('\033[31mErro! Insira um número inteiro valido\033[m')