from tkinter import messagebox as msb 
import shutil
import os
import sys
import pylnk3

def raiz():
    try: 
        # Obtém o caminho absoluto do arquivo Python atual
        script_path = os.path.abspath(sys.argv[0])

        # Define o diretório de destino na pasta de programas do Windows
        dest_dir = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs')

        # Copia o arquivo para o diretório de destino
        shutil.copy2(script_path, dest_dir)

        # Obtém o caminho absoluto do arquivo copiado
        dest_path = os.path.join(dest_dir, os.path.basename(script_path))

        # Cria um atalho para o arquivo copiado na pasta de programas do Windows
        shortcut_path = os.path.join(dest_dir, 'V-Audio.lnk')
        shortcut = pylnk3.create(dest_path, shortcut_path)
        shortcut.save()
    
    except OSError as erro:
        
        msb.showerror('ERRO !' , f'''
             Algo deu errado : {erro} . 
             \nCaso o erro persista , tire um print dessa mensagem e mande para nossa empresa .
             \nOBRIGADO PELA ATENÇÃO E DESCULPA PELO TRANSTORNO !     
            ''')
        
