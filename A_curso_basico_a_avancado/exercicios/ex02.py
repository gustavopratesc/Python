# 2. Argumentos posicionais e nomeados
# Crie a função apresentar(nome, idade) que retorna:
# "Olá, meu nome é X e eu tenho Y anos".
# Teste chamando com argumentos posicionais e depois com nomeados.
# Crie a função converter_tempo(segundos, formato="minutos"):
# Se formato="minutos", converte para minutos.
# Se formato="horas", converte para horas.

def apresentar(nome, idade):
    return f'Olá, meu nome é {nome} e eu tenho {idade} anos'

name = str(input('Insira seu nome: ')).strip().title()
if not name:
    print('ERRO: Nome não inserido!')
else:
    try:
        idade = int(input('Insira sua idade: '))
        print(f'{apresentar(name, idade)}')
    except ValueError:
        print('ERRO: Valor inserido não é númerico inteiro')

def converter_tempo(segundos, formato="minutos"):
    if formato in ['minutos', 'm', 'min']:
        conversao = segundos / 60
        return f'A conversão de segundos para minutos fica: {conversao}'
    elif formato in ['horas', 'h']:
        conversao = segundos / 3600
        return f'A conversão de segundos para horas fica: {conversao}'
    else:
        print('ERRO: Escolha entre minutos ou horas')

formato = str(input('Quer qual formato? minutos ou horas: ')).strip().lower()
if not formato:
    print('ERRO: nenhum valor inserido')
else:
    try:
        tempo = float(input('Insira o tempo em segundos: '))
        print(f'{converter_tempo(tempo, formato)}')
    except ValueError:
        print('ERRO: Valor inserido não é númerico!')
