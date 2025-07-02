## TUPLAS
# tuplas são imutaveis

lanche = ('Hamburguer', 'Pizza', 'Suco', 'Pão')
for i in lanche:
    print(f'Eu vou comer {i}')

# # outra maneira

for i in range(0, len(lanche)):
    print(lanche[i])

# # outra maneira

for pos, comida in enumerate (lanche): # <- posição com o pos
    print(f'Vou comer {comida} na posição {pos}')

print(sorted(lanche)) # <-- vai deixar em ordem alfabetica mas não vai mudar a tupla

## juntar tuplas

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = a + b
print(c)
print(len(c)) # <-- contagem de caracteres
print(c.count(5)) # <--- quantas vezes o numero 5 vai aparecer
print(c.index(8)) # <-- mostrar a posição do 8
print(c.index(0, 5)) # <-- vai pegar da posição 0 ate a posição 5
## tupla comporta varios formatos de tipos

pessoa = ('Gustavo', 21, 'M', 70.5)
del(pessoa) # <-- vai deletar a tupla
print(pessoa)