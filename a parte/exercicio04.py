"""Maria amou o programa que você fez para ela de calcular a área dos terrenos, mas ela possui outro
grande problema: alguns terrenos não possuem lados uniformes, assim, ela precisa, muitas vezes,
informar, além da área, o perímetro do terreno. Ela confirmou a você que todos os terrenos só
possuem quatro lados. Você sabe que para calcular o perímetro do terreno basta somar todos os
lados. Dessa forma, você confirmou a ela que faria esse programa de calcular perímetro.
"""

primeiroLado = float(input('Insira o primeiro lado: '))
segundoLado = float(input('Insira o segundo lado: '))
terceiroLado = float(input('Insira o terceiro lado: '))
quartoLado = float(input('Insira o quarto lado: '))

perimetro = primeiroLado + segundoLado + terceiroLado + quartoLado

print('O perimetro é igual a: {}'.format(perimetro))
