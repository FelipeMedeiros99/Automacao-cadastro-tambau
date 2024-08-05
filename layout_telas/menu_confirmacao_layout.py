import PySimpleGUI as sg

def menu_confirmacao_layout(nomes, cpfs, nascimentos, cpf_invalido):
    
    try:
      # abrir janela com todos os dados organizados
      layout = [
          [[sg.Text(f'Hóspede {pos+1}'), 
            sg.Input(nome, key="nome"), 
            
            sg.Text('cpf'),
            sg.Input(cpfs[pos], size=(13, 1), key="cpf"), sg.Text('nasc'),
            
            sg.Input(nascimentos[pos], size=(10,1), key='nascimento'),]
            for pos, nome in enumerate(nomes)],
          [sg.Button('Ok'), sg.Button('Cancelar')]
      ]

      return layout
    except IndexError:
      pass