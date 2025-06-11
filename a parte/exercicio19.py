"""Um baralho contém 52 cartas de 4 tipos (naipes) diferentes: paus, espadas, copas e ouro. Em cada
naipe, que consiste de 13 cartas, 3 dessas cartas contêm as figuras do rei, da dama e do valete,
respectivamente. Faça um programa que leia um número de 1 a 13 e informe qual carta o número
representa por extenso. Lembrando que temos algumas cartas especiais: 1 (Ás), 11 (Jalete), 12
(Rainha), 13 (Rei).
"""

"""
numero_carta = int(input('Insira um número entre 1 a 13 para saber informções sobre as cartas: '))

if numero_carta == 1:
    print('Isso é um Ás possui em todas as pintas!!')
elif numero_carta > 1 and numero_carta <= 10:
    print('Isso são cartas que representam números de 2 a 10: {}'.format(numero_carta))
elif numero_carta == 11:
    print('Isso é um Valete possui em todas as pintas!!')
elif numero_carta == 12:
    print('Isso é uma Dama possui em todas as pintas!!')
elif numero_carta == 13:
    print('Isso é um Rei possui em todas as pintas!!')
else:
    print('Escreva um número entre 1 a 13!!')
"""


primeiro_preco = float(input("Insira o primeiro valor: R$ "))
segundo_preco = float(input("Insira o segundo valor: R$ "))
terceiro_preco = float(input("Insira o terceiro valor: R$ "))
quarto_preco = float(input("Insira o quarto valor: R$ "))
quinto_preco = float(input("Insira o quinto valor: R$ "))

precos = []

precos.append(primeiro_preco)
precos.append(segundo_preco)
precos.append(terceiro_preco)
precos.append(quarto_preco)
precos.append(quinto_preco)

media = sum(precos) / len(precos)
print(f"A média dos preços é: R$ {media}")

for preco in precos:
		if preco > media:
				print(f"O preço R$ {preco} está acima da média.")
		elif preco < media:
				print(f"O preço R$ {preco} está abaixo da média.")
		else:
				print(f"O preço R$ {preco} é igual à média.")