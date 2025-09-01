# sets (conjuntos)
# Sets em python são mutaveis, porem aceitam apenas tipos imutaveis como valor interno
# Sets nao aceitam valores duplicados
# criando set 
# set(iteravel) ou {1, 2, 3}
# s1 = set('Luiz') 
# s1 = set() # vazio
# s1 = set('Luiz', 1, 2, 3) # com dados

# sets são eficientes para remover valores duplicados e iteraveis 
# eles não tem indice e nao garantem ordem
# eles são iteraveis (for, in, not in)

# metodos uteis
# add, update, clear, discard

# add => adiciona um valor
# update => adiciona varios valores
# clear => limpa o set
# discard => apaga um valor

letras = set()

while True:
    letra = input('Insira uma letra: ')
    if not letra:
        break
    letras.add(letra)

    print(letras)