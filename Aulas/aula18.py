## 2 parte funções DEF
help() # pedir ajuda no terminal vc escreve oq vc quer e pede ajuda no help

## docstrings
# abre 3 aspas duplas
def contador(i, f, p):
    """
    Aqui escreve como funciona a def
    """

## alguns parametros de def
# indicar o 0 pois se a pessoa escrever apenas 2 numeros o 0 vai fazer q n dê erro na DEF
def soma(a= 0, b= 0, c=0): 
    s = a + b + c
    print(f'Soma {s}')

soma(1, 2)
soma(5, 6, 1)

## ESCOPO DE VARIAVEIS

def teste():
    x = 1
    print(f'Na function teste a variavel x vale {x}')
    print(f'Na function teste a variavel n vale {n}')
#programa principal
n = 2 # funciona tanto fora da def quanto dentro pois ela n esta em um escopo fechado
print(f'No programa principal a variavel n vale {n}')
teste()
# print(f'No programa principal a varial x vale {x}') <-- isso aqui n funciona ja que a variavel x esta em outro escopo no caso da function DEF teste

## exemplo tem como criar variaveis com o mesmo nome so que em escopos diferentes

def funcao():
    n1 = 2
    print(f'O n1 dentro da def vale {n1} // ESCOPO INTERNO')

funcao()
n1 = 4
print(f'O n1 fora da def vale {n1} // ESCOPO EXTERNO')

"""MAS"""

def funcao():
    global n1 # <-- se utilizar o global o N1 de fora que conta que vale o n4
    n1 = 2
    print(f'O n1 dentro da def vale {n1} // ESCOPO INTERNO')

funcao()
n1 = 4
print(f'O n1 fora da def vale {n1} // ESCOPO EXTERNO')


## RETORNO DE VALORES

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # o S vai para as variaveis r1 r2 r3

r1 = somar(1, 2, 3)
r2 = somar(4, 7, 2)
r3 = somar(6, 2, 1)

print(f'Os resultados foram {r1} {r2} e {r3}')


## EXEMPLOS

def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input('Digite um numero para saber seu fatorial'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

## ou outra forma

f1 = fatorial(3)
f2 = fatorial(4)
f3 = fatorial(7)

print(f'Os resultados são {f1} {f2} {f3}')

## EXEMPLO COM BOOLEANS

def par(num=0):
    if num & 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número'))
print(par(num))
# ou
if par(num):
    print('É par')
else:
    print('É impar')