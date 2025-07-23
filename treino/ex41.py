senha = str(input('Insira uma senha: '))
senha_cadastrada = 'admin123'

if senha in senha_cadastrada:
    print(f'Acesso autorizado')
else:
    print(f'Acesso negado')