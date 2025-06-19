# 21
print('GRUPO DE MAIORIDADE')
maior_idade = []
menor_idade = []
for i in range(1, 8):
    idade = int(input('Digite a sua idade: '))
    if idade > 21:
       maior_idade.append(idade)
    else:
        menor_idade.append(idade)

print(f'O grupo de maior idade é {maior_idade} são {len(maior_idade)} pessoas')
print(f'O grupo de menor idade é {menor_idade} são {len(menor_idade)} pessoas')

# DOIS JEITOS DIFERENTES DE FAZER O CODIGO 

#print('GRUPO DE MAIORIDADE')
#contador_maior = 0
#contador_menor = 0
#for i in range(1, 8):
#    idade = int(input('Digite a sua idade: '))
#    if idade >= 21:
#        contador_maior += 1
#    else:
#        contador_menor += 1

#print(f'O grupo de maior idade é {contador_maior} pessoas')
#print(f'O grupo de menor idade é {contador_menor} pessoas')