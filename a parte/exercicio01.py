"""Você trabalha em um supermercado e no caixa que você trabalha o consumidor só pode comprar
um único produto, mesmo que várias unidades repetidas. Você deseja otimizar o seu trabalho e
criar um programa que leia o preço do produto e a quantidade de itens comprados e informe o
total da compra para o usuário.
"""

precoProduto = float(input("Insira o preço do produto: R$"))
quantidadeProduto = int(input("Insira q quantidade de produtos comprados: R$"))

totalCompra = precoProduto * quantidadeProduto

print('O preço do produto foi R${} a quantidade foi {} o total da compra foi R${}'.format(precoProduto, quantidadeProduto, totalCompra))