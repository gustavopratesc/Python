"""Você quer viajar para fora do Brasil, mas ainda não escolheu o seu destino. Você está em dúvida
entre Europa, Canadá, Estados Unidos e Argentina. Você sabe que as moedas nessas regiões são:
euro, dólar canadense, dólar americano, peso argentino. Você queria um programa que você
desse o valor que deseja levar e as cotações do dia de cada moeda e imprimisse quanto em cada
moeda você teria. Então, resolveu que faria esse programa para você e sua mãe verem quanto de
dinheiro teriam em cada região.
"""

euro = 5.75
dolarCanadense = 3.90
dolarAmericano = 5.10
pesoArgentino = 0.006

real = float(input('Insira o número de reais que queria converter: R$'))

euroConvertido = real / euro
dolarCanadenseConvertido = real / dolarCanadense
dolarAmericanoConvertido = real / dolarAmericano
pesoArgentinoConvertido = real / pesoArgentino

print('O dinheiro em reais R${} em euro fica {:.2f}'.format(real, euroConvertido))
print('O dinheiro em reais R${} em dolar Canadense fica {:.2f}'.format(real, dolarCanadenseConvertido))
print('O dinheiro em reais R${} em dolar Americano fica {:.2f}'.format(real, dolarAmericanoConvertido))
print('O dinheiro em reais R${} em peso Argentino fica {:.2f}'.format(real, pesoArgentinoConvertido))
