
print('Categoria de idade Esportes!!')


idade = int(input('Insira sua idade: '))

if idade <= 0 or idade > 140:
    print('Insira uma idade corretamente!!')
elif idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade == 20:
    print ('Categoria: SENIOR')
else:
    print('Categoria: MASTER')