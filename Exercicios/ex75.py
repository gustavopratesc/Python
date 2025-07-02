## contagem de vogais nas palavras

palavras = (
   'Python',
   'Javascript',
   'Java',
   'Ruby',
   'html',
   'css',
   'programaçao',
   'estudos',
   'desenvolvedor'
)

# vogais = 'aeiouAEIOU'
# print('Analisando vogais')
# for palavra in palavras:
#     vogais_encontradas = [letra for letra in palavra if letra in vogais]
#     quantidade_vogais = len(vogais_encontradas)
#     print(f'A palavra {palavra:<15} tem {quantidade_vogais} vogal(is): {",".join(vogais_encontradas)}')

## ou

for p in palavras:
    print(f'\nPara cada palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')