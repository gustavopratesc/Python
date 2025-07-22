"""Reescreva a função leiaint() que fizemos no desafio anterior, incluindo agora a possibilidade da digitação de um número do tipo invalido aproveite e crie tambem uma função leiafloat() com a mesma funcionalidade"""

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return n 

num = leiaint('Digite um valor inteiro: ')
print(f'O valor inteiro digitado foi {num}')

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número flutuante valido')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return n
        
num_float = leiafloat('Digite um valor flutuante: ')
print(f'O valor flutuante digitado foi {num_float}')

