# Exercício 01: Faça um programa que mostre a mensagem "Alo mundo" na tela
# Exercício 02: Faça um programa que peça um número e então mostre a mensagem "O número informado foi [número]"
# Exercício 03: Faça um programa que peça dois números e imprima a soma
# Exercício 04: Faça um programa que peça as 4 notas bimestrais e mostre a média
# Exercício 05: Faça um programa que converta metros para centímetros
# Exercício 06: Faça um programa que peça o raio de um círculo, calcule e mostre sua área
# Exercício 07: Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
# Exercício 08: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
# Exercício 09: Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
# Exercício 10: Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
# Exercício 11: Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre o produto do dobro do primeiro com metade do segundo, a soma do triplo do primeiro com o terceiro e o terceiro elevado ao cubo
# Exercício 12: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes
# Exercício 13: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes
# Exercício 14: João, um pescador, … leia o peso de peixes e calcule excesso e multa
# Exercício 15: Faça um programa que pergunte quanto você ganha por hora e … calcule salário líquido com descontos de IR, INSS, sindicato
# Exercício 16: Faça um programa para uma loja de tintas. Peça a área a ser pintada e informe quantidade de latas e preço total
# Exercício 17: Faça um programa para uma loja de tintas. Mesma ideia do exercício 16, mas comparando latas e galões e avaliando menor desperdício com folga de 10%
# Exercício 18: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download em minutos

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_download = float(input('Insira o tamalho do download em MB: '))
velocidade_internet = float(input('Informe a velocidade da internet em Mbps: '))


tempo = tamanho_download / velocidade_internet
minutos = tempo / 60

print(f'O tempo de download sera de {minutos:.2f} minutos')

