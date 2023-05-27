from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume 
from tkinter import messagebox as msb 
import tkinter as tk 
import keyboard as kb
import os

try :
    mensage_d = mensage_a = True
    loop = True
    
    def mensage_volume(volume):
        pass
        # falta colocar a msm de volume 
   
    def aumenta_volume():
        
        global mensage_a , mensage_d
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            current_volume = volume.GetMasterVolume()
            if current_volume < 1.0:
                new_volume = min(current_volume + 0.01, 1.0)
                volume.SetMasterVolume(new_volume, None)
                mensage_d = True
            else :
                if mensage_a :
                    msb.showinfo("AVISO !" , 'Volume Maximo Atingido !')
                    mensage_a = False
        volume = int(new_volume*100) 
        mensage_volume(volume)
            
            
    def diminui_volume():
        
        global mensage_d , mensage_a
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            current_volume = volume.GetMasterVolume()
            if current_volume > 0.0:
                new_volume = max(current_volume - 0.01, 0.0)
                volume.SetMasterVolume(new_volume, None)
                mensage_a = True
            else :
                if mensage_d :
                    msb.showinfo("AVISO !" , 'Volume Minimo Atingido !')  
                    mensage_d = False
                
                
    def atalhos(event):
        global loop
        if kb.is_pressed('alt') and kb.is_pressed('-'):
            diminui_volume()
        elif kb.is_pressed('alt') and (kb.is_pressed('=') or kb.is_pressed('+')):
            aumenta_volume()
        if kb.is_pressed('alt') and kb.is_pressed('p') :
            encerrar = msb.askyesno("ENCERRANDO !" , 'Deseja encerrar este aplicativo ?')
            if encerrar :
                os._exit(1)
            else :
                pass


    if __name__ == "__main__": 
        msb.showinfo('INICIANDO : ' , "Aparti de agora o Aplicativo estará em execução")
        msb.showwarning('COMANDOS :' , "Para alterar o volume use :\nAlt + '+' , para almentar\nAlt + '-' para , diminuir\nAlt + p , para encerrar ")
        kb.on_press(atalhos)
        kb.wait()

except IOError as erro:
    msb.showerror(title='Erro ao Executar ' , message=erro) 
