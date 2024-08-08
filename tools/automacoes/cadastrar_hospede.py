from time import sleep
from tools.automacoes.parada import parada
from tools.automacoes.automacao_primeiro_cadastro import automacao_primeiro_cadastro
from tools.automacoes.automacao_outros_cadastros import automacao_outros_cadastros
from pyautogui import press, click, hotkey, write
from pyperclip import copy

def cadastrar_hospede(nome, cpf, nascimento, cep, logradouro, bairro, cidade, telefone, email, contador_execucoes):

    confirmar_caso_hospede_tenha_cadastro = (713, 537)
    salvar_cadastro_do_hospede = (595, 586)
    confirmar_cadastro_do_hospede = (593, 560)
    confirmar_caso_hospede_ja_possua_reserva = (801, 540)
    press('tab')
    sleep(0.5)
    parada()
    
    # cpf
    copy(cpf)
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    sleep(0.2)
    parada()
    click(confirmar_caso_hospede_tenha_cadastro)
    sleep(0.2)
    parada()

    # nome
    copy(nome)
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    sleep(0.2)
    parada()

    if contador_execucoes == 0:
        automacao_primeiro_cadastro(cep, logradouro, bairro, cidade, telefone)
    
    else:
        automacao_outros_cadastros()

    # nascimento
    copy(nascimento)
    hotkey('ctrl', 'v')
    sleep(0.2)
    press('tab')
    sleep(0.2)

    copy(email)
    hotkey('ctrl', 'v')
    sleep(0.2)

    # fechando
    click(salvar_cadastro_do_hospede)
    sleep(0.2)
    click(confirmar_cadastro_do_hospede)
    sleep(0.01)
    click(confirmar_caso_hospede_ja_possua_reserva)
    sleep(0.01)
    click(confirmar_caso_hospede_ja_possua_reserva)
    sleep(0.2)