# CRIAR A LISTA FORA DO LOOP, PARA NÃO RENICIAR OS DADOS DA LISTA
maior_idade = []
homens_cadastrados = []
mulheres_menos_vinte_anos = []

while True:

    idade = int(input('Insira a sua idade: '))
    sexo = str(input('Insira seu sexo [M/F]: ')).strip().upper()
    print('=' * 20)
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()

    if idade > 18:
        maior_idade.append(idade)             

    if sexo in ['M', 'HOMEM', 'MACHO']:
        homens_cadastrados.append(sexo)

    if sexo in ['F', 'MULHER', 'FEMEA'] and idade < 20:
        mulheres_menos_vinte_anos.append((sexo, idade))

    if continuar in ['SIM', 'S']:
        continue
    elif continuar in ['NÃO', 'NAO', 'N']:
        print('Programa fechado')
        break
    else:
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()


print(f'Contagem de pessoas maiores de 18 anos: {len(maior_idade)}')
print(f'Contagem de homens cadastrados: {len(homens_cadastrados)}')
print(f'Contagem de mulheres com menos de 20 anos: {len(mulheres_menos_vinte_anos)}')
        