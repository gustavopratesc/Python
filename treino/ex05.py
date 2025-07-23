valor = input('Insira qualquer valor: ').strip().lower()

eh_inteiro = False
eh_float = False
eh_bool = False

try:
    int(valor)
    eh_inteiro = True
except ValueError:
    pass

try:
    float(valor)
    eh_float = True
except ValueError:
    pass

if valor in ['true', 'false']:
    eh_bool = True

print(f'Pode ser convertido para inteiro?: {eh_inteiro}')
print(f'Pode ser convertido para float?: {eh_float}')
print(f'Pode ser convertido para bool?: {eh_bool}')
