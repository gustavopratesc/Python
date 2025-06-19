print('COMPARAÇÃO DE PESOS')
medidas_pesos = []
for i in range(1, 6):
    peso = float(input('Insira seu peso: KG'))
    medidas_pesos.append(peso)

medidas_pesos.sort(reverse=True)
medida_max = max(medidas_pesos)
medida_min = min(medidas_pesos)
print(f'As medidas do maior para menor são: {medidas_pesos}')
print(f'A medida de peso max é: {medida_max}KG')
print(f'A medida de peso min é: {medida_min}KG')
## ou


