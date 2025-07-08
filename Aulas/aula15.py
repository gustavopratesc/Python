dados = dict()
dados = {'nome':'Pedro', 'idade': 25}
print(dados['nome']) # <-- pedro
print(dados['idade']) # <-- 25
dados['sexo'] = 'M' # <-- não existe append nos dicionarios é feito assim

filme = {
    'Titulo': 'Star Wars',
    'Ano': 1997,
    'Diretor': 'George Lucas'
}

print(filme.values()) # <-- vai mostrar todos os valores, como star wars, 1997, george lucas
print(filme.keys()) # <-- vai pegar o titulo, ano, e diretor
print(filme.items()) # <-- vai pegar tudo

for k, v in filme.items():
    print(f'O {k} é {v}')


pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}

print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # <-- usa aspas duplas dentro dos colchetes

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys(): # <-- mostra so nome, sexo, idade
    print(k)
for k in pessoas.values(): # <-- mostra o Gustavo, M, 22
    print(k)

for k, v in pessoas.items(): # o K pega as keys nome idade etc.., o V pega os valores Gustavo, M etc...
    print(f'{k} = {v}')

#del pessoas('sexo') # <-- aqui deleta
pessoas['nome'] = 'Leandro' # o nome Gustavo Vira Leandro

pessoas['peso'] = 98.5 # <-- aqui adiciona na lista o peso


##
## Juntar dicionarios com listas
estado = {
    'uf': 'Rio de janeiro', 
    'sigla': 'RJ' 
}
estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}
brasil = []
brasil.append(estado) 
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf']) # <-- aqui puxa o estado do indice 0
print(brasil[0]['sigla']) # <-- aqui puxa a sigla do indice 0

#####

## codigos importantes usando FOR

state = dict()
brazil = list()

for c in range(3):
    state['uf'] = str(input('Unidade Federativa: '))
    state['sigla'] = str(input('Sigla do Estado: '))
    brazil.append(state.copy())  # <-- aqui usa o copy em vez do [:]

## print formatado
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')

    ## ou
    
for e in brasil:
    for v in e.values():
        print(v)