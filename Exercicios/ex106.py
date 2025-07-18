"""FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VARIAS NOTAS DE ALUNOS E VAI RETORNAR UM DICIONARIO COM AS SEGUINTES INFORMAÇÕES:
    - QUANTIDADE DE NOTAS
    - A MAIOR NOTA
    - A MEDIA DA TURMA
    - A SITUAÇÃO (OPCIONAL)
    ADICIONAR TAMBEM AS DOCSTRINGS DA DEF 
"""

def notas(*nota, sit=False):
    """
    FUNÇÃO QUE MOSTRA:
    TOTAL NOTA
    MAIOR NOTA
    MENOR NOTA
    MEDIA NOTA
    SITUAÇÃO BOA, MEDIANA, RUIM
    """
    notas_alunos = list(nota)
    media = sum(notas_alunos) / len(notas_alunos)
    resultado = {
        'total': len(notas_alunos), 
        'Maior': max(notas_alunos), 
        'Menor': min(notas_alunos), 
        'Media': media
        }
    if sit:
        if media >= 7:
            resultado['Situação'] = 'BOA'
        elif media >= 5:
            resultado['Situação'] = 'MEDIANA'
        else:
            resultado['Situação'] = 'RUIM'
    return resultado

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

## resposta do professor

def notas(*n, sit=False):
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n) / len(n)
    if sit:
        if r['Media'] > 7:
            r['Situação'] = 'BOA'
        elif r['Media'] >= 5:
            r['Situação'] = 'RAZOAVEL'
        else:
            r['Situação'] = 'RUIM'
    return r
    


# programa principal
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)