"""Dessa vez, lhe iludiram e disseram que iam pagar para você fazer um programa, mas no fundo
você sabe que não vai receber. Você foi contratado para criar um programa de promoção do dia
1
do consumidor. Basicamente, você vai ler o total da compra de um consumidor e aplicar o
desconto conforme abaixo:
total compra desconto
< 50,00 5%
< 100,00 10%
< 200,00 20%
< 500,00 25%
>= 500, 00 30%
Por fim, você deve imprimir o valor total da compra após o desconto"""

total_compra = float(input('Insira o total da compra para ver se você ganha desconto: '))

if total_compra < 50:
    print('Você recebeu 5% de desconto!')
    desconto_cinco = total_compra * 0.05
    preco_cinco = total_compra - desconto_cinco
    print('Seu preço era R${} agora é R${}'.format(total_compra, preco_cinco))
elif total_compra < 100:
    print('Você recebeu 10% de desconto!')
    desconto_cem = total_compra * 0.10
    preco_cem = total_compra - desconto_cem
    print('Seu preço era R${} agora é R${}'.format(total_compra, preco_cem))
elif total_compra < 200:
    print('Você recebeu 20% de desconto!')
    desconto_vinte = total_compra * 0.20
    preco_vinte = total_compra - desconto_vinte
    print('Seu preço era R${} agora é R${}'.format(total_compra, preco_vinte))
elif total_compra < 500:
    print('Você recebeu 25% de desconto!')
    desconto_vinte_cinco = total_compra * 0.25
    preco_vinte_cinco = total_compra - desconto_vinte_cinco
    print('Seu preço era R${} agora é R${}'.format(total_compra, preco_vinte_cinco))
else:
    print('Você recebeu 30% de desconto!')
    desconto_trinta = total_compra * 0.30
    preco_trinta = total_compra - desconto_trinta
    print('Seu preço era R${} agora é R${}'.format(total_compra, preco_trinta))
    
    
    
    