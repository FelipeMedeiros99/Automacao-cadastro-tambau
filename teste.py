from time import sleep
from pyautogui import locateCenterOnScreen


while True:
    sleep(2)
    imagem = locateCenterOnScreen("reserva2.PNG")
    print(imagem)