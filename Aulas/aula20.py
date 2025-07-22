## TRY EXCEPT
 # o expect pode ter varios tipos de erro
# try:
#     print('Operação')
# except TypeError:
#     print('FALHA')
# except ValueError:
#     print('FALHA')
# except OSError:
#     print('FALHA')
# else: ## opcional
#     print('Deu certo')
# finally: ## opcional
#     print('Certo/Falha')


try:
    a = int(input('n:'))
    b = int(input('n:'))
    r = a / b
except (ValueError) or (TypeError): # <-- o as cria uma variavel chamada erro
    #print(f'Infelizmente tivemos um problema. Problema encontrado {erro.__class__}') # o class puxa a classe do problema
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possivel dividir o número por zero')
except KeyboardInterrupt:
    print('O usuario não informou os tipos de dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}') # <-- .__cause__ vai mostrar a causa do erro
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Volte sempre muito Obrigado!')