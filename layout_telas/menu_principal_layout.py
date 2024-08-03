import PySimpleGUI as sg

def menu_principal_layout():
    layout = [
        # índices 0 - nomes
        [
            sg.Text('nomes, cpfs e nascimentos:', size=(35, 1)),
        ],

        # caixas 0 - dados
        [
            sg.Multiline(size=(37, 5), key='dados'),
        ],

        # índices 2 - cep e logradouro
        [
            sg.Text('cep:', size=(18, 1)),
            sg.Text('logradouro:', size=(14, 1)),
        ],

        # caixas 2 - cep, botao e logradouro
        [
            sg.Input(key='cep', size=(11, 1)),
            sg.Button('Buscar', size=(6, 1)),
            sg.Input(key='logradouro', size=(17, 1)),

        ],

        # indices 3 - bairro e cidade
        [
            sg.Text('bairro:', size=(18, 1)),
            sg.Text('cidade:', size=(17, 1)),
        ],
        # caixas 3 - bairro e cidade
        [
            sg.Input(key='bairro', size=(20, 1)),
            sg.Input(key='cidade', size=(17, 1)),
        ],

        # índice 4 - contatos
        [
            sg.Text('email:', size=(18, 1)),
            sg.Text('contato:', size=(17, 1)),

        ],

        # caixa 4 - contatos:
        [
            sg.Input('ntm@gmail.com', key='email', size=(20, 1)),
            sg.Input(key='contato', size=(17, 1)),
        ],


        # botões
        [
            sg.Button('Ok'),
            sg.Button('Cancelar'),
        ],
    ]

    return layout