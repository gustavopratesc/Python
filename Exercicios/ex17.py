import random

aluno1 = input('Digine o nome do 1 aluno que deseja sortear: ')
aluno2 = input('Digine o nome do 2 aluno que deseja sortear: ')
aluno3 = input('Digine o nome do 3 aluno que deseja sortear: ')
aluno4 = input('Digine o nome do 4 aluno que deseja sortear: ')

lista = [aluno1, aluno2, aluno3, aluno4] # jeito mais correto <--

random.shuffle(lista)
print('A ordem de alunos para sorteio é {}'.format(lista))