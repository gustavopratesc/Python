## continue

# Quando o Python encontra um continue, ele interrompe o que estiver fazendo naquele momento no loop e volta para o início da próxima iteração.

for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

# Quando usar continue?
# Quando você quer ignorar certos casos dentro do loop.

# Quando precisa pular valores inválidos ou que não interessam.

# Quando precisa manter o loop rodando, mas não quer que ele execute tudo sempre.

nomes = ['Ana', '', 'Carlos', '', 'Lucas']

for nome in nomes:
    if nome == '':
        continue  # Pula nomes vazios
    print(f'Nome válido: {nome}')
