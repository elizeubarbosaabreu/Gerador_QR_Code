import PySimpleGUI as sg
import qrcode
import pathlib
import webbrowser

sg.theme('SystemDefault')   # Adicione um tema de sua preferência
# All the stuff inside your window.
layout = [  [sg.Text('Digite o conteúdo para converter em QR CODE: '), sg.InputText()],
            [sg.Text('Digite o nome da imagem. Ex.: "default.png": '), sg.InputText()],
            [sg.Text('Status:'), sg.Output(size=(80, 1))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
# Create the Window
window = sg.Window('GERADOR DE QR CODE', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    conteudo = values[0]
    img = qrcode.make(conteudo)
    type(img)
    nome_arquivo = (values[1])
    if nome_arquivo == '':
        nome_arquivo = 'default.png'
    img.save(nome_arquivo)
    caminho = (pathlib.Path(__file__).parent.absolute())
    print(f'Arquivo "{nome_arquivo.upper()}" gerado com sucesso!!!') 
    webbrowser.open(f'{caminho}/{nome_arquivo}')

window.close()
