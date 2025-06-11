"""Na sua escola, você faz três avaliações no ano e a sua nota final é a média aritmética dessas três
avaliações. Para você ser aprovado sua média deve ser maior ou igual a 7.0 pontos, caso contrário
você estará reprovado. Faça um programa para ler suas notas e dizer se você está aprovado ou
reprovado.
"""

primeira_nota = float(input('Insira a sua primeira nota: '))
segunda_nota = float(input('Insira a sua segunda nota: '))
terceira_nota = float(input('Insira a sua terceira nota: '))

media_notas = (primeira_nota + segunda_nota + terceira_nota) / 3

if media_notas >= 7:
    print('Aprovado!!')
elif media_notas < 7 and media_notas >= 5:
    print('Recuperação!!')
else:
    print('Reprovado!!')