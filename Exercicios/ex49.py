primeiro_termo = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(1, 11):
    termo = primeiro_termo + razao * i
    print(termo)