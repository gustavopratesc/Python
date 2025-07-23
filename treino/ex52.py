numero = int(input('Insira um número para tabuada: '))
tabuada = int(input('Insira o numero onde quer parar a tabuada: '))

for i in range(0, tabuada + 1):
    print(f'{numero} x {i} = {numero * i}')