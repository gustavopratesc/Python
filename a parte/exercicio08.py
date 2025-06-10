"""O IBGE (Instituto Brasileiro de Geografia e Estatística) para definir um preço médio de um produto
alimentar, por exemplo: o feijão, faz consulta a pelo menos 5 mercados de tamanhos variados.
Após ler os valores dos 5 mercados, o instituto calcula o valor médio do produto. Diferente do que
era praticado antes, atualmente, o IBGE utiliza um pequeno sistema para computar o preço
médio. Você está trabalhando na equipe de TI do IBGE para calcular o preço médio dos produtos.
Lembre-se de ler os cinco preços, calcular a média e exibir o resultado.
"""

produtoUm = float(input('Digite o preço do primeiro produto R$'))
produtoDois = float(input('Digite o preço do segundo produto R$'))
produtoTres = float(input('Digite o preço do terceiro produto R$'))
produtoQuatro = float(input('Digite o preço do quarto produto R$'))
produtoCinco = float(input('Digite o preço do quinto produto R$'))

valorMedio = (produtoUm + produtoDois + produtoTres + produtoQuatro + produtoCinco) / 5

print('O valor medio desses produtos é R${}'.format(valorMedio))
