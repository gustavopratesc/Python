## listas compostas
## listas dentro de listas

pessoas = [['Pedro', 19], ['Maria', 25], ['João', 35]]
print(pessoas[0][0]) # no indice 0 de pessoas, eu e nessse indice 0 eu quero o item 0 que é o 'Pedro'

# teste = list()
# teste.append('Gustavo')
# teste.append(21)
# galera = list()
# galera.append(teste[:]) # <-- vai criar uma copia
# teste[0] = 'Maria'
# teste[1] = 25
# galera.append(teste[:])
# print(galera)

galera = [['João', 12], ['Maria', 13], ['Joaquim', 34], ['Ana', 19]]

## fazer um print da lista com informações

for p in galera: # <-- para cada pessoa em galera vai printar ate o final da lista
    print(p)

for p in galera: # <-- para cada pessoa em galera vai printar ate o final da lista
    print(p[0]) ## <-- quer so o nome pega o indice 0

for p in galera: # <-- para cada pessoa em galera vai printar ate o final da lista
    print(p[1]) ## <-- quer a idade pega o indice 1

## formatando com f strings

for p in galera:
    print(f'{p[0]} tem {p[1]} anos!')

## outro exemplo muito bom

galera = list()
dado = list()
totalmai = totalmen = 0

for i in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # <-- vai criar uma copia
    dado.clear() # <-- vai excluir

#print(galera)

## print usando for com pessoas com idade acima de 21

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totalmen += 1

print(f'Temos {totalmai} maiores de idade e {totalmen} menores de idade')