
countMil = 0
total_compra = 0
mais_barato_nome = ''
mais_barato_preco = float('inf')

while True:
    nome_produto = str(input('Insira o nome do produto: ')).strip()
    preco = float(input('Insira o preço do produto R$ '))

    total_compra += preco

    if preco > 1000:
        countMil += 1

    if preco < mais_barato_preco:
        mais_barato_preco = preco
        mais_barato_nome = nome_produto    
    
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    
    if continuar in ['SIM', 'S']:
        continue
    elif continuar in ['NÃO', 'NAO', 'N']:
        print('Programa fechado!!')
        break
    else:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()



print(f'O total gasto da compra foi R${total_compra:.2f}')
print(f'Contagem de produtos valor mais de mil reais: {countMil}')
print(f'O produto mais barato foi: {mais_barato_nome}, e o preço foi R$ {mais_barato_preco:.2f}')