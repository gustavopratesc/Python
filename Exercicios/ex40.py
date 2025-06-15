print('FORMANDO UM TRIANGULO')
print('+=' * 20)

primeiro_lado = int(input('Insira a medida do primeiro lado: '))
segundo_lado = int(input('Insira a medida do segundo lado: '))
terceiro_lado = int(input('Insira a medida do terceiro lado: '))
print('+=' * 20)

triangulo = primeiro_lado + segundo_lado > terceiro_lado and primeiro_lado + terceiro_lado > segundo_lado and segundo_lado + terceiro_lado > primeiro_lado

if triangulo:
    print('Sim pode formar um triangulo!!')
    if primeiro_lado == segundo_lado == terceiro_lado:
        print('O triangulo é um equilatero!')
    elif primeiro_lado == segundo_lado or segundo_lado == terceiro_lado or primeiro_lado == terceiro_lado:
        print('O triangulo é isoceles!!')
    else:
        print('O triangulo é escaleno!!!')
else:
    print('Não podemos formar um triangulo')