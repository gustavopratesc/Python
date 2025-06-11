"""As empresas aéreas calculam o preço médio das suas bagagens considerando o peso médio das
malas despachadas durante um ano. O valor de cada quilo corresponde a R$ 10,00. Você deve ler
2
os pesos até que uma bagagem com peso zero seja informada. No final, exiba o peso médio das
bagagens e o novo preço da bagagem."""

quilo_bagagem = 10
soma_bagagem = 0
contador = 0

while True:
    peso_bagagem = float(input('Insira o peso da bagagem: '))
    if peso_bagagem == 0:
        break
    contador += 1
    print('Contagem de bagagens: {}'.format(contador))
    soma_bagagem += peso_bagagem

if contador > 0:
    media_bagagem = soma_bagagem / contador
    total_preco_bagagem = media_bagagem * quilo_bagagem

    print('A media da bagagem ficou: {}'.format(media_bagagem))
    print('O total a se pegar pelas bagagens ficou R${:.2f}'.format(total_preco_bagagem))
else:
    print('Nenhuma bagagem foi registrada!!')


    