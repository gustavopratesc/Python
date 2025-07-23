texto = input('Insira um texto ou palavra: ').strip()

contagem_letras = 0
contagem_numeros = 0

for i in texto:
    if i.isalpha():
        contagem_letras += 1
    elif i.isnumeric():
        contagem_numeros += 1


print(f'Contagem de caracteres: {len(texto)}')
print(f'Contagem de números do texto {contagem_numeros}')
print(f'Contagem de letras {contagem_letras}')
