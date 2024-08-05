import pyautogui as ag
from time import sleep
from PySimpleGUI import Popup
import os 

print(os.path.isfile("tools/imagens/image.png"))

while True:

    sleep(1)
    try:
        ag.locateCenterOnScreen('tools/imagens/image.png')
        Popup("Achei")

    except:
        print('imagem não encontrada')