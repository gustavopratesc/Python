palavra = str(input('Insira uma palavra: ')).strip().lower()
vogais = 0
for letra in palavra:
    if letra in 'aeiou':
        vogais += 1

print(f'Essa palavra tem {vogais} vogais')