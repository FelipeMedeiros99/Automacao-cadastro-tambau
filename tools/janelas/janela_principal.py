from tools.filtros.filtro_nomes import filtro_nomes
from tools.validacoes.validar_cpfs import validar_cpfs
from tools.correcao_dados.correcao_contato import correcao_contato
from tools.automacoes.preencher_endereco import preencher_endereco
from tools.janelas.janela_confirmacao import janela_confirmacao
from tools.filtros.filtro_datas_de_nascimento import filtro_datas_de_nascimento
from tools.validacoes.valida_endereco_esta_preenchido import valida_endereco_esta_preenchido
from layout_telas.menu_principal_layout import menu_principal_layout

from PySimpleGUI import WINDOW_CLOSED, Window, Popup

def janela_principal():

    # layout da primeira janela
    layout_menu_principal = menu_principal_layout()
    menu_principal = Window('Automação de cadastros', layout_menu_principal)
    cep=''

    while True:
        # ------ definindo variáveis -----------
        botoes, dados = menu_principal.Read()
        nascimentos = filtro_datas_de_nascimento(dados['dados'])
        cpfs, cpf_invalido = validar_cpfs(dados['dados'])
        nomes = filtro_nomes(dados)
        contato = correcao_contato(dados['contato'])

        if botoes == WINDOW_CLOSED or botoes == 'Cancelar':
            menu_principal.close()
            break

        if botoes == 'Buscar':
            cep = preencher_endereco(menu_principal, dados)
            
        while len(nascimentos) < len(cpfs):
            nascimentos.append('')

        if botoes == 'Ok':
            if len(cpf_invalido) > 0:
                texto = f"CPF(s) invalido(s): \n\n{str(cpf_invalido).replace("[", "").replace("]", '').replace(", ", '\n')}"
                Popup(texto)
        
            elif not valida_endereco_esta_preenchido(dados, cep):
                Popup('endereço inválido, verifique')

            else:
                janela_confirmacao(dados, nomes, cpfs, cpf_invalido, nascimentos, cep, contato)