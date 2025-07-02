# listagem de preços 

lista_preco = (
    'Pão',
    1,
    'Macarrão',
    7.50,
    'Arroz',
    8.20,
    'Feijão',
    10.99,
    'Cafè',
    16.50,
    'Carne',
    32.50,
    'Leite 1 Litro',
    7.50
)
## tem dessa forma
# print('-' * 20)
# print(f"""
#         TABELA DE PREÇOS    
#         ----------------
#         Primeiro: {lista_preco[0]:.<20} {lista_preco[1]}R$
#         Segundo: {lista_preco[2]:.<20} {lista_preco[3]}R$
#         Terceiro: {lista_preco[4]:.<20} {lista_preco[5]}R$
#         Quarto: {lista_preco[6]:.<20} {lista_preco[7]}R$
#         Quinto: {lista_preco[8]:.<20} {lista_preco[9]}R$
#         Sexto: {lista_preco[10]:.<20} {lista_preco[11]}R$
#         Setimo: {lista_preco[12]:.<20} {lista_preco[13]}R$
#         ---------------
# """)
## ou desse jeito
print('Listagem de preços')
print('=+' * 20)
for pos in range(0, len(lista_preco)):
    if pos % 2 == 0:
        print(f'{lista_preco[pos]:.<30}', end='')
    else:
        print(f'R${lista_preco[pos]:>7.2f}')