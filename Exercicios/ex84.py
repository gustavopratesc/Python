## peso leve 70, peso pesado = 100
#galera = []
# dado = []
# while True:
#     nome = str(input('Seu Nome: ')).strip().title()
#     peso = float(input('Seu Peso: '))
#     dado.append([nome, peso])
#     #galera.append(dado[:])

#     while True:
#         c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
#         if c in ['SIM', 'S']:
#             break
#         elif c in ['NÃO', 'NAO', 'N']:
#             print('Resultados...')
#             print(f'Quantidade de pessoas cadastradas {len(dado)}')
#             for p in dado:
#                 if p[1] >= 80: ## no for tem q usar o P em vez de DADO <-- OBS!!!!
#                     print(f'Pessoa pesada {p[0]}, peso {p[1]}KG')
#                 elif p[1] < 100:
#                     print(f'Pessoa leve {p[0]}, peso {p[1]}KG')
#             exit()
#         else:
#             print('Escolha entre [S/N]!!')

## ou de outra forma

temp = []
princ = []
maior = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = men = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) # <-- fazer uma copia
    temp.clear() # <-- vai limpar
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break

print('-' * 30)
print(f'Você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {maior}', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi {men}', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end='')
print()
