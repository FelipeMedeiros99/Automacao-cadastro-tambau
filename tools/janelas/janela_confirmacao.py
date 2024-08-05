from layout_telas.menu_confirmacao_layout import menu_confirmacao_layout
from tools.filtros.filtrar_dados_janela_confirmacao import filtrar_dados_janela_conmfirmacao
from tools.automacoes.processo_de_cadastro import processo_de_cadastro

from PySimpleGUI import Window, WINDOW_CLOSED

def janela_confirmacao(dados, nomes, cpfs, cpf_invalido, nascimentos, cep, contato):

    layout_janela_confirmacao = menu_confirmacao_layout(nomes, cpfs, nascimentos, cpf_invalido)
    janela_confirmacao = Window('dados', layout_janela_confirmacao)

    while True:
        botoes_tela_confirmacao, dados_tela_confirmacao = janela_confirmacao.Read()
        nomes, cpfs, nascimentos = filtrar_dados_janela_conmfirmacao(dados_tela_confirmacao)

        if botoes_tela_confirmacao == WINDOW_CLOSED or botoes_tela_confirmacao == 'Cancelar':
            janela_confirmacao.close()
            break

        if botoes_tela_confirmacao == 'Ok':
            processo_de_cadastro(janela_confirmacao, nomes, cpfs, nascimentos, cep, dados, contato)

            break

