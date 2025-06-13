"""
DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS E DIGA AO USUARIO SE ELAS PODEM OU NÃO FORMAR UM TRIANGULO
"""

print('Descubra se as retas podem formar um triangulo!!')

primeira_reta = int(input('Insira o comprimento da primeira reta: '))
segunda_reta = int(input('Insira o comprimento da segunda reta: '))
terceira_reta = int(input('Insira o comprimento da terceira reta: '))

triangulo = primeira_reta + segunda_reta > terceira_reta and primeira_reta + terceira_reta > segunda_reta and segunda_reta + terceira_reta > primeira_reta

if triangulo:
    print('Sim pode formar um triangulo!')
else:
    print('Não pode formar um triangulo!!')