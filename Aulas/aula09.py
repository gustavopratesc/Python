# switch case no python é = match case
# nao possui break no match case <-, nao possui default
opcao = int(input('Numero de 1 a 3: '))
match opcao:
    case 1:
        print('opcao um')
    case 2:
        print('Opcao 2')
    case 3:
        print('opcao 3')
    
## continue e try except

## try except

# Imagine que seu código vai fazer algo arriscado — como dividir um número ou converter texto em número. Se der erro, o programa normalmente para na hora.
# Com try / except, você diz:

# “Python, tente fazer isso (try), mas se der erro, me avise e continue sem travar tudo (except).”

try:
    # Código que pode dar erro
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

except ValueError:
    print("Erro: Você não digitou um número válido.")

except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")


# try:	Bloco onde você testa algo que pode falhar
# except	Bloco que roda se acontecer um erro
# Exception	Tipo de erro genérico
# as erro	Guarda detalhes do erro numa variável
# finally:	(Opcional) Sempre executa, mesmo se der erro ou não

#  Dica de dev pro:
# Você pode usar except Exception as e: para ver qualquer erro inesperado, especialmente em testes ou debug:

# try:
#     # código
# except Exception as e:
#     print(f"Erro inesperado: {e}")

try:
    numero = int(input('Digite um número inteiro: '))
    print(f'Você digitou um número certo {numero}')
except ValueError:
    print('Você digitou um valor invalido! ')

try:
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    div = n1 / n2

except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except ValueError:
    print('Valor errado!')

try:
    preco = str(input('Digite um preço com .')).replace(',', '.')

    print(f'Preço R${float(preco)}')
except ValueError:
    print('O valor saiu errado')