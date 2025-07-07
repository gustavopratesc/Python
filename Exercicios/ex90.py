alunos_notas = []

while True:
    nome = str(input('Nome aluno: ')).strip().title()
    nota = float(input('Nota aluno: '))
    nota2 = float(input('Nota 2 aluno: '))
    media = (nota + nota2) / 2
    alunos_notas.append([nome, nota, nota2, media])
    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in ['SIM', 'S']:
            break
        elif c in ['NÃO', 'NAO', 'N']:
            print('.....BOLETIM.....')
            for i, p in enumerate(alunos_notas):
                print(f'{i} - Nome aluno: {p[0]} || Media: {p[3]}')
                print('-=' * 20)
            while True:
                nota_individual = int(input('Quer ver notas individuais? Digite a posição do aluno ou valor negativo para finalizar o programa: '))
                if nota_individual < 0:
                    print('Finalizando o programa...')
                    exit()
                elif nota_individual >= 0 and nota_individual < len(alunos_notas): # Se o número digitado para consultar o aluno for válido (não negativo e dentro do número de alunos cadastrados), o programa pega aquele aluno na lista e mostra o nome dele junto com as duas notas que ele tirou.
                    aluno = alunos_notas[nota_individual]
                    print(f'Nome: {aluno[0]} || Nota 1: {aluno[1]} || Nota 2: {aluno[2]}')
                else:
                    print('Posição invalida tente novamente!!')
        else:
            print('Escolha entre [S/N]')