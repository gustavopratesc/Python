# Crie um programa em Python que:

# Permita ao usuário cadastrar vários alunos, informando:

# Nome do aluno

# Nota 1

# Nota 2

# Para cada aluno, o programa deve calcular a média das notas e armazenar os dados em uma lista de dicionários (ou tuplas, se preferir).

# Após o cadastro, o programa deve exibir um boletim geral, com:

# Nome dos alunos

# Média de cada um

# O programa deve permitir que o usuário consulte a nota individual de qualquer aluno, pelo número de identificação (posição na lista).

# O usuário pode cadastrar quantos alunos quiser (usar while ou loop com opção de continuar).

# A média é (nota1 + nota2) / 2.

# Exiba o boletim geral como uma tabela simples.

# Após exibir o boletim, permita ao usuário ver os detalhes de um aluno específico.

# Finalize o programa com uma mensagem de agradecimento.

print('Media alunos!')
print('+=' * 20)

media_alunos = [] # <-- vai criar uma lista de media de alunos

while True: # <-- um loop infinito, para parar precisa de uma condição
    nome_aluno = str(input('Insira o nome do aluno: ')).strip().title()
    nota_1 = int(input('Insira a primeira nota: '))
    nota_2 = int(input('Insira a segunda nota: '))
    media = (nota_1 + nota_2) / 2
    media_alunos.append((nome_aluno, nota_1, nota_2, media))

    while True:
        print('+=' * 20)# strip = espaços desnecessarios, title = Primeira letra maiuscula independente do espaço nas frases
        continuar = str(input('Quer continuar? [Sim/Não]: ')).strip().title() 
        print('+=' * 20)
        if continuar in ['Sim', 'S']: # se continuar for Sim ou S vai dar break nesse segundo (WHILE TRUE)
            break
        elif continuar in ['Não', 'Nao', 'N']: # (se nao se) vai mostrar o boletim geral
            print('=== BOLETIM GERAL ===')
            print('+=' * 20)
            for i, aluno in enumerate(media_alunos): # esse For eu nunca ouvi falar, mas ele roda na lista e pega a (posição i), o (nome do aluno), e a (media do aluno)
                print(f'[{i}] {aluno[0]} - Média: {aluno[3]}')
            ver_nota = str(input('Você quer ver a nota de algum aluno especifico?: ')).strip().title()
            if ver_nota in ['Sim', 'S']:
                posicao = int(input('Digite o número da posição do aluno especifico: '))
                if 0 <=  posicao < len(media_alunos): # se a posição for menor = a 0 e a quantidade da lista do array media alunos o programa vai imprimir
                     print(f'Aluno: {media_alunos[posicao][0]}') # o nome do aluno [posicao] <- é para identificar o número e não fazer uma quebra de caracter
                     print(f'1ª nota: {media_alunos[posicao][1]}') # nota 1
                     print(f'2ª nota: {media_alunos[posicao][2]}') # nota 2
                     print(f'Média: {media_alunos[posicao][3]}') # media
                else:
                    print(f'Posição invalida') 
            else:
                print('Programa Fechado!')
            exit() # vai fechar o programa geral
        else:
            print('Escolha entre Sim ou Não') # aqui vai rodar ate a pessoa escolher entre sim ou nao
    
