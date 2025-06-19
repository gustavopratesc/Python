primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo + razao, razao):
    print(i)