"""Você saiu com seus amigos para ir ao cinema. Depois de assistirem o filme, vocês foram para um
restaurante comemorar o aniversário de sua amiga, Alice. Na hora de pagar a conta, como sempre,
foi aquele furdunço, divide daqui, divide dali. Então, você pensou: vou fazer um programa para
calcular a conta por pessoa em um aniversário. Claro que a aniversariante não conta. Deste modo,
você faria um programa que lesse o total da conta, divide-a pelo número de pessoas na mesa,
menos o aniversariante. Depois, você só precisa exibir quanto cada um tem que pagar.
"""

totalConta = float(input('Digite o total da conta: R$'))
numeroPessoa = int(input('Digite o número de pessoas (menos aniversariante): '))

totalAPagar = totalConta / numeroPessoa

print('Tem que pagar R${:.2f} para cada {} pessoa'.format(totalAPagar, numeroPessoa))