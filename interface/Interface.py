import PySimpleGUI as sg

class Interface():
    def __init__(self, controller):
        self.controller = controller
        
        self.janela_principal(controller.lista_bots)

    def janela_principal(self, bots):
        # janela_comandos(bots['Bot fitness'])
        nome_bots = list(bots.keys())
        layout = [
            [sg.Text("Ola, bem vindo ao sistema fit bot!")],
            [sg.Text('selecione um bot')],
            [sg.InputCombo(values=nome_bots, size=(20, 1), key='lista_suspensa')],
            [sg.Text('', size=(60, 1))],
            [sg.Button('Confirmar')],
        ]

        window = sg.Window('fit bot', layout,font=('Helvetica', 14))


        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Confirmar':
                selecionado = bots.get(values['lista_suspensa'])
                
                if selecionado:
                    self.editar_bot(selecionado)


    def editar_bot(self, bot):
        layout = [
            [sg.Text("Editar nome")],
            [sg.Text(bot.nome)],
            [sg.Text("Editar pergunta")],
            [sg.Text('selecione uma pergunta')],
            [sg.InputCombo(values=[cmd.mensagem for cmd in bot.comandos], size=(60, 1), key='-pergunta_selecionada-')],
            [sg.Button('Editar pergunta')],
            [sg.Button('Salvar')]
        ]

        window = sg.Window('editar bot', layout,font=('Helvetica', 14))

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Salvar':
                self.controller.salvar(bot)
                window.close()
            if event == 'Editar pergunta':
                pgt_selecionada = values['-pergunta_selecionada-']
                if pgt_selecionada:
                    index_sel = [i for i in range(len(bot.comandos)) if bot.comandos[i].mensagem == pgt_selecionada][0]
                    bot.comandos[index_sel] = self.editar_pergunta(bot.comandos[index_sel])
                    window['-pergunta_selecionada-'].update(values=[cmd.mensagem for cmd in bot.comandos])

    def editar_pergunta(self, comando):
        layout = [
            [sg.Text("Editar pergunta")],
            [sg.InputText(comando.mensagem, size=(60, 1), key='-mensagem-')],
            [sg.Text("Editar resposta")],
            [sg.Multiline(comando.respostas, size=(60, 3), key='-resposta-')],
            [sg.Button('Confirmar')]
        ]

        window = sg.Window('editar pergunta', layout,font=('Helvetica', 14))

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                return comando

            if event == 'Confirmar':
                window.close()
                comando.mensagem = values['-mensagem-']
                comando.respostas = values['-resposta-']
                return comando