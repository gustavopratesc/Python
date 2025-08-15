# constantes com python n existem mas para afirmar uma variavel constante coloque letras maiusculas

# PI = 3.14 # <- constante 
def odd_pair(number):
    if number % 2 == 0:
        print(f'Esse {number} é par!')
    else:
        print(f'Esse {number} é impar!')
    # ou type = 'par' if number % 2 == 0 else 'impar' <-- alternativa para menos codigo
# alternativa em vez de usar TRY EXCEPT
# if number.isdigit():
    # faça alguma coisa
# else:
#   você não digitou um número

try:
    number = int(input('Insira um número inteiro: '))
    odd_pair(number)
except ValueError:
    print('ERRO: O valor inserido não é númerico!')


def current_hour(hour):
    good_morning = hour >= 0 and hour <= 11
    good_afternoon = hour >= 12 and hour < 17
    good_night = hour >= 18 and hour <= 23
    if good_morning:
        print('Bom dia')
    elif good_afternoon:
        print('Boa tarde')
    elif good_night:
        print('Boa noite')
    else:
        print('QUE HORARIO É ESSE?')

try:
    hour = int(input('Insira a hora atual: '))
except ValueError:
    print('ERRO: Valor inserido não é númerico!')

current_hour(hour)

def short_name(name):
    size_name = len(name)
    if size_name <= 4:
        print('Seu nome é curto!')
    elif size_name >= 5 and size_name <= 6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!')


name = str(input('Insira seu nome: ')).strip().title()
if not name:
    print('ERRO: Nenhum valor inserido!')
    exit()

short_name(name)