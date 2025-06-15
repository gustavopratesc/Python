"""VERIFICAR SE O ANO É BIXSEXTO"""

from datetime import date
ano = int(input('Insira o ano para saber se é bixsexto ou não: '))

ano_bixsexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
if ano == 0:
    ano = date.today().year
if ano_bixsexto:
    print(f'Sim o ano {ano} é bixsexto!')
else:
    print(f'Não! o ano {ano} não é bixsexto!')


"""EXPLICAÇÃO CALCULOO DO ANO BIXSEXTO PARA NÃO ESQUECER 
    (ANO TEM QUE DIVIDIR POR 4 E RESTAR 0 AND ANO TEM QUE DIVIDIR POR 100 E SER DIFERENTE DE 0) OR
    (ANO TEM QUE DIVIDIR POR 400 E RESTAR 0)
"""

