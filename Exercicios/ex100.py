# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), QUE RECEBA VARIOS PARAMETROS COM VALORES INTEIROS
# SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES E DIZER QUAL DELES É O MAIOR.

## minha solução
from time import sleep

def maior(*num, delay = 0.5): # * é para desempacotar e receber varios parametros
    print('-' * 40)
    print(f'Analisando valores passados...')
    for v in (num): # o for v in (num) ou for i, v in enumarate(num)
        print(v, end=' ', flush=True)
        sleep(delay)
        

    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi o {max(num)}.')
    print(f'-' * 40)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)