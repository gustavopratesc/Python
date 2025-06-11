"""The Asa’s Club é um clube da cidade e você está trabalhando na portaria dela. As regras para
comprar ingressos para o clube são claramente machistas, mas elas são aplicadas. As mulheres
que chegarem até as 22h não pagam a entrada, mas depois desse horário, elas pagam metade do
valor do ingresso. Os homens que chegarem até as 22h pagam 70% do ingresso, enquanto depois
desse horário pagam o valor integral. Você que não perdeu tempo, fez um programa para a
portaria. Eu fico me perguntando porque tu se mete nessas coisas sem ganhar um centavo, mas
tudo bem.
"""

sexo = input('Insira o seu sexo: masculino / feminino ')
horario = float(input('Insira o horario de chegada antes das 22hr ou depois das 22hr?: '))

if sexo.lower() == 'feminino' and horario <= 22:
    print('Você é mulher e chegou antes das 22hr vc não paga entrada!!')
elif sexo.lower() == 'feminino' and horario > 22:
    print('Você é mulher mas chegou depois das 22hr vc vai pagar metade do ingresso!!')
elif sexo.lower() == 'masculino' and horario <= 22:
    print('Você é homem e chegou antes das 22hr vc vai pagar 70% do ingresso!!')
else:
    print('Você é homem e chegou depois das 22hr vai pagar ingresso no valor integral!!')
    