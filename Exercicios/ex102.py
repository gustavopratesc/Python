"""Crie um programa que tenha um função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições! """
# from datetime import datetime
# def voto(ano_nascimento):
#     ano_atual = datetime.now().year
#     idade = ano_atual - ano_nascimento

#     if idade < 16:
#         return f'Com {idade} anos: VOTO NEGADO!'
#     elif 16 <= idade < 18 or idade > 70:
#         return f'Com {idade} anos: VOTO OPCIONAL!'
#     else:
#         return f'Com {idade} anos: VOTO OBRIGATORIO!'
    
        

# ano = int(input('Insira seu ano de nascimento: '))
# resultado = voto(ano)
# print(resultado)

## ou minha solução

def voto(idade):
    from datetime import datetime # importar dentro da function economiza memoria
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    if idade > 65:
        return print('Voto OPCIONAL')
    elif idade > 18 and idade <= 65:
        return print('Voto OBRIGATORIO')
    else:
        return print('Voto NEGADO')
    
        



ano_nascimento = int(input('Insira seu ano de nascimento: '))
voto(ano_nascimento)
