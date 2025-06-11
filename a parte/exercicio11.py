"""Sofia tem oitos anos e está aprendendo os números, os antecessores e os sucessores. Você
resolveu fazer um programa para ajudá-la a saber se um número é sucessor de outro. Você
basicamente pede como entrada um número, depois o suposto sucessor, por fim exibe se o
suposto sucessor é o sucessor mesmo. É tipo assim: Sofia insere os números: 23 e, depois, 24 e
você vai exibir: “O número 24 é sucessor de 23”, mas se Sofia colocar 23 e, depois, 26, você deve
exibir: “O número 26 não é sucessor de 23”"""

numero = int(input('Insira um número especifico para saber seu sucessor e antecessor!'))
sucessorOuAntecessor = int(input('Insira o número que você ache que é sucessor ou antecessor: '))

if sucessorOuAntecessor == numero + 1:
    print('Esse {} numero é sucessor do numero {}'.format(sucessorOuAntecessor, numero))
elif sucessorOuAntecessor == numero - 1:
    print('Esse {} número é antecessor do número {}'.format(sucessorOuAntecessor, numero))
else:
    print('Nenhum dos dois é sucessor ou antecessor do número fornecido')