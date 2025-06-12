"""Peça para o usuário digitar uma frase. Em seguida:
Mostre os 10 primeiros caracteres.
Mostre do caractere 5 até o 15.
Mostre a frase pulando de 2 em 2.
"""

#frase = str(input('Insira uma frase: ')).strip()

#print(f'Os 10 primeiros caracteres da frase: {frase[0:11]}')
#print(f'Caracteres de 5 a 15: {frase[5:16]}')
#print(f'Pulando de 2 em 2 caracteres: {frase[::2]}')

"""
Com base na frase "Estudando Python com dedicação":
Quantos caracteres essa frase tem?
Quantas vezes a letra o aparece?
Qual a posição onde começa a palavra Python?
"""

#frase = 'Estudando Python com dedicação'
#frase_sem_espaco = frase.replace(" ", '')
#print(f'A frase python possui {len(frase_sem_espaco)} caracteres')
#print(f'A palavra (o) aparece {frase.count('o')} vezes')
#print(f'A palavra Python aparece na posição {frase.find('Python')}')

"""
Exercício 3 – Verificando conteúdo
Verifique se a palavra dedicação existe na frase "Estudando Python com dedicação". Mostre uma mensagem verdadeira ou falsa.
"""

#frase = 'Estudando Python com dedicação'.lower()

#if 'dedicação' in frase:
#    print(f'Sim a palavra dedicação esta na frase: {frase}')
#else:
#    print(f'Não esta!!')


"""
 Exercício 4 – Substituindo palavras
Peça ao usuário para digitar uma frase com a palavra "chatGPT" e:
Troque "chatGPT" por "PythonGuru".
Mostre a frase em letras maiúsculas.
Mostre a frase em letras minúsculas.
"""

#print('Digite uma palavra com chatGPT')
#frase = str(input('Digite agora a frase: '))

#frase_modificada = frase.replace('chatGPT', 'PythonGuru')
#print(frase_modificada)
#print(frase_modificada.upper())
#print(frase_modificada.lower())

"""
Peça para o usuário digitar o nome completo e:
Mostre o nome com apenas a primeira letra maiúscula (capitalize()).
Mostre o nome com a primeira letra de cada palavra em maiúsculo (title()).
"""

#nome = input('Insira seu nome completo: ')

#print(f'Seu nome com apenas 1 letra maiuscula {nome.capitalize()}')
#print(f'Seu nome formato normal {nome.title()}')

"""
Dada a string ' Python é incrível! ':
Remova os espaços da direita.
Remova os espaços da esquerda.
Remova todos os espaços desnecessários dos dois lados.
"""

#frase =  ' Python é incrível! '
#frase_direita = frase.rstrip()
#frase_esquerda = frase.lstrip()
#frase_dois_lados = frase.strip()

#print(frase_direita)
#print(frase_esquerda)
#print(frase_dois_lados)

"""
Peça ao usuário que digite uma frase com 3 palavras. Em seguida:
Divida essa frase em palavras usando split().
Mostre cada palavra separadamente.
"""

#frase_tres = input('Insira 3 palavras separadas por espaço: ')
#frase_separada = frase_tres.split()

#primeira = frase_separada[0]
#segunda = frase_separada[1]
#terceira = frase_separada[2]

#print(primeira)
#print(segunda)
#print(terceira)

