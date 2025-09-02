def maior_valor(*nums):
    if not nums:
        return None
    return max(nums)

lista_numeros = []

while True:
    print('Digite um número ou 0 para finalizar!')
    try:
        numero = int(input('Numero: '))
        if numero != 0:
            lista_numeros.append(numero)
        else:
            maior = maior_valor(*lista_numeros)
            if maior is None:
                print('Nenhum número foi digitado')
            else:
                print(f'Maior númerod a lista foi {maior}')
            break
    except ValueError:
        print('ERRO: Digite um valor númerico')
        continue