salario = float(input("Me informe seu salario e vc ira receber 15% de aumento: "))
aumento = salario * 0.15
novoSalario = salario + aumento

print('Seu salario antigo era {:.2f}R$ agora seu novo salario é {:.2f}R$'.format(salario, novoSalario))