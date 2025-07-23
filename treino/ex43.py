idade = int(input('Insira a sua idade: '))

if idade < 18:
    print(f'Menor de idade')
elif 18 <= idade <= 64:
    print(f'Adulto')
else:
    print(f'Idoso')