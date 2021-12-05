import PySimpleGUI as sg
import qrcode
from time import sleep

#   ___  ____     ____          _      
#  / _ \|  _ \   / ___|___   __| | ___ 
# | | | | |_) | | |   / _ \ / _` |/ _ \
# | |_| |  _ <  | |__| (_) | (_| |  __/
#  \__\_\_| \_\  \____\___/ \__,_|\___|
#                                      
#   ____                           _             
#  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
#  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
#                                                


sg.theme('Reddit')

layout = [[sg.Text('Digite ou cole o link ou texto para converter em QR CODE')],
          [sg.InputText(size=(60, 2), key='-conteudo-'),
           sg.Button('Gerar QR', size=(15, 2))],
          [sg.Output(size=(80, 4), font=('Courier New', 9), key='-output-')],
          [sg.Stretch(), sg.Image(key='-img-') ,sg.Stretch()]
          ]

# Criação da janela
window = sg.Window('GERADOR DE QR CODE', layout)

# Eventos e processamento de valores
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED: 
        break
    
    if event in ('Gerar QR'):
    
        conteudo = values['-conteudo-']    
        img = qrcode.make(conteudo)
        type(img)

        nome_arquivo = sg.popup_get_file('Escolha Onde quer Guardar seu QR CODE',
                                       title='Salvar Arquivo',
                                       file_types=(("PNG","*.png"),("Outras","*.*"),),
                                       save_as = True,)
        
        if nome_arquivo == '':
            nome_arquivo = 'default.png'
            
        img.save(nome_arquivo)                             
                                
        print(f'Convertendo {conteudo} em qr code...')
        sleep(0.3)
        print(f'Estamos gerando seu arquivo de imagem...')
        sleep(0.3)
        print(f'Arquivo {nome_arquivo} gerado com sucesso!!!')
        sleep(1)
           
        window['-img-'].update(nome_arquivo)

window.close()
