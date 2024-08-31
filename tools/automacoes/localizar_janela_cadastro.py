from pyautogui import locateCenterOnScreen
from time import time, sleep
from PySimpleGUI import Popup

def localizar_janela_cadastro():
    tempo_inicial = time()
    while True:
    
        if (time() - tempo_inicial) > 10:
            Popup("Janela de cadastro não encontrada")
            raise TypeError
        try:
            imagem = locateCenterOnScreen('reserva.PNG') or locateCenterOnScreen("reserva2.PNG")
            if imagem: 
                break
        except:
            sleep(0.5)


if __name__ == "__main__":
    localizar_janela_cadastro()