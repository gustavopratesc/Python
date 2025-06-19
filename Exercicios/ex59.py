primeiro_termo = int(input('Insira um número: '))
razao = int(input('Insira o número da razão: '))

contador = 0
entesimo_termo = 0

while contador <= 10:
    contador += 1
    entesimo_termo = primeiro_termo + (contador - 1) * razao
    print(entesimo_termo)