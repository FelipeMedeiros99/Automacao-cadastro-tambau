from re import compile, findall

def filtro_datas_de_nascimento(txt):
    regex_nascimento = r'(0[0-9]|[12][0-9]|3[01])\D?(0[0-9]|1[0-2])\D?(19[7-9]\d|20\d\d)'
    padrao = compile(regex_nascimento)
    nascimentos = findall(padrao, txt)
    nascimentos_ajustados = []

    for nascimento in nascimentos: 
        nascimento = list(nascimento)
        nascimentos_ajustados.append('/'.join(nascimento))
    
    return nascimentos_ajustados

