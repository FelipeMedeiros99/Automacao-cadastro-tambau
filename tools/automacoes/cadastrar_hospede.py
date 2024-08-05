from time import sleep
from tools.automacoes.parada import parada
from pyautogui import press, click, hotkey, write
from pyperclip import copy


def cadastrar_hospede(nome, cpf, nascimento, cep, logradouro, bairro, cidade, telefone, email):
    press('tab')
    sleep(0.5)
    parada()

    click(x=1174, y=282)
    # cpf
    copy(cpf)
    hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    press('tab')
    sleep(0.2)
    parada()
    click(x=816, y=477)
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

    press('backspace')
    write(telefone)
    sleep(0.2)
    press('tab')
    sleep(0.2)
    press('tab')
    sleep(0.2)

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
    click(x=676, y=529)
    sleep(0.2)
    click(x=682, y=496)
    sleep(0.2)
    click(x=886, y=479)
    sleep(0.2)
    click(x=886, y=479)
    sleep(0.2)