nota = float(input('Insira uma nota: '))
if 7 <= nota <= 10:
    print(f'Aprovado!')
elif 5 <= nota < 7:
    print(f'Recuperação!')
elif nota < 5:
    print(f'Reprovado!')
else:
    print('Nota entre 0 a 10!')