"""Em um supermercado é comum que no caixa os produtos sejam passados até que finalize-se a
compra. Você deve fazer um programa que leia os preços dos produtos, até que o preço zero seja
informado. O total da compra deve ser informado no final. Você deve, basicamente, somar todos
os preços informados.
"""

soma_compra = 0

while True:
    compra = float(input('Insire o valor das compras / 0 Para finalizar e somar tudo: R$'))
    if compra == 0:
        break
    soma_compra += compra

print('O total da compra ficou R${}'.format(soma_compra))

