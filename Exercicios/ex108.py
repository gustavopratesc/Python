"""CRIE UM MODULO CHAMADO moeda.py QUE TENHA FUNÇÕES INCORPORADAS AUMENTAR(), DIMINUIR(), DOBRO(), METADE()
FAÇA TAMBEM UM PROGRAMA QUE IMPORTE ESSE MODULO E USE ALGUMAS DESSAS FUNÇÕES
"""
import moeda
n = int(input('Insira um número para ver alguns resultados: '))
print(f'O número escolhido + 10 = {moeda.aumentar(n)}')
print(f'O número escolhido - 10 = {moeda.diminuir(n)}')
print(f'O número escolhido * 2 = {moeda.dobro(n)}')
print(f'O número escolhido / 2 = {moeda.metade(n)}')
print(f'Formato de moeda: {moeda.moeda(n)}')

## FALTA MAIS COISA