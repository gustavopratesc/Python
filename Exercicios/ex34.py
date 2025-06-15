"""Escreva um programa para aprovar o emprestimo
    bancario para a compra de uma casa. O programa
    vai perguntar o valor da casa, 
    o salario do comprador e em quantos anos ele vai pagar
    Calcule o valor da prestação mensal sabendo
    que ela não pode execer 30% do salario
    ou então o emprestimo sera negado.
"""

valor_da_casa = float(input('Insira o valor da casa: R$'))
salario_comprador = float(input('Insira o salário do comprador: R$'))
quantos_anos_pagar = int(input('Insira quantos anos você quer pagar: '))

prestacao_mensal = valor_da_casa / (quantos_anos_pagar * 12) # <-- vai calcular o valor da casa / pelos meses totais
limite = salario_comprador * 0.3 # <-- vai calcular 30% do salario do comprador

if prestacao_mensal <= limite:
    print(f'Aprovado')
    print(f'Você ira pagar R${prestacao_mensal:.2f} durante {quantos_anos_pagar} anos')
else:
    print(f'Reprovado emprestimo negado!!')
