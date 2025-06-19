print('Analisador completo')

soma_idade = 0
contador_mulher = 0
nome_homem_velho = ''
maior_idade_homem = 0

for i in range(1, 6):
    nome = str(input('Insira o seu nome: ')).title().strip()
    idade = int(input('Insira a sua idade: '))
    sexo = str(input('Insira o seu sexo F / M: ')).lower()
    print('=+' * 20)
    soma_idade += idade
    if idade < 21 and sexo == 'f':
        contador_mulher += 1

    if sexo == 'm':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_velho = nome
          

media_idade = soma_idade / 5

print(f'A media de idade do grupo é: {media_idade}')
print(f'A quantidade de mulheres com menos de 21 anos é: {contador_mulher}')
print(f'O nome do homem mais velho é {nome_homem_velho} e sua idade é: {maior_idade_homem}')
