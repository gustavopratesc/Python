extenso = (
    'Zero',
    'Um',
    'Dois',
    'Tres',
    'Quatro',
    'Cinco',
    'Seis',
    'Sete',
    'Oito',
    'Nove',
    'Dez',
    'Onze',
    'Doze',
    'Treze',
    'Quatorze',
    'Quinze',
    'Dezsseis',
    'Dezssete',
    'Dezoito',
    'Dezsenove',
    'Vinte'
)

while True:
    numero = int(input('Insira um número de 0 a 20 para ver seu formato em extenso: '))
    if 0 <= numero <= 20:
        break
    print('Tente novamente: ', end='')

print(f'Esse é o formato em extenso: {extenso[numero]}')
