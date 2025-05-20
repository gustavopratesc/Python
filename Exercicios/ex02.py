numero = int(input('Digite algum número para saber seu sucessor e seu antecessor: '))

sucessor = numero + 1
antecessor = numero - 1

print('O número é {}\n Seu Sucessor é {}\n Seu Antecessor é {}'.format(numero, sucessor, antecessor))

# outra forma de fazer seria
# print('O número é {} Seu sucessor é {} Seu antecessor é {}'.format(numero, (numero + 1), (numero - 1)))