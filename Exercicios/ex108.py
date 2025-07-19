"""CRIE UM MODULO CHAMADO moeda.py QUE TENHA FUNÇÕES INCORPORADAS AUMENTAR(), DIMINUIR(), DOBRO(), METADE()
FAÇA TAMBEM UM PROGRAMA QUE IMPORTE ESSE MODULO E USE ALGUMAS DESSAS FUNÇÕES
"""
import moeda
n = int(input('Insira um número para ver alguns resultados (TRUE/FALSE) para ver formato moeda: '))
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(n, 13, True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}')
print(f'Formato de moeda: {moeda.moeda(n)}')

## FALTA MAIS COISA