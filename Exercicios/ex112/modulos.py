
from dados import pessoas

def nova_pessoa(nome, idade):
    pessoas.append((nome, idade))
    print(f'Novo registro de {nome} adicionado!.')
                    

def nova_mensagem(msg):
    print('-' * 30)
    print(f'     {msg}     ')
    print('-' * 30)
