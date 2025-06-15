from datetime import datetime

nome = str(input('Digite o seu nome: ')).title()
idade = int(input('Digite sua idade: '))
ja_alistou = str(input('Digite se SIM ou NÃO / Se você ja alistou: ')).lower().strip()

print('=+' * 20)

ano_atual = datetime.now().year

data_nascimento = ano_atual - idade
faltam = 18 - idade
acumulou = idade - 18

if data_nascimento > 2007 and ja_alistou in ('não' 'nao'): 
    print(nome)
    print(f'Você ainda não completou 18 anos, falta {faltam} anos, então não vai se alistar ainda!!')
elif data_nascimento > 2007 and ja_alistou in 'sim':
    print(nome)
    print(f'Você nem tem 18 anos, falta {faltam} anos, nem adianta mentir você não se alistou!')
elif data_nascimento == 2007 and ja_alistou in 'sim':
    print(nome)
    print(f'Muito bem você ja se alistou!!')
elif data_nascimento == 2007 and ja_alistou in ('não', 'nao'):
    print(nome)
    print(f'Você precisa se alistar para não dar problemas')
elif data_nascimento < 2007 and ja_alistou in 'sim':
    print(nome)
    print(f'Parabens você é maior de 18 anos e não é enrrolado')
elif data_nascimento < 2007 and ja_alistou in ('não', 'nao'):
    print(nome)
    print(f'Você e maior de 18 e é irresponsavel pois não se alistou, acumulo {acumulou} anos')
else:
    print(f'Insira os dados corretamente! ')


