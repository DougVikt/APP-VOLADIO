from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume 
from tkinter import messagebox as msb 
import keyboard as kb
import tkinter as tk
import pymsgbox as pbx
import os

try :
    mensage_d = mensage_a = True
    loop = True
    volume_atual = []
    
    def posicao(tela , tamanho=[20 , 20] , alterar= [0 , 0]):
                
        tela_vert = tela.winfo_screenheight()
        tela_hori = tela.winfo_screenwidth()
        posi_x = (( tela_hori - tamanho[0])//2) + alterar[0]
        posi_y = (( tela_vert - tamanho[1])//2) + alterar[1]
        print(posi_x , posi_y)
        return tela.geometry(f'{tamanho[0]}x{tamanho[1]}+{posi_x}+{posi_y}')     
        
    
    def menu():
        janela = tk.Tk()
        janela.attributes('-topmost' , True)
        
    
    def mensage_volume(volume):
        
        janela = tk.Tk()
        janela.attributes("-topmost", True)
        janela.overrideredirect(True)
        janela.configure(bg="white")
        
        
        label = tk.Label(janela, text='Volume : ' + str(volume), font=("Arial", 16), bg="white")
        label.pack(padx=10 , pady=10)
        
        posicao(janela , [185,55], [-15 , 415])
        janela.after( 100, lambda: janela.destroy())
        
        janela.mainloop()      
        
   
   
    def aumenta_volume():
        
        global mensage_a , mensage_d
        try :
            sessions = AudioUtilities.GetAllSessions()
            new_volume = 1.0
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                current_volume = volume.GetMasterVolume()
                if current_volume < 1.0:
                    new_volume = min(current_volume + 0.01, 1.0)
                    volume.SetMasterVolume(new_volume, None)
                    mensage_d = True
                else :
                    if mensage_a :
                        pbx.alert('Volume Máximo Atingido!', 'AVISO')
                        mensage_a = False
            volume = int(new_volume*100) 
            mensage_volume(volume)
        except UnboundLocalError :
            pass
        
            
    def diminui_volume():
        
        global mensage_d , mensage_a
        try : 
            sessions = AudioUtilities.GetAllSessions()
            new_volume = 0.0
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                current_volume = volume.GetMasterVolume()
                if current_volume > 0.0:
                    new_volume = max(current_volume - 0.01, 0.0)
                    volume.SetMasterVolume(new_volume, None)
                    mensage_a = True
                else :
                    if mensage_d :
                        pbx.alert('Volume Minimo Atingido!', 'AVISO')
                        mensage_d = False
            volume = int(new_volume*100) 
            mensage_volume(volume)                
        except UnboundLocalError:
            pass
                   
    def mudo_on_off() :
        
        global volume_atual 
        try :
            
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions :
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                new_volume = volume.GetMasterVolume()
                volume_atual.append(new_volume)
                if len(volume_atual) > 3 :
                    volume_atual.pop()
                    
                if new_volume != 0.0 :
                    volume.SetMasterVolume(0 , None)
                    msm = True
                else :
                    volume.SetMasterVolume(volume_atual[0] , None)
                    msm = False
            
            volume_msm = int(volume_atual[0] * 100)
            if msm :
                mensage_volume('MUDO')
            else :
                mensage_volume(volume_msm)
           
        except UnboundLocalError :
            pass
        
                
    def atalhos(event):
        global loop
        if kb.is_pressed('alt') and kb.is_pressed('-'):
            diminui_volume()
        elif kb.is_pressed('alt') and (kb.is_pressed('=') or kb.is_pressed('+')):
            aumenta_volume()
        elif kb.is_pressed('alt') and kb.is_pressed('m') :
            mudo_on_off()
        if kb.is_pressed('alt') and kb.is_pressed('p') :
            encerrar = msb.askyesno("ENCERRANDO !" , 'Deseja encerrar este aplicativo ?')
            if encerrar :
                os._exit(1)
            else :
                pass


    if __name__ == "__main__": 
        msb.showinfo('INICIANDO : ' , "Aparti de agora o Aplicativo estará em execução")
        msb.showwarning('COMANDOS :' , '''Para alterar o volume use :
                                        \nAlt + '+' , para Almentar
                                        \nAlt + '-' , para Diminuir
                                        \nAlt + m  , para o Mudo
                                        \nAlt + p , para encerrar ''')
        kb.on_press(atalhos)
        kb.wait()

except IOError as erro:
    msb.showerror(title='Erro ao Executar ' , message=erro) 
