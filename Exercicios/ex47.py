from time import sleep
print('Tabuada')
sleep(1)

numero = int(input('Informe o número que queira saber a tabuada: '))

print(f'A tabuada desse número {numero} é:')
for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')