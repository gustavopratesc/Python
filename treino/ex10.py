try:
    n1 = float(input('Insira um número: '))
    n2 = float(input('Insira outro número: '))
except ValueError:
    print(f'Insira um valor númerico!')
    exit()
opcao = str(input('OPERAÇÃO: + - * /: ')).strip()
if opcao == '+':
    result = n1 + n2
elif opcao == '-':
    result = n1 - n2
elif opcao == '*':
    result = n1 * n2
elif opcao == '/':
    result = n1 / n2
else:
    print('Escolha as operações corretas!')

print(f'Resultado: {result}')