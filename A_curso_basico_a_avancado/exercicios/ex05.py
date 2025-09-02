def soma_tudo(*nums):
    soma = sum(*nums)
    return f'A soma de todos os números é {soma}'

lista_numeros = []

while True:
    print('Adicione um número ou 0 para parar e somar')
    try:
        numero = int(input('Insira o número: '))
        if numero != 0:
            lista_numeros.append(numero)
        else:
            print(soma_tudo(lista_numeros))
            break
    except ValueError:
        print('ERRO: Valor inserido não é númerico')
        continue