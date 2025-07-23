n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

operacao = str(input('Insira uma operação: (+, -, *, /): '))

if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*':
    resultado = n1 * n2
elif operacao == '/':
    resultado = n1 / n2
else:
    print(f'Escolha as operações corretas!')

print(f'O resultado fica: {resultado}')