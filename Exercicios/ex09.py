preco = float(input('Insira o preço do produto. Você ira receber 5% de desconto!!: '))
desconto = preco * 0.05
novopreco = preco - desconto

print('O preço antigo era R${:.2f} agora com desconto ficou R${:.2f}'.format(preco, novopreco))

# R${:.2f} <-- formata para casa 2 casas decimais
# ou novopreco = preco - (preco * 5 / 100) <--- formula sem variavel