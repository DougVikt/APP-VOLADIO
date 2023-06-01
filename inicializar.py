from tkinter import messagebox as msb 
import shutil
import os
import sys
import pylnk3

def instalar1():
    try: 
        # Obtém o caminho absoluto do arquivo Python atual
        caminho = os.path.abspath(sys.argv[0])

        # Define o diretório de destino na pasta de programas do Windows
        pasta_atalho = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')
        # Obter o diretório da área de trabalho
        desktop_pasta = os.path.expanduser("~\\Desktop")
        
        # Copia o arquivo para o diretório de destino
        shutil.copy2(caminho, pasta_atalho)

        # Obtém o caminho absoluto do arquivo copiado
        pasta_raiz = os.path.join(pasta_atalho, os.path.basename(caminho))

        # Cria um atalho para o arquivo copiado na pasta de programas do Windows
        shortcut_pasta = os.path.join(pasta_atalho, 'V-Audio.lnk')
        shortcut = pylnk3.create(pasta_raiz, shortcut_pasta)
        shortcut.save()
        
        # Criar o caminho completo para o atalho na área de trabalho
        shortcut_pasta2 = os.path.join(desktop_pasta, 'V-Audio.lnk')
        shortcut = pylnk3.create(pasta_raiz, shortcut_pasta2)
        shortcut.save()
    
    except OSError as erro:
        
        msb.showerror('ERRO !' , f'''
             Algo deu errado : {erro} . 
             \nCaso o erro persista , tire um print dessa mensagem e mande para nossa empresa .
             \nOBRIGADO PELA ATENÇÃO E DESCULPA PELO TRANSTORNO !     
            ''')
        

def desinstalar1():
     
    # Define o diretório de destino na pasta de programas do Windows
    pasta_atalho = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')
     # Obter o diretório da área de trabalho
    desktop_pasta = os.path.expanduser("~\\Desktop")
        
    # Remove o atalho
    shortcut_raiz = os.path.join(pasta_atalho, 'V-Audio.lnk')
    os.remove(shortcut_raiz)
    try :
        # em caso de não achar o atalho na pasta 
        shortcut_desk = os.path.join(desktop_pasta, 'V-Audio.lnk')
        os.remove(shortcut_desk)
    except FileExistsError :
        pass

    # Obtém o caminho absoluto do arquivo atual
    caminho = os.path.abspath(__file__)

    # Remove a cópia do arquivo na pasta de destino
    pasta_raiz = os.path.join(pasta_atalho, os.path.basename(caminho))
    os.remove(pasta_raiz)


def instalar():
    pass

def desinstalar():
    pass