n1 = int(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = input('Terceiro número: ')

int_n3 = int(n3)

sum = n1 + n2 + int_n3

print(f'A soma dos números {n1} + {n2} + {int_n3} = {sum}')
print(f'Converti o {n3} que tava em {type(n3)} em {type(int_n3)}')