'''Para abrir o chat é necessário clicar no botão "Chat" na parte inferior direita da tela.
Ou apertar CTRL + I para abrir o chat inbutido no código.
'''

import matplotlib.pyplot as plt

alturas = [150, 160, 165, 170, 175, 180, 185]

pesos = [50, 60, 65, 70, 75, 80, 80]

plt.bar(alturas, pesos)
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação entre Altura e Peso')
plt.show()