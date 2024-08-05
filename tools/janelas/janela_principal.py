from tools.filtro_nomes import filtro_nomes
from tools.correcao_de_dados import modelo_cpf, modelo_de_contato
from tools.preencher_endereco import preencher_endereco
from tools.janela_confirmacao import janela_confirmacao
from tools.filtro_datas_de_nascimento import filtro_datas_de_nascimento
from layout_telas.menu_principal_layout import menu_principal_layout


from PySimpleGUI import WINDOW_CLOSED, Window

def janela_principal():

    # layout da primeira janela
    layout_menu_principal = menu_principal_layout()
    menu_principal = Window('Automação de cadastros', layout_menu_principal)
    cep=''

    while True:
        # ------ definindo variáveis -----------
        botoes, dados = menu_principal.Read()
        nascimentos = filtro_datas_de_nascimento(dados['dados'])
        cpfs, cpf_invalido = modelo_cpf(dados['dados'])
        nomes = filtro_nomes(dados)
        contato = modelo_de_contato(dados['contato'])

        if botoes == WINDOW_CLOSED or botoes == 'Cancelar':
            break

        if botoes == 'Buscar':
            cep = preencher_endereco(menu_principal, dados)
            
        # deixando a lista de nascimento proporcional
        while len(nascimentos) < len(cpfs):
            nascimentos.append('')

        if botoes == 'Ok':
            janela_confirmacao(dados, nomes, cpfs, cpf_invalido, nascimentos, cep, contato)