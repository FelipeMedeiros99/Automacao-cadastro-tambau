from layout_telas.menu_confirmacao_layout import menu_confirmacao_layout
from tools.automacao import localizar_janela, editar_hospede, cadastrar_hospede, fechar_janela, parada
from tools.filtrar_dados_janela_confirmacao import filtrar_dados_janela_conmfirmacao

import PySimpleGUI as sg

def janela_confirmacao(dados, nomes, cpfs, cpf_invalido, nascimentos, cep, contato):
    layout_janela_confirmacao = menu_confirmacao_layout(nomes, cpfs, nascimentos, cpf_invalido)
    janela_confirmacao = sg.Window('dados', layout_janela_confirmacao)

    while True:
        botoes_tela_confirmacao, dados_tela_confirmacao = janela_confirmacao.Read()
        nomes, cpfs, nascimentos = filtrar_dados_janela_conmfirmacao(dados_tela_confirmacao)

        if botoes_tela_confirmacao == sg.WINDOW_CLOSED or botoes_tela_confirmacao == 'Cancelar':
            janela_confirmacao.close()
            break

        elif botoes_tela_confirmacao == 'Ok':
            if len(cep) == 0 or len(dados['logradouro']) == 0 or len(dados['bairro']) == 0 or len(dados['cidade']) == 0:
                sg.Popup('endereço inválido, verifique')
                janela_confirmacao.close()
                break
            
            try:
                localizar_janela()
                for c in range(len(nomes)):

                    # abrindo ediçao do hóspede
                    editar_hospede()

                    # automação cadastro
                    cadastrar_hospede(nomes[c], cpfs[c], nascimentos[c], cep, dados['logradouro'],
                                        dados['bairro'], dados['cidade'], contato, dados['email'])

                fechar_janela()

            except:
                sg.popup('Automação parada')
                break
            break

