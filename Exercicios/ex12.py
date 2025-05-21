dia = int(input('Quantos dias alugados?: '))
km = float(input('Quantos KM rodados?: '))

diasAlugados = dia * 60
kmRodados = km * 0.15
total = diasAlugados + kmRodados
# ou poderia ser assim --> total = (dia * 60) + (km * 0.15) <-- seria mais eficiente poupando memoria
print('Preço por dias alugados e KM rodados: R${:.2F}'.format(total))