"""Você sabia que um ano tem 365 dias, 5 horas, 48 minutos e 48 segundos, aproximadamente? O
calendário que temos hoje passou por várias transformações ao longo da história, saindo de
calendários lunares para solares, tentando manter sempre a precisão quanto ao equinócio de
primavera (quando começa a primavera). Se não considerássemos esse tempo excedente no ano,
considerando apenas os 365 dias, em 372 anos, nós estaríamos adiantados 3 mês em relação ao
2
sol, ou seja, estaríamos em junho, mas o sol estaria ainda em março. Por isso, de 4 em 4 anos, o
mês de fevereiro tem 29 dias e o ano é chamado de bissexto. Então, a regra para um ano ser
bissexto é:
1. ele precisa ser divisível por 4
2. e se divisível por 100 precisa ser divisível por 400 ao mesmo tempo.
Exemplos:
1600, 2000, 2020, 2024 (anos bissextos),
1900, 1800, 1700 (não são bissextos, apesar de serem divisíveis por 4, eles também se
dividem por 100, mas não por 400).
Faça um programa que diga se um ano é bissexto ou não.
"""

anoBix = int(input('Digite uma ano que você ache que é bixsexto: '))

if anoBix % 4 == 0:
    if anoBix % 100 != 0 or anoBix % 400 == 0:
        print('O ano {} é bixsexto'.format(anoBix))
    else:
        print('Não é bixsexto')
else:
    print('Não é bixsexto')

"""Parabéns! Esse é o seu primeiro dia no estágio na rede de hotéis: DOM. O seu supervisor de
estágio passou uma demanda que eles estão tendo em produção. As datas não estão sendo
validadas corretamente pela função da API, então, ele resolveu pedir a você que desenvolvesse
um programa que validasse a data. Você deve ler o dia, o mês e o ano e ao fim imprimir se a data é
válida ou não. Não esqueça de verificar se o ano é bissexto ou não (se for bissexto, o mês de
fevereiro terá 29 dias).
"""

ano = int(input('Digite o ano: '))
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês em números: '))

trinta_e_um_dias = [1, 3, 5, 7, 8, 10, 12]
trinta_dias = [4, 6, 9, 11]
fevereiro = 2

if 1 <= mes <= 12:
        if mes in trinta_e_um_dias and 1 <= dia <= 31:
            print('Data válida: {}/{}/{}'.format(dia, mes, ano))
        elif mes in trinta_dias and 1 <= dia <= 30:
            print('Data válida: {}/{}/{}'.format(dia, mes, ano))
        elif mes == fevereiro:
            if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
                if 1 <= dia <= 29:
                    print('Data válida: {}/{}/{}'.format(dia, mes, ano))
                else:
                    print('Data inválida: Fevereiro bissexto vai até 29 dias.')
            else:
                if 1 <= dia <= 28:
                    print('Data válida: {}/{}/{}'.format(dia, mes, ano))
                else:
                    print('Data inválida: Fevereiro comum vai até 28 dias.')
        else:
            print('Dia inválido.')
else:
        print('Mês inválido.')
            
                



