# def descricao_produto(**info):
#     print(f'O produto {info["nome"]} custa R${info["preco"]} e possui {info["estoque"]} em estoque')

# produtos = {
#     "nome": str(input('Insira o nome do produto: ')).strip().title(),
#     "preco": float(input('Insira o preço do produto: ')),
#     "estoque": int(input('Insira o estoque do produto: '))
# }

# descricao_produto(**produtos)

## ou dessa maneira mais completa

def descricao_produto(**info):
    print(f'O produto {info["nome"]} custa R${info["preco"]} e possui {info["estoque"]} em estoque')

produtos = []
try:
    qtd = int(input('Quantos produtos deseja cadastrar?: '))
except ValueError:
    print('ERRO: Digite um número inteiro valido!')

for i in range(qtd):
    print(f'Produto {i + 1}:')
    produto = {
        "nome": str(input('Insira o nome: ')).strip().title(),
        "preco": float(input('Insira o preço: ')),
        "estoque": int(input('Insira a quantidade em estoque: '))
    }
    produtos.append(produto)

print(f'\n--- Lista de produtos cadastrados ---')
for p in produtos:
    descricao_produto(**p)