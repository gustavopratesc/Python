### functions def

def mostrar_Linha():
    print('---------------')


mostrar_Linha()
print('Testando functions DEF')
mostrar_Linha()


def mensagem(msg): ## msg é um parametro que tem q colocar dentro da function se vc quiser que ela seja flexivel para outras coisas
    print('----------')
    print(msg) # <-- aqui e com o msg tem como inserir mensagens atraves do nome da function
    print('----------')

mensagem('Sistema de alunos') # <-- com o msg tem como inserir atraves de mensagem('alguma coisa') 
mensagem('Inserindo na function')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma entre A + B = {s}')

#soma(a = int(input('Insira um n: ')), b = int(input('Insira outro n: '))) # teste
# OU
pri = int(input('Numero: '))
seg = int(input('Numero: '))
soma(pri, seg) # <-- vai puxar os números para os parametros (a, b)
soma(b=4, a=5)
soma(8, 9)
soma(2, 1)

## EMPACOTAMENTO E DESEMPACOTAMENTO
 ## com TUPLAS
# def contador(*num):
#     for valor in num:
#         print(valor, end=' ')
#     print('FIM')
def contador(*num): # o * recebe varios valores
    quantidade = len(num)
    print(f'Recebi os valores {num} e são {quantidade} números')

contador(2, 1, 7)
contador(5, 7, 8, 9)
contador(1, 3, 8, 5, 4)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)


## COM LISTAS


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1

valores = [7, 4, 5, 0, 2]
dobra(valores)
print(valores)