def persona(name, age):
    reversed_name = name[::-1]
    name_spaces = name.count(" ")


    if name and age:
        print(f'Seu nome é {name}')
        print(f'Seu nome invertido é {reversed_name}')
        print(f'Seu nome contem espaços? {name_spaces}')
        print(f'Seu nome tem {len(name)} letras')
        print(f'A primeira letra do seu nome é {name[0]}')
        print(f'A ultima letra do seu nome é {name[-1]}')
    else:
        print('Desculpe você deixou campos vazios.')

name = input('Insira seu nome: ').strip().title()
try:
    age = int(input('Insira sua idade: '))
except ValueError:
    print('ERRO: Valor digitado não é numerico')

persona(name, age)