# texto = 'Python'

# for letra in texto:
#     print(letra)

# range(start, stop, step)

# for i in range(10):
#     if i == 2:
#         print('i é 2, pulando...')
#         continue


#     if i == 8:
#         print('i é 8 seu else não executara')
#         break


#     for j in range(1, 3):
#         print(i, j)

# else:
#     print('FOR completo com sucesso!')

# hidden_letter = 'PYTHON'
# saved_letters = []
# count = 0
# def guess_letter(letter):
#     global count
#     count += 1
#     acertou = False

#     for l in hidden_letter:
#         if letter == l:
#             print(f'Acertou! Letra {letter}')
#             saved_letters.append(letter)
#             acertou = True
#             break
        
#     if not acertou:
#         print('ERROU! *')
#     # set() para comparar sem se preocupar com ordem ou repetição.
#     if set(saved_letters) == set(hidden_letter):
#         print(f'Parabens você acertou! Tentativas: {count} | Frase: {hidden_letter}')
#         return True
    
#     return False

# while True:
#     letter = str(input('Insira apenas uma letra: ')).strip().upper()
#     if not letter:
#         print('ERRO: Nenhum valor inserido!')
#         break

#     if guess_letter(letter[0]):
#         break

""" versão professor """

import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada in palavra_secreta:
        os.system('clear')
        print('Parabens vc ganhou!')
        print(f'Tentativas {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0
        break