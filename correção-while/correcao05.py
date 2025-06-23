"""Progressão aritmetica
    leia primeiro termo, e a razão de uma PA
    mostrando os 10 primeiros termos da progressão
    usando o while
"""
print('Gerador de PA')
print('+=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador_termo = 1

while contador_termo <= 10:
    print(f'{termo} ->', end=' ') # <- end= ' '  deixar em horizontal
    termo += razao
    contador_termo += 1
print('FIM')

# -----------------------

print('Super Gerador de PA')
print('+=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador_termo = 1
total = 0
mais = 10
# WHILE DENTRO DE WHILE <----
while mais != 0:
    total += mais
    while contador_termo <= total:
        print(f'{termo} ->', end=' ') # <- end= ' '  deixar em horizontal
        termo += razao
        contador_termo += 1

    print('Pausa')

    mais = int(input('Quantos termos você quer mostrar mais?: '))
print(f'Total de termos {total}')