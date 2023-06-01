
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume 
from tkinter import messagebox as msb 
import inicializar as ic
import keyboard as kb
import tkinter as tk
import pymsgbox as pbx
import os

try :
    # variaveis globais
    mensage_d = mensage_a = True
    loop = True
    volume_atual = []
    
    def posicao(tela , tamanho=[20 , 20] , alterar= [0 , 0]):
                
        tela_vert = tela.winfo_screenheight()
        tela_hori = tela.winfo_screenwidth()
        posi_x = (( tela_hori - tamanho[0])//2) + alterar[0]
        posi_y = (( tela_vert - tamanho[1])//2) + alterar[1]
        return tela.geometry(f'{tamanho[0]}x{tamanho[1]}+{posi_x}+{posi_y}')     
        
    
    def menu():
        
        
        janela = tk.Tk()
        janela.attributes('-topmost' , True)
        janela.title('V-Audio')
        janela.configure(bg='dodger blue')
        posicao(janela , [240,300])
        
     
            
        def msn_instrucao():
            
            msb.showinfo('INSTRUÇÕES :' , 
                        '''Para execução correta da aplicação leia os comandos .
            \nPor favor não excluir o atalho do app , em caso de fechamento o atalho e a opção para abrir o app novamente .  
            \nPara sair do menu aperte no botão ESCONDER ou no 'X', assim o app ficara em execução em segundo plano .
            \nPara fechar o app , so clicando no botão SAIR no menu .
            \nPara desinstalar o app use o botão DESINSTALAR no menu , assim não dexará resto de arquivos no seu computador .''')
            
            
        def msn_comando():
        
            msb.showwarning('COMANDOS :' , '''Alt + ' + ' , para Almentar
                                        \nAlt + ' - ' , para Diminuir
                                        \nAlt + m  , para o Mudo
                                        \nAlt + z , para acessar o menu''')
            
        def comd_escond():
            janela.destroy()
            
        
        def comd_sair():
            
            resposta = msb.askyesno('FECHAR ?' , 'Quer fechar a aplicação ?')
            if resposta :
                pbx.alert('Ate a proxima !', 'AVISO')
                os._exit(1)
                
        
        def comd_desi():
            desins = msb.askokcancel('DESINSTALAR ?' , 'Tem certeza que quer desinstalar o V-Audio ?')
            if desins :
                ic.desinstalar()
            
        
        bt_instru = tk.Button(janela , text='INSTRUÇÕES' , command=msn_instrucao , width=20 , height=2)
        bt_instru.pack(padx=10 , pady=10 )
        
        bt_comando = tk.Button(janela , text='COMANDOS' , command=msn_comando , width=20 , height=2)
        bt_comando.pack(padx=10 , pady=10 )
        
        bt_susp = tk.Button(janela , text='ESCONDER' , command=comd_escond , width=15 , height=1)
        bt_susp.pack(padx=10 , pady=15)
        
        bt_sair = tk.Button(janela , text='SAIR' , command=comd_sair , width=7 , height=1 , bg='gold')
        bt_sair.pack(padx=10 , pady=30 )
        
        bt_des = tk.Button(janela , text='DESINSTALAR' , command=comd_desi , width=10 , height=1 ,bg='red2')
        bt_des.pack(padx=10 , pady=8 )
        
        janela.mainloop()
        
        
        
    def mensage_volume(volume):
        
        janela = tk.Tk()
        volume_var = tk.StringVar()
        janela.attributes("-topmost", True)
        janela.overrideredirect(True)
        janela.configure(bg="white")
        volume_var.set(f'Volume : {volume}')
        
        label = tk.Label(janela, textvariable=volume_var, font=("Arial", 16), bg="white")
        label.pack(padx=10 , pady=10)
        
        posicao(janela , [185,55], [-15 , 415])
        janela.after( 200, lambda: janela.destroy())
        
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
                
                volume_atual.insert(0 ,new_volume)
                if len(volume_atual) > 3 :
                    volume_atual.pop() 
                    
                if new_volume != 0.0 :
                    volume.SetMasterVolume(0 , None)
                    msm = True
                else :
                    volume.SetMasterVolume(volume_atual[2] , None)
                    msm = False
            
            volume_msm = int(volume_atual[2] * 100)
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
        if kb.is_pressed('alt') and kb.is_pressed('z') :
            menu()


    if __name__ == "__main__": 
        ic.instalar()
        menu()
        kb.on_press(atalhos)
        kb.wait()

except IOError as erro:
    msb.showerror('Erro ao Executar ' , erro) 
