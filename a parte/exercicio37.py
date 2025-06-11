# As temperaturas no verão estão sendo cada vez mais quentes, assim como algumas regiões estão
# tendo invernos mais rigorosos. Devido a isso, alertas de emergências devem ser divulgados com
# antecedência. Você deve fazer um programa que leia as temperaturas máximas e mínimas
# durante uma semana. Você deve apresentar a mínima e a máxima da semana.


temperaturas = []

print('Insira a temperatura maxima e minima da semana!')
for _ in range(1, 7):
    usuario_resposta = float(input('Digite a temperatura: '))
    temperaturas.append(usuario_resposta)

ordenacao = sorted(temperaturas)

array_to_string = ', '.join(str(x) for x in ordenacao)

print('A ordem de max para mim é: {}'.format(array_to_string))