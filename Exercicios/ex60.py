primeiro_termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

contador = 1
total_termos = 10

while True:
    while contador <= total_termos:
        termo = primeiro_termo + (contador - 1) * razao
        print(f'{contador}º termo: {termo}')
        contador += 1

    continuar = int(input('Quer continuar? 1 para sim, 0 para não: '))
    if continuar == 1:
        mais_termos = int(input('Quantos termos quer ver a mais? '))
        total_termos += mais_termos
    else:
        print('Programa finalizado.')
        break

    
