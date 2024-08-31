from pyautogui import locateCenterOnScreen
from time import time, sleep
from PySimpleGUI import Popup

def localizar_janela_cadastro():
    tempo_inicial = time()
    while True:
    
        if (time() - tempo_inicial) > 5:
            Popup("Janela de cadastro não encontrada")
            raise TypeError
        try:
            imagem1 = locateCenterOnScreen('reserva.PNG', confidence=0.8)
            imagem2 = locateCenterOnScreen("reserva2.PNG", confidence=0.8)
            if imagem1 or imagem2: 
                break
        except:
            sleep(0.5)
            continue


if __name__ == "__main__":
    localizar_janela_cadastro()