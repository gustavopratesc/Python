from time import sleep
print('Todos os números pares de 1 a 50')
sleep(1)

#for i in range(0, 51, 2):
#    print(i)

# ou

for i in range(0, 51):
    if i % 2 == 0:
        print(i)