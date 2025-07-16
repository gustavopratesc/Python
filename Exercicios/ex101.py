"""FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS E DUAS FUNÇÕES CHAMADAS SORTEIO() E SOMAPAR() A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCA-LOS DENTRO DE UMA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR."""

from random import randint
from time import sleep

numeros = []
def sorteio():
    print('Sorteando 5 valores da lista!: ', end='')
    for _ in range(5):
        num = randint(1, 20)
        numeros.append(num)
        print(f'{num} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


sorteio() # <-- n esquece de chamar a função 


def soma_par():
    soma = 0
    for v in (numeros):
        if v % 2 == 0:
            soma += v
    print(f'A soma dos números pares dessa lista {numeros} é igual a {soma}')

soma_par()


    
