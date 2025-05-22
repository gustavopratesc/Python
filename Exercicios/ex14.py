from math import hypot
catetoOposto = float(input('Insira o cateto oposto do triangulo retangulo: '))
catetoAdjacente = float(input('Insira o cateto adjacente do triangulo retangulo: '))

hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('Cateto oposto {} | Cateto Adjacente {} | Hipotenusa {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa))

# jeito sem modulo importado vv

co = float(input('Insira o primeiro cateto: '))
ca = float(input('Insira o segundo cateto: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {}'.format(hi))