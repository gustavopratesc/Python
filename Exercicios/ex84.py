## peso leve 70, peso pesado = 100
#galera = []
dado = []
while True:
    nome = str(input('Seu Nome: ')).strip().title()
    peso = float(input('Seu Peso: '))
    dado.append([nome, peso])
    #galera.append(dado[:])

    while True:
        c = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if c in ['SIM', 'S']:
            break
        elif c in ['NÃO', 'NAO', 'N']:
            print('Resultados...')
            print(f'Quantidade de pessoas cadastradas {len(dado)}')
            for p in dado:
                if p[1] >= 100: ## no for tem q usar o P em vez de DADO <-- OBS!!!!
                    print(f'Pessoa pesada {p[0]}, peso {p[1]}KG')
                elif p[1] < 100:
                    print(f'Pessoa leve {p[0]}, peso {p[1]}KG')
            exit()
        else:
            print('Escolha entre [S/N]!!')