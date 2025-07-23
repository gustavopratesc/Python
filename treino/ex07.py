n = input('Insira um número: ').strip()

eh_inteiro = False
eh_float = False
eh_positivo = False

try:
    numero_int = int(n)
    eh_inteiro = True
    if numero_int > 0:
        eh_positivo = True
except ValueError:

    try:
        numero_float = float(n)
        eh_float = True
        if numero_float > 0:
            eh_positivo = True
    except ValueError:
        pass

print(f'Ele é inteiro?: {eh_inteiro}')
print(f'Ele é float?: {eh_float}')
print(f'Ele é positivo?: {eh_positivo}')