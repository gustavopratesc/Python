"""Faça um programa que leia o sexo de uma 
pessoa mas so aceite os valores 'M' e 'F'. Caso
esteja errado, peça a digitação novamente até ter um
valor correto"""

sexo = str(input('Digite seu sexo [M/F]')).upper().strip()[0]

while sexo not in 'MF': # <- enquanto sexo for diferente de M F ele vai ficar repetindo o loop
    sexo = str(input('Dados invalidos informe novamente seu sexo: [M/F]: ')).upper().strip()[0]

print(f'Sexo {sexo} registrado com sucesso!')