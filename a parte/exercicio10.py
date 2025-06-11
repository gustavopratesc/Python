"""Uma loja de tintas deseja informar para os clientes o melhor custo-benefício na compra de suas
tintas. Você foi contratado para desenvolver um programa que deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6
metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em
galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta a serem
compradas e os respectivos preços em 3 situações:
a. comprar apenas latas de 18 litros;
b. comprar apenas galões de 3,6 litros;
c. misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10%
de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

areaPintada = float(input('Insira em metros a area a ser pintada: m²'))

lataTinta = 18
precoLata = 80
galaoTinta = 3.6
precoGalao = 25
misturaGalaoELata = (galaoTinta * lataTinta) * 0.10
precoMistura -= misturaGalaoELata

print('Se você comprar latas de 18 litros o preço sai por R${} lembrando que 1 litro equivale a 6 metros'.format(precoLata / areaPintada))
print('Se você comprar galões de 3.6 litros o preço sai por R${} lembrando que 1 litro equivale a 6 metros'.format(precoGalao / areaPintada))
print('Se você misturar o galão e a lata você ganha desconto de 10%'.format(precoMistura))
