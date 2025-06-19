print('Verificação se uma frase é palindromo!')
for i in range(1, 10):
    frase = str(input('Digite uma frase: ')).strip().lower()
    frase_modificada = frase.replace(" ", "")
    frase_modificada_invertida = frase_modificada[::-1]
    if frase_modificada == frase_modificada_invertida:
        print(f'Essa frase {frase_modificada} é palindroma da frase {frase_modificada_invertida}')
        break
    else:
        print(f'A frase "{frase}" NÃO é um palíndromo!')

print('FIM!')