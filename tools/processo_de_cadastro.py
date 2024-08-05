from tools.automacoes.localizar_janela_cadastro import localizar_janela_cadastro 
from tools.automacoes.fechar_janela import fechar_janela
from tools.automacoes.cadastrar_hospede import cadastrar_hospede
from tools.automacoes.editar_hospede import editar_hospede
from PySimpleGUI import Popup

def processo_de_cadastro(janela_confirmacao, nomes, cpfs, nascimentos, cep, dados, contato):
    janela_confirmacao.close()
    try:
        localizar_janela_cadastro()

        for c in range(len(nomes)):
            editar_hospede()

            # automação cadastro
            cadastrar_hospede(nomes[c], 
                              cpfs[c], 
                              nascimentos[c], 
                              cep, 
                              dados['logradouro'],
                              dados['bairro'], 
                              dados['cidade'], 
                              contato, 
                              dados['email'])

        fechar_janela()

    except:
        Popup('Automação parada')
    