"""O zoom é uma plataforma de busca dos preços mais baixos da web para um mesmo produto. Ele
além de mostrar o menor valor encontrado, apresenta também o preço médio do produto nos
últimos trinta dias. Para encontrar o menor preço, o programa lê 6 preços durante o mês e
encontra o menor deles. Você deve encontrar o menor preço do produto durante o mês.
"""

menor_valor = None
soma_produtos = 0

for i in range(1, 7):
    preco = float(input('{} // Preço do produto: R$'.format(i)))
    soma_produtos += preco

    
    if menor_valor is None or preco < menor_valor:
        menor_valor = preco

media_preco = soma_produtos / 6


print('A media de preços é {:.2f}'.format(media_preco))
print('O menor preço é R${}'.format(menor_valor))