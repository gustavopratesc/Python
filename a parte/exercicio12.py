"""Você viu na televisão que esse inverno vai ser rigoroso no Brasil. Decidiu então que vai monitorar a
temperatura da sua cidade. Se as temperaturas estiverem abaixo de 17ºC, você vai exibir na tela:
“Frio da moléstia", mas caso contrário: “Tudo normal nas terras de Cuçumarim”.
"""

temperatura = float(input('Insira a temperatura da sua cidade: °C'))

if temperatura < 17:
    print('Frio da moléstia')
elif temperatura >= 17 and temperatura <= 31:
    print('Tudo normal nas terras de Cuçumarim')
else:
    print('Ta pegando fogo bixo!!')