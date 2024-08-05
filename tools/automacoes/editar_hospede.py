from pyautogui import click
from tools.automacoes.parada import parada
from time import sleep


def editar_hospede():
    parada()
    click(x=1174, y=282)
    sleep(1)
    parada()
    click(x=799, y=434)
    sleep(1)
    parada()
