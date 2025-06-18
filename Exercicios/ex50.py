print('Vamos saber se um número é primo ou não!')

contador = 0
numero = int(input('Insira um número inteiro: '))
for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1

if contador == 2:
    print(f'Esse número é {numero} primo')
else:
    print(f'Esse número {numero} não é primo!!')