import pyautogui
from pyautogui import *


def parada():
    if position() == (0, 0):
        raise pyautogui.FailSafeException


def abrir_programa():
    import pyautogui as ag
    from time import sleep
    ag.click(x=561, y=876)
    sleep(1)


def abrir_reservas(nova=False):
    import pyautogui as ag
    from time import sleep
    ag.hotkey('ctrl', 'f')
    sleep(1)

    if nova:
        ag.click(x=280, y=222)
        sleep(1)
        ag.click(x=487, y=402)
        sleep(1)
    else:
        ag.click(x=280, y=222)
        sleep(1)
        ag.click(x=487, y=303)
        sleep(1)


def editar_reserva(num_reserva):
    import pyautogui as ag
    from time import sleep
    num_reserva = ''.join([num for num in num_reserva if num.isnumeric()])
    ag.write(num_reserva)
    sleep(2)
    [ag.click(x=471, y=286) for c in range(2)]
    sleep(1)
    [ag.click(x=468, y=443) for c in range(2)]
    sleep(1)


def editar_hospede():
    import pyautogui as ag
    from time import sleep
    parada()
    ag.click(x=1174, y=282)
    sleep(1)
    parada()
    ag.click(x=799, y=434)
    sleep(1)
    parada()


def cadastrar_hospede(nome, cpf, nascimento, cep, logradouro, bairro, cidade, telefone, email):
    import pyautogui as ag
    from time import sleep
    import pyperclip as pc
    ag.press('tab')
    sleep(0.5)
    parada()

    ag.click(x=1174, y=282)
    # cpf
    pc.copy(cpf)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    ag.press('tab')
    sleep(0.2)
    parada()
    ag.click(x=816, y=477)
    sleep(0.2)
    parada()

    # nome
    pc.copy(nome)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    ag.press('tab')
    sleep(0.2)
    parada()

    # cep
    pc.copy(cep)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    ag.press('tab')
    sleep(0.2)
    parada()

    # logradouro
    pc.copy(logradouro)
    ag.hotkey('ctrl', 'a')
    parada()
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    ag.press('tab')
    parada()

    # bairro
    pc.copy(bairro)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    ag.press('tab')
    parada()

    # cidade
    pc.copy(cidade)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    parada()
    ag.press('tab')
    sleep(0.2)
    parada()
    ag.press('tab')
    sleep(0.2)

    ag.press('tab')

    # telefone
    pc.copy(telefone)
    ag.press('backspace')
    ag.write(telefone)
    sleep(0.2)
    ag.press('tab')
    sleep(0.2)
    ag.press('tab')
    sleep(0.2)

    ag.press('backspace')
    ag.write(telefone)
    sleep(0.2)
    ag.press('tab')
    sleep(0.2)
    ag.press('tab')
    sleep(0.2)

    # nascimento
    pc.copy(nascimento)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)
    ag.press('tab')
    sleep(0.2)

    pc.copy(email)
    ag.hotkey('ctrl', 'v')
    sleep(0.2)

    # fechando
    ag.click(x=676, y=529)
    sleep(0.2)
    ag.click(x=682, y=496)
    sleep(0.2)
    ag.click(x=886, y=479)
    sleep(0.2)
    ag.click(x=886, y=479)
    sleep(0.2)


def fechar_janela():
    import pyautogui as ag
    from time import sleep
    #ag.click(x=1022, y=352)
    ag.click(x=1174, y=282)
    
    sleep(0.5)
    ag.click(x=1021, y=354)


def adicionar_quarto():
    import pyautogui as ag
    ag.click(x=1131, y=439)



if __name__ == "__main__":
    pass