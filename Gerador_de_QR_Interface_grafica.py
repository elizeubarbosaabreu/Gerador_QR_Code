#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import qrcode, webbrowser
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

layout = [  [sg.Stretch(), sg.Text('GERADOR DE QR CODE', font=('Arial 20')), sg.Stretch()],
            [sg.HorizontalSeparator()],
            [sg.Text('LINK/TEXTO PARA QR CODE', size=(30, 1)), sg.InputText(size=(50, 1), key='-conteudo-')],
            [sg.Text('NOME DA IMAGEM: OPCIONAL', size=(30, 1)), sg.InputText(size=(42, 1), key='-nome_da_imagem-'), sg.Button('Ok')],
            [sg.HorizontalSeparator()],
            [sg.Output(size=(80, 4), font=('Courier New', 9), key='-output-')]
            ]

# Cria\u00e7\u00e3o da janela
window = sg.Window('GERADOR DE QR CODE', layout)

# Eventos e processamento de valores
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    conteudo = values['-conteudo-']    
    img = qrcode.make(conteudo)
    type(img)
    nome_arquivo = (values['-nome_da_imagem-'])
    
    if nome_arquivo == '':
        nome_arquivo = 'default.png'
        
    img.save(nome_arquivo)                             
                            
    print(f'Convertendo {conteudo} em qr code...')
    sleep(1)
    print(f'Estamos gerando seu arquivo de imagem...')
    sleep(1)
    print(f'Arquivo {nome_arquivo} gerado com sucesso!!!')
    sleep(1)
    print(f'Vou abrir o qr code gerado em seu navegador...')
    sleep(1)    
    webbrowser.open(f'{nome_arquivo}')

window.close()
