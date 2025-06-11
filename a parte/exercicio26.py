"""Quando crianças aprendemos as tabuadas dos números 2, 3, 4, assim em diante. Vamos criar a
tabuada do número que quisermos. O usuário deve informar o número que ele deseja a tabuada e
você deve imprimir a tabuada tal como abaixo:
Número da tabula: 5
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""
numero = int(input('Insira um número para saber a sua tabuada: '))
print('Tabuada de {}:'.format(numero))
for i in range(1, 11):
    print('{} X {} = {}'.format(numero, i, (numero * i)))