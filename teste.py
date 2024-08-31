from time import sleep
from pyautogui import locateCenterOnScreen


while True:
    sleep(0.5)
    try:
        imagem = locateCenterOnScreen("reserva2.PNG")
        print(imagem)
    except:
        print('.')