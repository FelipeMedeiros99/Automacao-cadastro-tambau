from tools.automacoes.localizar_janela_cadastro import localizar_janela_cadastro 
from tools.automacao import editar_hospede, cadastrar_hospede, fechar_janela
from PySimpleGUI import Popup

def processo_de_cadastro(janela_confirmacao, nomes, cpfs, nascimentos, cep, dados, contato):
    janela_confirmacao.close()
    try:
        localizar_janela_cadastro()
        for c in range(len(nomes)):
            
            # abrindo ediçao do hóspede
            editar_hospede()

            # automação cadastro
            cadastrar_hospede(nomes[c], cpfs[c], nascimentos[c], cep, dados['logradouro'],
                                dados['bairro'], dados['cidade'], contato, dados['email'])

        fechar_janela()

    except:
        Popup('Automação parada')
    