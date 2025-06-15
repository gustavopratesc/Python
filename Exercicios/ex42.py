print('Pagamento de produtos')
print('=+' * 20)

preco = float(input('Insira o preço a se pagar: R$'))
metodo = str(input('Insira o metodo a se pagar: dinheiro/cheque, debito, cartão 2x, cartão 3x: ')).lower().strip()
novo = None

if metodo in ('dinheiro', 'cheque', 'dinheiro/cheque'):
    novo = preco - (preco * 0.10)
    print('Você recebeu 10% de desconto')
elif metodo in ('cartão', 'a vista', 'debito'):
    novo = preco - (preco * 0.05)
    print('Você recebeu 5% de desconto')
elif metodo in ('credito 2x', 'cartão 2x', '2x'):
    novo = preco
elif metodo in ('credito 3x', 'cartão 3x', '3x', '4x', '12x'):
    novo = preco + (preco * 0.20)
    print('Você ira pagar 20% a mais de juros')
else:
    print('Insira os dados corretamente!!')

print(f'Você ira pagar R${novo}')
