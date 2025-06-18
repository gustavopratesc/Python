## FOR LAÇO DE REPETIÇÃO

for i in range(1, 10):
    print(f'OI') # <- vai contar de 1 a 9, se for (1, 11) <- vai contar de 1 a 10
print('fim')

# e se for uma contagem regressiva

for j in range(11, 0, -1): # <- o menos 1 vai diminuir
    print(j)

# e se for uma contagem de 2 em 2

for i in range(0, 11, 2): # <- vai contar de 2 em 2 
    print(i)

# e se for uma pessoa inserindo um número

n = int(input('Insira um número: ')) # <- vai fazer a contagem da pessoa 

for c in range(0, n+1):
    print(c)

# outro exemplo <-- voce escolhe o inicio, o passo tipo pular de 2 em 2, e o fim escolhe o numero que vai ser o fim

i = int(input('Inicio: '))
p = int(input('Passo: '))
f = int(input('Fim: '))

for c in range(i, f+1, p):
    print(c)

print('FIM')

# outro exemplo

s = 0
for i in range(0, 10):
    n = int(input('Digite um número para soma: '))
    s += n
print(f'O somatorio é igual a: {s}')