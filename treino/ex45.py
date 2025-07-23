ano = int(input('Insira um ano: '))

bixsexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

if bixsexto:
    print(f'O ano {ano} é bixsexto!')
else:
    print(f'Não é')