from re import compile


def filtro_nomes(dados):
    nomes = []
    # filtrando dados com numeros
    modelo_numeros = compile(r'[0-9]+')
    for dado in dados['dados'].split('\n'):
        if not modelo_numeros.findall(dado):
            nomes.append(dado.strip())

    # filtrando caracteres especiais e espaços vazops
    nomes = [''.join(list(filter(
                lambda caractere: not caractere in [':', '=', '*', '\\', ';', '?', ',', '.'], nome)))
                for nome in nomes if len(nome) > 0]
    return nomes 
