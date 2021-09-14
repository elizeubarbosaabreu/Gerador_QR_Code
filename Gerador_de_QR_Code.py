import qrcode
import pathlib
import webbrowser

print('{::^80}'.format('\033[7mGERADOR DE QR-CODE\033[m'))

conteudo = str(
    input(
        'Entre com o conteúdo, texto ou link que deseja converter em QR Code: '))
img = qrcode.make(conteudo)
type(img)
nome_arquivo = str(
    input(
        'Que nome você quer dar para o arquivo. Digite o nome com a extensão: ex.: qrcode.png: '))

img.save(nome_arquivo)
caminho = (pathlib.Path(__file__).parent.absolute())
print(f'Arquivo {nome_arquivo} gerado com sucesso!!!') 
webbrowser.open(f'{caminho}/{nome_arquivo}')
