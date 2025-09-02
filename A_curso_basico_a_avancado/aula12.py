# FUNCTIONS!!
# 105 & 110. Definindo funções + return + docstrings
def soma(a, b):
    """ Function que faz a soma de 2 valores """ # <- docstrings
    s = a + b
    return s


n1 = int(input('Insira um n: '))
n2 = int(input('Insira outro n: '))
print(f'Soma: {soma(n1, n2)}')

# 106. Argumentos posicionais e nomeados

def saudar(nome, saudacao = 'Olá'):
    return  f'{saudacao} {nome}'

nome = str(input('Insira seu nome: ')).strip().title()
saudacao = str(input('Insira a saudacao: ')).strip().title()
print(saudar(nome, saudacao))

# 107. Padrões e o papel do None/NoneType

def adicionar(item, lista = None): # o None evita de colocar 0 na lista
    if lista is None:
        lista = []
    lista.append(item)
    return lista   

# 108, 109 & 117. Escopo, namespace, global

contador = 0
def proximo():
    global contador # evite usar global 
    contador += 1
    return contador

def media(*nums): # o * vai receber todos valores
    return sum(nums) / len(nums) if nums else 0


# 136 (parte **kwargs). **kwargs (variável número de nomeados)

def configurar(**kwargs):
    debug = kwargs.get("debug", False)
    porta = kwargs.get("porta", 8000)
    return debug, porta