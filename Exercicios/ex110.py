"""DENTRO DO PACOTE utilidadescev QUE CRIAMOS NO DESAFIO ANTERIOR, TEMOS UM MODULO CHAMADO DADO. CRIE UMA FUNÇÃO CHAMA leiadinheiro() QUE SEJA CAPAZ DE FUNCIONAR COMO UMA FUNÇÃO INPUT() MAS COM UMA VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES QUE SEJAM MONETARIOS"""
from utilidadescev import dados
import moeda
p = dados.leia_dinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)