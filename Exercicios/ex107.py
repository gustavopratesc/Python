"""FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON. O USUARIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. QUANDO O USUARIO DIGITAR A PALAVRA 'FIM', O PROGRAMA SE ENCERRARA.
    OBS: USE CORES  
"""

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# PROGRAMA PRINCIPAL
comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!')