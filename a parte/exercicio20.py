"""A minha sobrinha está aprendendo as letras do alfabeto. Ela ainda confunde o que é vogal e
consoante. Você topou fazer comigo um programa que verifica se uma letra é vogal ou consoante.
Então, é isso, né? Vamos lá?
"""

vogal = ['a', 'e', 'i', 'o', 'u']

letra = input('Insira a letra para saber se é vogal ou consoante: ').lower()

if letra in vogal:
    print('Isso ({}) é uma vogal'.format(letra))
else:
    print('Isso ({})a é uma consoante'.format(letra))