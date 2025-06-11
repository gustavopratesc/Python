"""A equipe de meteorologia de um jornal precisava calcular a temperatura média semanal em
determinada localidade. Para tal, são feitas as leituras das máximas dos sete dias de uma semana.
Por fim, a temperatura média deve ser exibida.
"""

soma_temperatura = 0

for i in range(1, 8):
    temperatura = float(input('Insira a temperatura semanal para saber sua media: '))
    soma_temperatura += temperatura

media_temperatura = soma_temperatura / 7

print('A media de temperatura de 1 semana é igual a: {:.2f}'.format(media_temperatura))