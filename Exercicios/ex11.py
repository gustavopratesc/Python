celcius = float(input('Digite uma temperatura em celcius °C para transformar em Fahrenheit °F: '))
fah = (celcius * 1.8) + 32
# ou outra formula seria fah = ((9*c)/5)+32
print('A temperatura {}°C em Fahrenheit é {}°F'.format(celcius, fah))