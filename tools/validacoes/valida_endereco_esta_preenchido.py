from PySimpleGUI import Popup

def valida_endereco_esta_preenchido(janela_confirmacao, dados, cep):
    if len(cep) == 0 or len(dados['logradouro']) == 0 or len(dados['bairro']) == 0 or len(dados['cidade']) == 0:
        Popup('endereço inválido, verifique')
        janela_confirmacao.close()
        return False
    
    return True
    
        