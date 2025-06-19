contador = 0
soma_numeros = 0

print('Insira varios números inteiros que quiser e 999 para parar e somar!')
while True:
    numero = int(input('Insira um número: '))
    if numero == 999:
        print('Você parou!')
        break
    
    contador += 1
    soma_numeros += numero
        
print(contador)
print(soma_numeros)
