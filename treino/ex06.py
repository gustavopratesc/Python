print('    CALCULADORA SIMPLES     ')
n1 = float(input('Insira um número: '))
n2 = float(input('Insira outro número: '))
operacao = input('Insira uma operação: + - * /: ')
if operacao == '+':
    result = n1 + n2
elif operacao == '-':
    result = n1 - n2
elif operacao == '*':
    result = n1 * n2
elif operacao == '/':
    result = n1 / n2
else:
    print('Escolha as opções corretas!')

print(f'O resultado da operação foi: {result}')