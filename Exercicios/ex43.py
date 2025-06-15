import random
# pedra papel ou tesoura
print('Pedra papel e tesoura!!')

opcao = str(input('Insira pedra, papel ou tesoura: ')).lower().strip()

sorteio = random.choice(['pedra', 'papel', 'tesoura'])
print(sorteio)

if opcao == 'pedra' and sorteio == 'pedra':
    print('Empate!')
elif opcao == 'papel' and sorteio == 'papel':
    print('Empate!')
elif opcao == 'tesoura' and sorteio == 'tesoura':
    print('Empate!')
elif opcao == 'papel' and sorteio == 'pedra':
    print('Você ganhou!')
elif opcao == 'pedra' and sorteio == 'papel':
    print('bot ganhou')
elif opcao == 'tesoura' and sorteio == 'pedra':
    print('bot ganhou')
elif opcao == 'pedra' and sorteio == 'tesoura':
    print('Você ganhou') 
elif opcao == 'tesoura' and sorteio == 'papel':
    print('Você ganhou')
elif opcao == 'papel' and sorteio == 'tesoura':
    print('Você ganhou')
else:
    print('Insira os dados corretamente')

## ou DA FORMA DO CHATGPT

print('Pedra, Papel e Tesoura!!')

opcao = input('Insira pedra, papel ou tesoura: ').lower().strip()
sorteio = random.choice(['pedra', 'papel', 'tesoura'])
print(f'Bot jogou: {sorteio}')

if opcao == sorteio:
    print('Empate!')
elif opcao == 'pedra' and sorteio == 'tesoura':
    print('Você ganhou!')
elif opcao == 'tesoura' and sorteio == 'papel':
    print('Você ganhou!')
elif opcao == 'papel' and sorteio == 'pedra':
    print('Você ganhou!')
elif opcao in ['pedra', 'papel', 'tesoura']:
    print('Bot ganhou!')
else:
    print('Insira uma opção válida!')
