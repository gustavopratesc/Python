frase = 'Olá, bom dia!'.lower().strip()
palavra = str(input('Digite uma palavra e vê se ela esta na frase: ')).lower().strip()

if palavra in frase:
    print(f'Sim a palavra {palavra} esta na tambem na frase {frase.capitalize()}')
else:
    print('Não está')