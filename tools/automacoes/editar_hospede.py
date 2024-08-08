from pyautogui import click
from tools.automacoes.parada import parada
from time import sleep


def editar_hospede():
    botao_adicionar = (1092, 340)
    botao_cadastrar = (718, 504)
    parada()
    click(botao_adicionar)
    sleep(1)
    parada()
    click(botao_cadastrar)
    sleep(1)
    parada()
