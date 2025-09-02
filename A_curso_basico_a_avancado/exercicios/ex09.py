def cadastrar_usuario(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')



usuarios = {
    "nome": str(input('Insira o nome: ')).strip().title(),
    "idade": int(input('Insira a idade: ')),
    "cidade": str(input('Insira a cidade: ')).strip().title()
}

cadastrar_usuario(**usuarios)