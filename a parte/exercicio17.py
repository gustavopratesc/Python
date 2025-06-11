"""Você agora quer fazer um programa apenas para exercitar a sua lógica. Basicamente, você viu que
o IBGE faz uma consulta de 5 preços para ver a média de preços. Você resolveu fazer o seguinte:
ler os valores, calcular a média e verificar quais valores estão acima da média.
"""

primeiro_preco = float(input('Insira o primeiro preço: R$'))
segundo_preco = float(input('Insira o segundo preço: R$'))
terceiro_preco = float(input('Insira o terceiro preço: R$'))
quarto_preco = float(input('Insira o quarto preço: R$'))
quinto_preco = float(input('Insira o quinto preço: R$'))

media_preco = (primeiro_preco + segundo_preco + terceiro_preco + quarto_preco + quinto_preco) / 5

if primeiro_preco > media_preco:
    print('O primeiro preço R${} está acima da media R${}'.format(primeiro_preco, media_preco))
elif segundo_preco > media_preco:
    print('O segundo preço R${} está acima da media R${}'.format(segundo_preco, media_preco))
elif terceiro_preco > media_preco:
    print('O terceiro preço R${} está acima da media R${}'.format(terceiro_preco, media_preco))
elif quarto_preco > media_preco:
    print('O quarto preço R${} está acima da media R${}'.format(quarto_preco, media_preco))
elif quinto_preco > media_preco:
    print('O quinto preço R${} está aicma da media R${}'.format(quinto_preco, media_preco))
else:
    print('Insira os dados corretamente!!')