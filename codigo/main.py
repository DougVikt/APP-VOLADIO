'''====== DESENVOLVIDO POR LORDDOUG ======='''
from tkinter import messagebox as msb 
from volume import VolumeControle as vc
from menu import JanelaPrincipal as jp
import keyboard as kb



try :
      
    def atalhos(event):
        
        # Verifica se a combinação de teclas Alt + - foi pressionada     
        if kb.is_pressed('alt') and kb.is_pressed('-'):    
            # Chama a função para diminuir o volume
            if kb.is_pressed('0') or kb.is_pressed('*'):
                # caso pressionado diminui de 5 em 5 
                tela_volume.diminui_volume(0.05)
            else:
                tela_volume.diminui_volume(0.01)
                
        # Verifica se a combinação de teclas Alt + = ou Alt + + foi pressionada
        elif kb.is_pressed('alt') and (kb.is_pressed('=') or kb.is_pressed('+')):
            # Chama a função para aumentar o volume
            if kb.is_pressed('0') or kb.is_pressed('*'):
                # caso pressionado aumenta de 5 em 5 
                tela_volume.aumenta_volume(0.05)
            else:
                tela_volume.aumenta_volume(0.01)
    
        # Verifica se a combinação de teclas Alt + m foi pressionada
        if kb.is_pressed('alt') and kb.is_pressed('m'):
            # Chama a função para alternar entre mudo e som
            tela_volume.mudo_on_off()
            
            
        # Verifica se a combinação de teclas Alt + z foi pressionada
        if kb.is_pressed('alt') and kb.is_pressed('z'):
            # Chama a função para exibir o menu
            iniciando()
        
       
            
    if __name__ == "__main__": 
  
        def iniciando():
            window = jp()
            if jp.exist :# inicia o menu
                window.menu() 
        
            window.janela.mainloop()
            
        tela_volume = vc()
        iniciando()
        
    
        # Monitora a pressão de teclas para atalhos
        kb.on_press(atalhos)
        
        # Aguarda o término da execução
        kb.wait()

except IOError as erro:
    # Exibe uma mensagem de erro caso ocorra um erro de E/S (Input/Output)
    msb.showerror('Erro ao Executar', erro)
