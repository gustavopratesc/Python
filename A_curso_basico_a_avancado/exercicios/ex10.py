def boletim(**notas):
    media = sum(notas.values()) / len(notas) # .values() para pegar apenas os valores
    return media

notas = {
    "matematica": float(input('Insira a nota de matematica: ')),
    "português": float(input('Insira a nota de português: ')),
    "inglês": float(input('Insira a nota de inglês: '))
}

print(f'A media das suas todas foram: {boletim(**notas):.2f}')