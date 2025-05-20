nota1 = float(input('Insira a sua primeira nota: '))
nota2 = float(input('Insira a sua segunda nota: '))

media = (nota1 + nota2) / 2

print('Sua primeira nota foi {nota1}\n Sua segunda nota foi {nota2}\n Sua media foi {media}'
      .format(nota1=nota1, nota2=nota2, media=media))