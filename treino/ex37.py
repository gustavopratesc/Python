frase = 'Você quer ser alguma'
frase_modificada = str(input('Insira uma palavra ou frase: ')).strip().title()

print(frase.replace('alguma', frase_modificada))
print(frase.split())
print('*'.join(frase))