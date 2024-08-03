from re import compile, findall
from datetime import date

def filtro_datas_de_nascimento(txt):
    padrao = compile(r'(\d{2}).?(\d{2}).?(\d{4}|\d{2})')
    nascimentos = findall(padrao, txt)
    nascimentos_ajustados = []

    for nascimento in nascimentos: 
        nascimento = list(nascimento)
        if len(nascimento[2]) == 2:
            nascimento[2] = f'19{nascimento[2]}'
        nascimentos_ajustados.append('/'.join(nascimento))
    
    return nascimentos_ajustados

