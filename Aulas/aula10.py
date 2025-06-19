## WHILE <-- mesma coisa que as outras linguagens, so muda a sintaxe
## while usado quando não sabe o limite, (e tambem sabendo o limite mas é melhor o FOR)
contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# ou outro exemplo

soma_nota = 0
contador_nota = 0

while True:
    nota = float(input('Insira a nota dos seus alunos: '))
    contador_nota += 1
    if nota == 0:
        break

    soma_nota += nota
    media_nota = soma_nota / contador_nota

print(f'A media de nota de seus {contador_nota} alunos é igual a {media_nota:.2f}')

# ou outro exemplo

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')

# ou outro exemplo

r = 'S'
while r == 'S':
    number = int(input('Digite o numero:'))
    r = str(input('Quer continuar? [S/N]')).upper()
print('FIM')