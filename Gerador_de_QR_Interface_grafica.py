import PySimpleGUI as sg
import qrcode, pathlib, webbrowser

sg.theme('Reddit')   # Adicione um tema de sua preferência
# Conteúdo da janela.
layout = [  [sg.Image('image/app.png'), sg.Text('GERADOR DE QR CODE')],
            [sg.Text('Conte\u00fado para converter em QR CODE: '), sg.InputText(size=(33, 5))],
            [sg.Text('Nome da imagem a ser gerada. Ex.: "default.png": '), sg.InputText(size=(25, 1))],
            [sg.Text('Status:'), sg.Output(size=(60, 2))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
# Criação da janela
window = sg.Window('GERADOR DE QR CODE', layout, element_justification='center')
# Eventos e processamento de valores
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    conteudo = values[1]
    img = qrcode.make(conteudo)
    type(img)
    nome_arquivo = (values[2])
    if nome_arquivo == '':
        nome_arquivo = 'default.png'
    img.save(nome_arquivo)
    caminho = (pathlib.Path(__file__).parent.absolute())
    print(f'Arquivo {nome_arquivo.upper()} gerado com sucesso!!!') 
    webbrowser.open(f'{caminho}/{nome_arquivo}')

window.close()
