print(f'Calculadora de IMC')
peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    frase = 'abaixo do peso'
elif 18.5 <= imc <= 24.9:
    frase = 'peso ideal'
elif 25 <= imc <= 29:
    frase = 'sobrepeso'
else:
    frase = 'obesidade'


print(f'Seu imc deu {imc:.2f} e vc esta com {frase}')
