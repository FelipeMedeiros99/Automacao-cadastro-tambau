from time import sleep
from tools.automacoes.parada import parada
from pyautogui import press, click, hotkey, write
from pyperclip import copy

def automacao_primeiro_cadastro(cep, logradouro, bairro, cidade, telefone):
    # cep
    copy(cep)
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    sleep(0.2)
    parada()

    # logradouro
    copy(logradouro)
    hotkey('ctrl', 'a')
    parada()
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    parada()

    # bairro
    copy(bairro)
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    parada()

    # cidade
    copy(cidade)
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    sleep(0.2)
    parada()
    press('tab')
    sleep(0.2)

    press('tab')

    # telefone
    copy(telefone)
    press('backspace')
    write(telefone)
    sleep(0.2)
    press('tab')
    sleep(0.2)
    press('tab')
    sleep(0.2)

    # telefone
    press('backspace')
    write(telefone)
    sleep(0.2)
    press('tab')
    sleep(0.2)
    press('tab')
    sleep(0.2)