import PySimpleGUI as sg


def janela_principal():
    layout = [
        [sg.Text("Ola, bem vindo ao sistema fit bot!")],
        [sg.Text('escolha o bot')],
        [sg.Multiline(default_text='bot 1')],
        [sg.Combo(values=['Bot 1', 'Bot 2'])],
        [sg.Text('', size=(60, 1))],
        [sg.Text('Digite o bot escolhido: '), sg.InputText('', key='bot'), sg.Button('Confirmar')],
        [sg.Text('', size=(60, 1))]
    ]

    window = sg.Window('Principal', layout,font=('Helvetica', 14))


    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Bot 2' or 'Bot 1':
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
