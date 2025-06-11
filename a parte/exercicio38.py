# O dólar, assim como qualquer outra moeda relativamente estável, tem o seu valor flutuante. Uma
# empresa de câmbio normalmente monitora os valores máximos da cotação do dólar comercial
# para realizar transações no final do dia. Você deve ler os valores de cotação que são liberados de
# 30 em 30 minutos das 08h da manhã até às 17h. Esses dados serão informados de uma única vez
# no final do dia corrente. Você deve ao fim exibir o valor máximo de cotação.
import time
from datetime import datetime

tempo_inicio = datetime.now().replace(hour=8, minute=0)
tempo_final = datetime.now().replace(hour=20, minute=38)

valores = []

while True:
    tempo_atual = datetime.now()
    cotacao = float(input('Insira o valor da cotação: R$'))
    valores.append(cotacao)

    time.sleep(5)

    esta_na_hora = tempo_atual >= tempo_inicio and tempo_atual <= tempo_final

    if not esta_na_hora:
        break


ordenacao_valores = sorted(valores)
array_to_string = ', '.join(str(x) for x in ordenacao_valores)

print('A ordenação dos valores minimos pros maximos é: {}'.format(array_to_string))
    
