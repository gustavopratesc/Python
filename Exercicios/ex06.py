tabuada = int(input('Insira um número para saber sua tabuada: '))

vezesUm = tabuada * 1 
vezesDois = tabuada * 2
vezesTres = tabuada * 3
vezesQuatro = tabuada * 4
vezesCinco = tabuada * 5
vezesSeis = tabuada * 6
vezesSete = tabuada * 7
vezesOito = tabuada * 8
vezesNove = tabuada * 9
vezesDez = tabuada * 10

print('----------------------------')
print('A tabuada desse número {} é\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}\n {}'.format(tabuada, vezesUm, vezesDois, vezesTres, vezesQuatro, vezesCinco, vezesSeis, vezesSete, vezesOito, vezesNove, vezesDez))
print('----------------------------')

# outra forma seria

num = int(input('Digite um número para saber a sua tabuada: '))

print('-----------------------------------')
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('-----------------------------------')
