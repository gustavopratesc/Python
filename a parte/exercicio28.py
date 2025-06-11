"""Calcular a área de uma casa, ou um apartamento, pode ser uma tarefa complicada,
principalmente, quando a área construída não é parecida com um quadrado ou retângulo. Por isso,
um modo mais fácil é somar as áreas de cada cômodo da casa e então ter a área total. Faça um
programa que pede a área por cômodo, até que a área informada seja igual a zero. Quando a área
for nula, você deve informar a área total da casa, ou apartamento.
"""

soma_area = 0

while True:
    area = float(input('Insira o valor da area: / 0 para finalizar e somar: '))
    if area == 0:
        break
    soma_area += area

print('O total ficou {}'.format(soma_area))
