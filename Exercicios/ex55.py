sexo = ''

while sexo not in ['M', 'F']:
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()
    if sexo not in ['M', 'F']:
        print('Entrada inválida! Tente novamente.')

print(f'Sexo {sexo} registrado com sucesso!')

## outros exercicios

idade = None

while True:
    idade = int(input('Insira sua idade: '))
    if idade < 0 or idade > 120:
        print('Idade inválida. Tente novamente.')
    else:
        print(f'Sua idade esta correta {idade} anos')
        break

## outros exercicios

while True:
    senha = str(input('Digite sua senha: ')).strip()
    senha_novamente = str(input('Confime sua senha: ')).strip()
    if senha == senha_novamente:
        print('Senha Validada!')
        break
    else:
        print('Digite novamente!')

## outros exercicios

while True:
    menu = int(input("""
                     [1] Cadastrar usuario
                     [2] Ver usuarios
                     [3] Sair
                     Resposta: """))
    if menu == 1:
        print('Você entrou no cadastramento de usuario: ')
        break
    elif menu == 2:
        print('Você quer ver quais usuarios?: ')
        break
    elif menu == 3:
        print('Você quer sair do programa? [S/N]: ')
        sair = 'S'
        sair = str(input('S/N')).upper().strip()
        if sair == 'S':
            print('Programa fechado!')
            break
        else:
            print('Resposta invalida!')
    else:
        print('Opção inválida. Tente de novo')