print('Calculadora de IMC')

altura = float(input('Insira a sua altura: '))
peso = float(input('Insira o seu peso: '))

imc = peso / (altura * altura)

print(f'Seu IMC é {imc:.2f}')

if imc > 40:
    print('Obesidade Morbida')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 18.5 and imc <= 25:
    print('Peso ideal')
else:
    print('Abaixo do peso')
