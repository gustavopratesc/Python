nota1 = float(input('Insira a sua primeira nota: '))
nota2 = float(input('Insira a sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 10:
    print('Aprovado!!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!!')
elif media >= 0 and media < 5:
    print('Reprovado')
else:
    print('Insira os dados corretamente!!')

