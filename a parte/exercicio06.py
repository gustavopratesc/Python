"""O Bar do Boca é um bar conhecido na sua cidade. Todas as sextas-feiras, o bar tem música ao vivo
e um novo cardápio a cada mês. O dono do bar, Boca, não sabe mais o que fazer com as contas
que são fechadas erradas, pois os garçons esquecem de adicionar a taxa de couvert ou esquecem
1
que a gorjeta sai de 10% para 20%. Você que conhece o Boca há muito tempo resolveu ajudá-lo.
Você vai fazer um programa que ler o total da conta e acrescenta 20% da gorjeta e a taxa fixa do
couvert.
"""

totalConta = float(input("Digite o total da conta: R$"))

acrescimo = totalConta * 0.20

contaComAcrescimo = totalConta + acrescimo

print('A conta normal ficou R${} mas teve acrescimo de 20% agora ficou R${}'.format(totalConta, contaComAcrescimo))