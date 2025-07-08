aluno = {}

aluno['Nome'] = str(input('Insira seu nome: '))
aluno['Media'] = float(input('Insira a media: '))

print(f'O nome é {aluno["Nome"]}')
print(f'A media é {aluno["Media"]}')
if aluno['Media'] >= 6:
    print('Situação é igual a Aprovado!!')
else:
    print('Situação é Reprovado!!')
    