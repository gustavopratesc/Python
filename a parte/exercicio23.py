"""As cores no computador podem ser representadas por número inteiros entre 0 e 255, ou seja, 256
valores distintos, onde 0 (zero) representa preto e 255 representa branco. Nessa escala de cinza,
os valores abaixo de 128 são os mais escuros, acima desse valor os mais claros. Faça um programa
que leia o nível de cinza, verifique se o valor está entre 0 e 255 e depois diga se é tom escuro ou
claro.
"""

escala_cor = int(input("Insira a escala de cor para ver se é escuro ou claro entre 0 e 255: "))

if escala_cor == 0:
    print('Totalmente preto!!')
elif escala_cor < 128:
    print('Escala de cinza quanto menor mais escuro!!')
elif escala_cor < 254:
    print('Escala de branco quanto maior mais claro!!')
elif escala_cor == 255:
    print('Totalmente branco!!')
else:
    print('Escreva um número entre 0 a 255')