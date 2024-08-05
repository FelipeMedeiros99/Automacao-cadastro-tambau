def valida_endereco_esta_preenchido(dados, cep):
    if len(cep) == 0 or len(dados['logradouro']) == 0 or len(dados['bairro']) == 0 or len(dados['cidade']) == 0:
        return False
    return True
    
        