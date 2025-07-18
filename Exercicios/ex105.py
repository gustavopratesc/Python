"""CRIE UMA FUNÇÃO LEIAINT() QUE VAI FUNCIONAR DE FORMA SEMELHANTE A FUNÇÃO INPUT() DO PYTHON, SO QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS VALOR NUMERICO
    EX: n = leiaint('Digite um n: ')
"""

def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Erro')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')