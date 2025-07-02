## listas

lista = [] # <-- com colchetes
lista.append('cookie') # <-- o append coloca no final da lista
lista.insert(0, 'cachorro quente') # <-- vai inserir na posição 0 inicial da lista
#del(lista[3]) # <-- vai deletar o 3
#lista.pop(3) # <-- tambem vai deletar ao 3
lista.pop() # <-- vai remover o ultimo
#lista.remove('') # <-- tambem mas aqui vc n indica o indice, indica o valor que quer remover
#print(lista)
valores = list(range(4, 11)) # <-- vai criar uma lista com elementos e indices, 0 a 6
valores = [8, 2, 3, 5, 9, 3, 0]
valores.sort() # <-- vai ordenar todos valores
valores.sort(reverse=True) # <-- vai ordenar na ordem reversa
len(valores) # <-- quantos elementos

##
## praticando listas

num = [2, 3, 5, 9]
num[2] = 3
num.append(7)
num.sort()
#num.sort(reverse=True)
num.insert(2, 0) # <-- na posição 2 inserir o valor 0
num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número na posição 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')

## com for

teste_valores = []

teste_valores.append(5)
teste_valores.append(4)
teste_valores.append(9)

for i in teste_valores:
    print(f'{i}...')

## ou se vc quiser o valor e o indice, utilize o enumerate

for cont in range(0, 5):
    teste_valores.append(int(input('Digite um valor: ')))

## tambem dessa forma
for c, i in enumerate(teste_valores):
    print(f'Na posição {c} encontrei o valor {i}')

## observação importante no python

a = [1, 3, 4, 6]
b = a # <-- aqui ele faz a ligação da lista
b = a[:] # <-- aqui ele faz uma copia da lista ai pode modificar tranquilo
b[2] = 8 #  <-- ele modifica as duas listas apos igualarem as listas, o python faz uma ligação da lista com a outra
print(f'Lista A {a}')
print(f'Lista B {b}')