conversor = float(input('Digite a medida em metros que o programa ira converter em cm, dc e mm: '))

decimetro = conversor * 10
centimetros = conversor * 100
milimetros = conversor * 1000

print('A altura em metros fica {}m\n A altura em diametros fica {}\n A altura em centimetros fica {}cm\n A altura em milimetros fica {}mm'.format(conversor, decimetro, centimetros, milimetros))

conversorDois = float(input('Digite a medida em metros que o programa ira converter em km, hm, dam: '))

quilometros = conversorDois / 1000
hectometro = conversorDois / 100
decametro = conversorDois / 10

print('A altura em metros é {}m\n Em quilometros {}km\n Em hectometro {}hm\n Em decametro {}dam\n'.format(conversorDois, quilometros, hectometro, decametro))
