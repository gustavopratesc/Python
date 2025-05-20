#operadores aritmeticos
# **, *, /, //, %, +, -
#
#Ordem de precedencia
# (), **, * / // %, + -

###################################################################################################
name = input('Qual é seu nome?')
print('Prazer em te conhecer {:20}!'.format(name))
print('Prazer em te conhecer {:>20}!'.format(name)) #  direita
print('Prazer em te conhecer {:<20}!'.format(name)) #  esquerda
print('Prazer em te conhecer {:^20}!'.format(name)) # centraliza no meio entre 20 espaços divididos
print('Prazer em te conhecer {:=^20}!'.format(name)) # meio com algumas caracteristicas

###################################################################################################

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

sub = n1 - n2
mult = n1 * n2
poten = n1 ** n2
div = n1 / n2
restodiv = n1 % n2
divinteira = n1 // n2 

# \n <-- é para quebrar a linha, tipo um (enter)

print('A soma entre os \ndois números é {}'.format((n1 + n2))) # +
print('A subtração entre os dois números é: {}'.format(sub)) # -
print('A multiplicação entre dois números é: {}'.format(mult)) # *
print('A potencia entre dois números é: {}'.format(poten)) # **
print('A divisão entre dois números é: {}'.format(div)) # /
print('O resto da divisão entre dois números é: {}'.format(restodiv)) # %
print('A divisão inteira entre dois números é: {}'.format(divinteira)) # //