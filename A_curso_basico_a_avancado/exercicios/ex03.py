def registrar_usuario(nome, lista=None):
    return f'Nome: {nome} | Lista: {lista}'

lista_usuarios = []

while True:
    nome = str(input('Insira o nome: ')).strip().title()
    lista_usuarios.append(nome)
    if not nome:
        print('-' * 20)
        print('ERRO: Nenhum nome digitado!')
        continue
    else:
        print(registrar_usuario(nome, lista_usuarios))
    