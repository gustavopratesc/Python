
def leia_dinheiro(msg):
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            print(f'ERRO! É um preço invalido!')
            
    

    
## ou nao usando o try

def dinherio(msg):
    valor = False
    while not valor:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro {entrada} é um preço inválido!!')
        else:
            valor = True
            return float(entrada)