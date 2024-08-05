from pyautogui import position, FailSafeException

def parada():
    if position() == (0, 0):
        raise FailSafeException