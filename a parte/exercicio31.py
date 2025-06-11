"""A professora Alice precisa calcular a média das notas dos seus alunos. Os alunos possuem quatro
notas bimestrais. A média final do aluno é a média aritmética das notas. Calcule e imprima a
média de um aluno.
"""

soma_notas = 0

for i in range(1, 5):
    nota = float(input('Insira a nota do seu aluno: '))
    soma_notas += nota

media_notas = soma_notas / 4

print('A media de nota de seu aluno é: {}'.format(media_notas))