# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMA ESCREVA QUE RECEBA UM TEXTO QUALQUER COMO PARAMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTAVEL

# EX:
# escreva('Olá, Mundo!')
# SAIDA:
# -----------
# Olá, mundo!
# -----------

def escreva(texto):
    hifen = '-'
    if len(hifen) <= len(texto):
        novo_hifen = hifen * len(texto)
        print(novo_hifen)
        print(texto)
        print(novo_hifen)    


mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)

## ou 

def escreva(texto):
    borda = ('-' * 2) * len(texto)   # cria a linha com o mesmo tamanho do texto
    print(borda)
    print(texto)
    print(borda)

mensagem = input('Digite uma mensagem: ')
escreva(mensagem)