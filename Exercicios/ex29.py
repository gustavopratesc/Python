"""DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTANCIA
    DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM,
    COBRANDO R$0,50 POR VIAGENS DE ATE 200KM
    E R$0.45 PARA VIAGENS MAIS LONGAS.
"""

distancia_viagemkm = float(input('Insira a distancia em KMs para calcular o preço da passagem: '))

if distancia_viagemkm <= 200:
    primeiro_preco = distancia_viagemkm * 0.50
    print(f'A sua passagem ira ser R${primeiro_preco:.2f}')
else:
    segundo_preco = distancia_viagemkm * 0.45
    print(f'A sua passagem ira ser R${segundo_preco:.2f}')

## VERSÃO OTIMIZADA E LEGIVEL VV NÃO ESQUECA DISSO
"""
distancia = float(input('Informe a distância da viagem em KM: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da sua passagem será R${preco:.2f}')

"""