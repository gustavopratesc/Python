def concatena_palavras(*palavras):
    palavras_juntas = " ".join(palavras)
    return palavras_juntas
    

lista_palavras = []

while True:
    palavra = str(input('Insira uma palavra: ')).strip()
    if not palavra:
        if not lista_palavras:
            print('ERRO: Nenhuma palavra digitada!')
            continue
        else:
            print(f'Frase final: {concatena_palavras(*lista_palavras)}')
            break


    lista_palavras.append(palavra)