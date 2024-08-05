from pyautogui import locateCenterOnScreen
from time import time, sleep
from PySimpleGUI import Popup

def localizar_janela_cadastro():
    tempo_inicial = time()
    while True:
    
        if (time() - tempo_inicial) > 5:
            Popup("Janela de cadastro não encontrada")
            break
        try:
            imagem = locateCenterOnScreen('reserva.PNG')
            if imagem: 
                break
        except:
            sleep(0.5)
            continue


if __name__ == "__main__":
    localizar_janela_cadastro()