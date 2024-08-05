from layout_telas.menu_confirmacao_layout import menu_confirmacao_layout
from tools.filtrar_dados_janela_confirmacao import filtrar_dados_janela_conmfirmacao
from tools.valida_endereco_esta_preenchido import valida_endereco_esta_preenchido
from tools.processo_de_cadastro import processo_de_cadastro

import PySimpleGUI as sg

def janela_confirmacao(dados, nomes, cpfs, cpf_invalido, nascimentos, cep, contato):
    
    print("nascimentos: ", nascimentos)

    layout_janela_confirmacao = menu_confirmacao_layout(nomes, cpfs, nascimentos, cpf_invalido)
    janela_confirmacao = sg.Window('dados', layout_janela_confirmacao)

    while True:
        botoes_tela_confirmacao, dados_tela_confirmacao = janela_confirmacao.Read()
        nomes, cpfs, nascimentos = filtrar_dados_janela_conmfirmacao(dados_tela_confirmacao)

        if botoes_tela_confirmacao == sg.WINDOW_CLOSED or botoes_tela_confirmacao == 'Cancelar':
            janela_confirmacao.close()
            break

        if botoes_tela_confirmacao == 'Ok':
            endereco_esta_preenchido = valida_endereco_esta_preenchido(janela_confirmacao, dados, cep)
            if not endereco_esta_preenchido:
                break 
            
            processo_de_cadastro(janela_confirmacao, nomes, cpfs, nascimentos, cep, dados, contato)

            break

