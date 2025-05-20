#input('Teste')
# Tipo primitivo INTEIRO = int // 1, 2, 3, 4, 5, -1, -2, -4
# Tipo primitivo FLAOT = float // 1.0, 2.5, 3.14, -1.0, -2.5, -4., 00.2
# Tipo primitivo STRING = str // 'Olá', '1', '2.5', '3.14', 'Teste'
# Tipo primitivo BOOLEANO = bool // True, False
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
#print('A soma entre os números são: ', s)

print(type(n1)) # <-- ver o tipo da variável

print('A soma entre {n1} e {n2} é igual a {s}'.format(n1=n1, n2=n2, s=s)) # <-- formatação de string
