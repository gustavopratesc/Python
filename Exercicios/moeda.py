def aumentar(num):
    """
    Vai acrescentar mais 10 
    """
    acrescentar = 10
    acrescentar += num
    return acrescentar

def diminuir(num):
    """
    Vai diminuir menos 10
    """
    menos = 10
    menos -= num
    return menos

def dobro(num):
    """
    Vai dobrar por 2
    """
    dobro = 2
    dobro *= num
    return dobro

def metade(num):
    """
    Vai dividir pela metade
    """
    metade = 2
    metade /= num
    return metade

def moeda(num):
    moeda = f'R${num:.2f}'
        
    return moeda



