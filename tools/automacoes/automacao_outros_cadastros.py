from pyautogui import press
from time import sleep
from tools.automacoes.parada import parada

def automacao_outros_cadastros():
    # pula cep 
        press('tab')
        sleep(0.2)
        parada()

        # pula logradouro 
        press('tab')
        sleep(0.2)
        parada()

        # pula bairro 
        press('tab')
        sleep(0.2)
        parada()

        # pula cidade 
        press('tab')
        sleep(0.2)
        parada()

        # pula uf 
        press('tab')
        sleep(0.2)
        parada()

        # pula pais
        press('tab')
        sleep(0.2)
        parada()

        # pula telefone
        press('tab')
        sleep(0.2)
        parada()

        # pula fax 
        press('tab')
        sleep(0.2)
        parada()

        # pula celular
        press('tab')
        sleep(0.2)
        parada()

        # pula sexo
        press('tab')
        sleep(0.2)
        parada()