"""MODULARIZAÇÃO E PACOTES"""
"""ESSE CODIGO VAI FICAR NO UTEIS.PY"""
# def fatorial(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i
#     return f

# def dobro(n):
#     return n * 2

# def triplo(n):
#     return n * 3


# import uteis ## <-- importar funções criadas de outros arquivos py 
from uteis import numeros
# PROGRAMA PRINCIPAL
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O Dobro de {fat} é {numeros.dobro(fat)}')


## PACOTES

"""PACOTES SÃO PASTAS COM VARIOS MODULOS DE FUNÇÕES SEPARADOS ORGANIZADOS
    __init__.py <-- tem que ter esse formato
"""