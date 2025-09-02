# def lambda 
# função de uma linha

lista = [
    {'nome': 'Gustavo', 'sobrenome': 'Prates Caetano'},
    {'nome': 'Maria', 'sobrenome': 'Soares'},
    {'nome': 'João', 'sobrenome': 'Silva'},
    {'nome': 'Ana', 'sobrenome': 'Santos'},
    {'nome': 'Joaquim', 'sobrenome': 'Oliveira'},
]


    

lista.sort(key=lambda item: item['nome']) # <- essa linha de codigo faz com que a lista seja ordenada pelo nome em ordem alfabetica com lambda e key sem precisar de um def
for item in lista:
    print(item)

def executa(funcao, *args):
    return funcao(*args)

def soma(a, b):
    return a + b

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(
        lambda x, y: x + y,
        10, 20
    )
)