# Manipulando texto e strings
frase = 'Curso em video python'

#fatiamento

print(frase[9]) # <-- vai pegar ate o caracter 9 // começa a partir do 9 
print(frase[9:13]) # <-- vai pegar a partir do 9 e vai ate o 13 mas não pega o caracter 13 e sim o 12
print(frase[9:21]) # <-- outro exemplo o 21 puxa o caracter 20
print(frase[9:21:2]) # <-- começa 9 termina no 21 e pula de 2 em 2 caracteres
print(frase[:5]) # <-- começa do inicio 0 e termina no 5
print(frase[15:]) # <-- começa do 15 e vai até o fim
print(frase[9::3]) # <-- começa do 9 vai ate o final e pula de 3 em 3 caracteres

#Analisando Strings

print(len(frase)) # <-- vai analisar o comprimento (caracteres) da frase
print(frase.count('o')) # <-- vai contar quantos 'o' possui na frase
print(frase.count('o', 0, 13)) # <-- vai contar quantos 'o' tem começando do 0 terminando no 13
print(frase.find('deo')) # <-- vai me indicar onde começou e a posição onde começou
print(frase.find('Android')) # <-- apareceu -1 é porque 'Android' não existe na variavel frase
print('Curso'in(frase)) # <-- vai me indicar se possui a palavra na variavel mostrando true ou false

#Transformação Strings

print(frase.replace('python', 'Android')) # <-- vai subsituir python por android de uma forma secundaria
print(frase.upper()) # <-- vai deixar em maiusculo
print(frase.lower()) # <-- vai deixar em minusculo
print(frase.capitalize()) # <-- vai jogar todos os caracteres em minusculo e deixar so o 1 em maiusculo
print(frase.title()) # <-- vai deixar todos os 1 caracter em maiusculo [ Curso Em Video Python ]
print(frase.strip()) # <-- remove espaços inuteis da esquerda ou da direita
print(frase.rstrip()) # <-- remove os espaços inuteis da direita
print(frase.lstrip()) # <-- remove os espaços inuteis da esquerda

#Dividir strings

print(frase.split()) # <-- separa os caracteres em listas com todas as cadeias de caracteres 012 0123 01

#Juntar strings

print('-'.join(frase)) # <-- vai juntar a frase com o - hifen nos espaços