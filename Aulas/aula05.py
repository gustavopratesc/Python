## IF E ELSE ELIF == se, senao, se senao

#nome = str(input('Digite seu nome: ')).title()
#if nome == 'Gustavo':
#    print('Que nome lindo você tem!')
#else:
#    print('Seu nome é tão normal!')
#print(f'Bom dia, {nome}')

## ---------
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

m = (n1 + n2) / 2
print(f'A sua media foi {m:.2f}')

if m >= 6.0:
    print('Sua media foi boa parabens')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')