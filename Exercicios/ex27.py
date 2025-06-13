"""ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO 
SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO
A MULTA VAI CUSTAR R$7 A CADA KM ACIMA DO LIMITE
"""
## POSSO FAZER COM RANDOM.RANDINT PRA DEIXAR MAIS INTUITIVO TAMBEM
import random
import time
print('Medindo velocidade do carro...')
time.sleep(2)
velocidade_carro = random.randint(0, 120)

if velocidade_carro > 80:
    print(f'Você foi multado a velocidade do seu carro esta {velocidade_carro}KM')
    km_acima = velocidade_carro - 80
    multa = km_acima * 7
    print(f'Sua multa sera de R${multa:.2f}')
else:
    print(f'Você esta dentro dos parametros!! KM {velocidade_carro}')



