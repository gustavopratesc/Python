## ESSE CODIGO VOU TER QUE DESTRINCHAR PARA ENTENDER

print("""
    ----- CAIXA ELETRÔNICO -----
""")

dinheiro = int(input('Insira quanto de dinheiro quer sacar R$ '))

total = dinheiro
cedula = 50
total_cedulas = 0

while total > 0:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} cédula(s) de R${cedula}')
        # Troca para próxima cédula menor
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0  # Reinicia a contagem da nova cédula

print('Fim do saque!')

## ou usando divmod melhor forma

print("""
    ----- CAIXA ELETRÔNICO -----
""")

valor = int(input('Insira quanto de dinheiro quer sacar R$ '))

cedulas = [50, 20, 10, 1]

for cedula in cedulas:
    qtd, valor = divmod(valor, cedula)
    if qtd > 0:
        print(f'{qtd} cédula(s) de R${cedula}')

print('Fim do saque!')
