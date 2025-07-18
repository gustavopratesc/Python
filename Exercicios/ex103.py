"""CRIE UM PROGRAMA QUE TENHA UMA FUNCTION FATORIAL() QUE RECEBA DOIS PARAMETROS: O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E O OUTRO CHAMADO SHOW, QUE SERA UM VALOR LOGICO (OPCIONAL) INDICANDO-SE SERA MOSTRADO OU NÃO NA TELA O PROCESSO DE CALCULO DO FATORIAL"""

def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o numero vai ser calculado
    :param show: (opcional) mostrar ou não a conta.
    :return: vai retornar os valores o valor fatorial de um número n
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f

# n = int(input('Digite um número para saber seu fatorial: '))
# escolha = bool(input('True / False: '))
print(fatorial(10, True))
# help(fatorial)