def aumentar(num, porcentagem, format=False):
    """
    Vai acrescentar mais 10%
    """
    porcentagem_aumentar = (num * porcentagem) / 100
    acrescentar = porcentagem_aumentar + num

    return acrescentar if format is False else moeda(acrescentar)

def diminuir(num, porcentagem, format=False):
    """
    Vai diminuir menos 13%
    """
    porcentagem_diminuir = (num * porcentagem) / 100
    menos = num - porcentagem_diminuir

    return menos if format is False else moeda(menos)

def dobro(num, format=False):
    """
    Vai dobrar por 2
    """
    dobro = 2
    dobro *= num

    return dobro if format is False else moeda(dobro)

def metade(num, format=False):
    """
    Vai dividir pela metade
    """
    metade = 2
    num /= metade

    # Se o parâmetro 'format' for False, retorna o número original.
    # Caso contrário, retorna o número formatado como moeda.
    return num if format is False else moeda(num)

def moeda(num = 0):
    moeda = f'R${num:.1f}'
        
    return moeda


def resumo(num, aumentar, diminuir):

    print('-' * 30)
    print('     RESUMO DO VALOR     ')
    print('-' * 30)
    print(f'Preço analisado:    {moeda(num)}')
    print(f'Dobro do preço:    {moeda(dobro(num))}')
    print(f'Metade do preço:    {moeda(metade(num))}')
    porcentagem_aumentar = (num * aumentar) / 100
    acrescentar = porcentagem_aumentar + num
    print(f'{aumentar}% do preço:       {moeda(acrescentar)}')
    porcentagem_diminuir = (num * diminuir) / 100
    reduzir = num - porcentagem_diminuir
    print(f'{diminuir}% do preço:       {moeda(reduzir)}')
    print('-' * 30)


"""TEM QUE COLOCAR ESSE MODULO NA PASTA ESPECIFICA NO ARQUVIO __init__.py"""

