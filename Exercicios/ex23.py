"""FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO
    E MOSTRE:
    QUANTAS VEZES APARECE A LETRA 'A'

    EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ

    EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ
"""

frase = str(input('Digite alguma frase: ')).strip().upper()

print(f'Frase ({frase}) Quantidade de vezes apareceu a letra A {frase.count('A')}')
print(f'Posição em que ela aparece primeira vez {frase.find('A')}')
print(f'Posição em que ela aparece ultima vez {frase.rfind('A')}')
