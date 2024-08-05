from re import compile, findall
from datetime import date

def filtro_datas_de_nascimento(txt):
    regex_nascimento = r'(0[0-9]|[12][0-9]|3[01]).?(0[0-9]|1[0-2]).?(19[7-9]\d|20\d\d|\d{2})'
    padrao = compile(regex_nascimento)
    nascimentos = findall(padrao, txt)
    nascimentos_ajustados = []

    for nascimento in nascimentos: 
        nascimento = list(nascimento)
        if len(nascimento[2]) == 2:
            nascimento[2] = f'19{nascimento[2]}'
        nascimentos_ajustados.append('/'.join(nascimento))
    
    return nascimentos_ajustados

