algo = input("Digite alguma coisa: ")
print('A classe é: ', type(algo))
print('Ele é númerico?: ', algo.isnumeric()) # <-- verifica se é numérico
print('Ele é alfabético?: ', algo.isalpha()) # <-- verifica se é alfabético
print('Ele é alfanumerico: ', algo.isalnum()) # <-- verifica se é alfanumérico
print('Ele é maiusculo?: ', algo.isupper()) # <-- verifica se é maiúsculo
print('Ele é minúsculo?: ', algo.islower()) # <-- verifica se é minúsculo
print('Esta captalizado?: ', algo.istitle()) # <-- verifica se está captalizado
print('Só tem espaços?:', algo.isspace()) # <-- verifica se so tem espaços