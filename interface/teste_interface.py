import PySimpleGUI as sg

lista = ['valor 1', 'valor 2', 'valor 3', 'valor 4'] # Sua lista de valores

def janela_principal():
    layout = [
        [sg.Text("Ola, bem vindo ao sistema fit bot!")],
        [sg.Text('selecione um bot')],
        [sg.InputCombo(values=lista, size=(20, 1), key='lista_suspensa')],
        [sg.Text('', size=(60, 1))],
        [sg.Button('Confirmar')],

    ]

    window = sg.Window('Principal', layout,font=('Helvetica', 14))


    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Confirmar':
            window.close()
            janela_comandos()


def janela_comandos():
    layout = [
        [sg.Text('Escolha a sua pergunta')],
        [sg.Button('pergunta 1')],
        [sg.Button('pergunta 2')],
        [sg.Text('Resposta: '), sg.Text('', key='resposta', size=(50,1))]
    ]

    window = sg.Window('Bot', layout)
    event, values = window.read()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'pergunta 1':
            window.Element('resposta').update('voce fez a pergunta 1')


janela_principal()
