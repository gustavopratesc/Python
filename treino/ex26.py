from math import sqrt

n1 = int(input('Insira um número: '))
n2 = int(input('Insira outro número: '))

rn1 = sqrt(n1)
rn2 = sqrt(n2)

if rn1 > rn2:
    print(f'O 1° numero {n1} tem sua raiz {rn1:.2f} que é maior que a raiz do 2° numero {n2} raiz: {rn2:.2f}')
else:
    print(f'A raiz do número 2 {rn2:.2f} é maior que numero 1 {rn1:.2f}')