from pyautogui import click
from time import sleep

def fechar_janela():
    botao_de_close = (946, 420)
    click(botao_de_close)
    
    # sleep(0.5)
    # click(x=1021, y=354)