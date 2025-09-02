# **kwargs

def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

#  essa é a forma errada de usar como input
nome = str(input('Nome: '))
idade = int(input('Idade: '))
cidade = str(input('Cidade: '))
produto = str(input('Produto: '))
preco = float(input('Preço: '))
autor = str(input('Autor: '))


# exibir_dados(nome, idade, cidade, produto, preco, autor) <-- FORMA ERRADA
# exibir_dados(nome= "Ana", idade= 25, cidade= "Lisboa")
# exibir_dados(produto= "Livro", preco= 19.99, autor="Desconhecido")

#  temos duas formas
# ja passa com os argumentos nomeados
exibir_dados(
    nome=nome,
    idade=idade,
    cidade=cidade,
    produto=produto,
    preco=preco,
    autor=autor
)

# ou ja cria um dicionario e desempacota ele chamando na função

dados = {
    "nome": input('Nome: '),
    "idade": int(input('Idade: ')),
    "cidade": input('Cidade: '),
    "produto": input('Produto: '),
    "preco": float(input('Preço: ')),
    "autor": input('Autor: ')
}

exibir_dados(**dados)

## versão dinamica para usuario digitar seus proprios dados

def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')


dados = {}

print("Digite as informações (aperte Enter em 'chave' para finalizar).")

while True:
    chave = input("Nome da informação (ex: nome, idade, cidade): ").strip()
    if not chave:  # se só apertar Enter, finaliza
        break
    valor = input(f"Valor para '{chave}': ").strip()
    dados[chave] = valor

exibir_dados(**dados)

## versão dinamica com detecção automatica do tipo

def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor} ({type(valor).__name__})')


def converter_valor(valor: str):
    """Tenta converter o valor para int ou float; se não der, retorna string."""
    if valor.isdigit():  # só dígitos → int
        return int(valor)
    try:
        return float(valor)  # tenta converter para float
    except ValueError:
        return valor  # mantém como string


dados = {}

print("Digite as informações (aperte Enter em 'chave' para finalizar).")

while True:
    chave = input("Nome da informação (ex: nome, idade, cidade): ").strip()
    if not chave:  # Enter → encerra
        break
    valor = input(f"Valor para '{chave}': ").strip()
    dados[chave] = converter_valor(valor)

exibir_dados(**dados)
