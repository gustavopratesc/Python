## Faça um programa que tenha uma função chamada contador(), que receba três parametros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens atraves da função criada:
# a) de 1 ate 10 de 1 em 1 
# b) de 10 ate 0 de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(inicio, fim, passo, delay=0.5):

    if passo == 0: # se o passo for zero o passo recebe 1 então n tem problema se a pessoa digitar 0
        passo = 1
    passo = abs(passo) # retorna sempre um número positivo

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True) # <-- faz aparecer o número imediatamente no print
            sleep(delay)
        
    elif inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            sleep(delay)
    print(f'FIM')

    

contador(1, 10, 1)
contador(10, 0, 2)
primeiro = int(input('Digite o inicio: '))
segundo = int(input('Digite o fim: '))
terceiro = int(input('Digite o passo: '))
contador(primeiro, segundo, terceiro)




## ou for do professor

def contador(i, f, p):
    if p <= 0:
        p *= -1
    print('-=' * 20)
    print(f'Contagem de {i} ate o {f} de {p} em {p}')
    sleep(2.5)


    if i < f:
        cont = 1
        while cont <= f:
            print(f'{c} ', end='', flush=True) # <-- o flush vai fazer a contagem com 0.5 milisegundos
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = 1
        while cont >= f:
            primeiro(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')
    



# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)