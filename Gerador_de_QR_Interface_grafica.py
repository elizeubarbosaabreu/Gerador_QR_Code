#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import qrcode, pathlib, webbrowser

sg.theme('Reddit')   # Adicione um tema de sua preferência
# Conteúdo da janela

layout = [  [sg.Text('GERADOR DE QR CODE', font=('Arial 20'))],
            [sg.Text('Conte\u00fado para converter em QR CODE: '), sg.InputText(size=(33, 5), key='-conteudo-')],
            [sg.Text('Nome da imagem a ser gerada. Ex.: "default.png": '), sg.InputText(size=(25, 1), key='-nome_da_imagem-')],
            [sg.Text('Status:'), sg.Output(size=(60, 2))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Criação da janela
window = sg.Window('GERADOR DE QR CODE', layout, element_justification='center')

# Eventos e processamento de valores
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    
    conteudo = values['-conteudo-']
    img = qrcode.make(conteudo)
    type(img)
    nome_arquivo = (values['-nome_da_imagem-'])
    
    if nome_arquivo == '':
        nome_arquivo = 'default.png'
        
    img.save(nome_arquivo)
    caminho = (pathlib.Path(__file__).parent.absolute())
    print(f'Arquivo {nome_arquivo.upper()} gerado com sucesso!!!')
    print(values['-nome_da_imagem-'])
    webbrowser.open(f'{caminho}/{nome_arquivo}')

window.close()
