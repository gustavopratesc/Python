"""A professora Alice precisa fazer o mesmo cálculo de médias de seus alunos, porém, ela precisa
fazer isso para todos os seus 25 alunos. Calcule a média final para todos os 25 alunos.
"""

soma_nota = 0

for i in range(1, 26):
    nota = float(input('Insira a nota dos seus 25 alunos: '))
    soma_nota += nota

media_nota = soma_nota / 25

print('A media de notas de seus 25 alunos ficou: {}'.format(media_nota))