def filtrar_dados_janela_conmfirmacao(dados_tela_confirmacao):
    nomes = []
    cpfs = []
    nascimentos = []

    for dados in dados_tela_confirmacao.items():
        if 'nome' in str(dados[0]):
            nomes.append(dados[1])

        if 'cpf' in str(dados[0]):
            cpfs.append(dados[1])

        if 'nascimento' in str(dados[0]):
            nascimentos.append(dados[1])
    
    return nomes, cpfs, nascimentos