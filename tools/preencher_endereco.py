from PySimpleGUI import Popup
from tools.filtra_numeros import filtra_numeros
from pycep import PyCep

def preencher_endereco(janela, dados):
    cep = ''
    try:
        busca = PyCep(filtra_numeros(dados['cep']))
        endereco = busca.dadosCep
        janela['cep'].update(endereco['cep'])
        janela['bairro'].update(endereco['bairro'])
        janela['logradouro'].update(endereco['logradouro'])
        janela['cidade'].update(endereco['localidade'])
        cep = endereco['cep']

    except Exception as erro:
        print(erro)
        Popup('cep inválido')

    finally:
        return cep