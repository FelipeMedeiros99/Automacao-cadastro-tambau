from pyautogui import position
from PySimpleGUI import Popup
def localizar_ponto():
    return position()

if __name__ == "__main__":
    while True:
        input()
        print(localizar_ponto())
        