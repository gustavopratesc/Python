altura = float(input('Insira o tamanho da altura: '))
largura = float(input('Insira o tamanho da largura: '))

area = altura * largura
quantTinta = area / 2

print('A altura é {altura} A largura é {largura}\nA area é {area}m² e a quantidade de tinta necessaria por 2 metros quadrados é {quantTinta}L'.format(altura=altura, largura=largura, area=area, quantTinta=quantTinta))