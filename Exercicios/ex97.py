# FAÇA UM PROGRAMA QUE TENHA UMA DEF CHAMADA AREA(), QUE RECEBA DIMENSÕES DE UM TERRENO RETANGULAR
# (LARGURA E COMPRIMENTO) E MOSTRE A AREA DO TERRENO!

print('CONTROLE DE TERRENOS')
print('-' * 20)
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area do seu terreno é {largura}x{comprimento} é de {area:.1f}m².')

## 1° maneira
#area(largura= float(input('Largura (m): ')), comprimento= float(input('Comprimento (m): ')))

## 2° maneira

larg = float(input('Largura (m): '))
compri = float(input('Comprimento (m): '))

area(larg, compri) # não esqueça de chamar a função