'''====== DESENVOLVIDO POR LORDDOUG ======='''
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
    
    # função para simplificar o uso do geometry 
    def posicao(tela, tamanho=[20, 20], alterar=[0, 0]):
        # Obtém a altura da tela
        tela_vert = tela.winfo_screenheight()
        
        # Obtém a largura da tela
        tela_hori = tela.winfo_screenwidth()
        
        # Calcula a posição x da janela para centralizá-la na tela
        posi_x = ((tela_hori - tamanho[0]) // 2) + alterar[0]
        
        # Calcula a posição y da janela para centralizá-la na tela
        posi_y = ((tela_vert - tamanho[1]) // 2) + alterar[1]
        
        # Define a geometria da janela com o tamanho e posição calculados
        return tela.geometry(f'{tamanho[0]}x{tamanho[1]}+{posi_x}+{posi_y}')
 
        
    
    def menu():
        
                
        # Cria uma nova janela usando a classe Tk do módulo tkinter
        janela = tk.Tk()

        # Coloca o icone na janela
        #janela.iconbitmap('v-audio.png')
        
        # Define a janela como a janela de maior prioridade, ou seja, será exibida acima de outras janelas
        janela.attributes('-topmost', True)

        # Define o título da janela como 'V-Audio'
        janela.title('V-Audio')

        # Configura o fundo da janela com a cor 'dodger blue'
        janela.configure(bg='DeepSkyBlue3' , bd= 15 , relief= 'ridge' )

        # Posiciona a janela no centro da tela usando a função 'posicao' e define o tamanho como [240, 300]
        posicao(janela, [240, 340])

        def msn_instrucao():
           
            # exibe a mensagem das instrções     
            msb.showinfo('INSTRUÇÕES :' , 
                        '''Para execução correta da aplicação leia os comandos .
            \nPor favor não excluir o atalho do app , em caso de fechamento o atalho e a opção para abrir o app novamente .  
            \nPara sair do menu aperte no botão ESCONDER ou no 'X', assim o app ficara em execução em segundo plano .
            \nPara fechar o app , so clicando no botão SAIR no menu .
            \nPara desinstalar o app use o botão DESINSTALAR no menu , assim não dexará resto de arquivos no seu computador .''' )
            
            
        def msn_comando():
            
            # Exibe a mensagem dos comandos usados 
            msb.showwarning('COMANDOS :' , '''Alt + ' + ' , para Almentar
                                        \nAlt + ' - ' , para Diminuir
                                        \nAlt + m  , para o Mudo
                                        \nAlt + z , para acessar o menu''')
            
        def comd_escond():
            
            # Destroy a janela do Tkinter
            janela.destroy()
            
        
        def comd_sair():
            
            # Exibe uma mensagem que tem 'yes' ou 'no' 
            resposta = msb.askyesno('FECHAR ?' , 'Quer fechar a aplicação ?')
            
            # Se a resposta for 'yes'
            if resposta :
                
                # Manda uma mensagem de despedida
                pbx.alert('Ate a proxima !', 'AVISO')
                # Fecha o programa
                os._exit(1)
                
        
        def comd_desi():
            
            # Exibe a mensagem de decisão 
            desins = msb.askyesno('DESINSTALAR ?' , 'Tem certeza que quer desinstalar o V-Audio ?')
            # Se a resposta for 'ok'
            if desins :
                # Executa a fução de desinstalação
                ic.desinstalar()
            
        
        # Todos são botões do menu 
        bt_instru = tk.Button(janela , text='INSTRUÇÕES' , command=msn_instrucao , width=20 , height=2 , bg='SpringGreen3')
        bt_instru.pack(padx=10 , pady=10 )
        
        bt_comando = tk.Button(janela , text='COMANDOS' , command=msn_comando , width=20 , height=2 , bg='SpringGreen3')
        bt_comando.pack(padx=10 , pady=10 )
        
        bt_susp = tk.Button(janela , text='ESCONDER' , command=comd_escond , width=15 , height=1 , bg='SpringGreen3')
        bt_susp.pack(padx=10 , pady=15)
        
        bt_sair = tk.Button(janela , text='SAIR' , command=comd_sair , width=7 , height=1 , bg='gold')
        bt_sair.pack(padx=10 , pady=30 )
        
        bt_des = tk.Button(janela , text='DESINSTALAR' , command=comd_desi , width=10 , height=1 ,bg='red2')
        bt_des.pack(padx=10 , pady=8 )
        
        # Loop do Tkinter 
        janela.mainloop()
        
        
        
    def mensage_volume(volume):
        # Cria uma nova janela
        janela = tk.Tk()
        
        # Variável para exibir o volume na janela
        volume_var = tk.StringVar()
        
        # Configurações da janela
        janela.attributes("-topmost", True)  # Mantém a janela sobre outros apps
        janela.overrideredirect(True)  # Remove as bordas da janela
        janela.configure(bg="white")  # Define o fundo da janela como branco
        
        # Define o valor da variável de exibição do volume
        volume_var.set(f'Volume : {volume}')
        
        # Cria um rótulo para exibir o volume na janela
        label = tk.Label(janela, textvariable=volume_var, font=("Arial", 16), bg="white")
        label.pack(padx=10, pady=10)
        
        # Define a posição da janela usando a função posicao
        posicao(janela, [185, 55], [-15, 415])
        
        # Define um atraso de 200 milissegundos antes de destruir a janela
        janela.after(200, lambda: janela.destroy())
        
        # Inicia o loop principal da janela
        janela.mainloop()
        
        

    def aumenta_volume():
        # Variáveis globais
        global mensage_a, mensage_d
        
        try:
            # Obtém todas as sessões de áudio ativas
            sessions = AudioUtilities.GetAllSessions()
            
            # Define o novo volume desejado como 1.0 (volume máximo)
            new_volume = 1.0
            
            # Itera sobre cada sessão de áudio
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                current_volume = volume.GetMasterVolume()
                
                # Verifica se o volume atual é menor que 1.0
                if current_volume < 1.0:
                    # Incrementa o volume atual em 0.01, limitado a 1.0
                    new_volume = min(current_volume + 0.01, 1.0)
                    volume.SetMasterVolume(new_volume, None)
                    mensage_d = True
                else:
                    # Se o volume atual já for 1.0, exibe uma mensagem de aviso apenas uma vez
                    if mensage_a:
                        pbx.alert('Volume Máximo Atingido!', 'AVISO')
                        mensage_a = False
                        
            # Converte o novo volume para uma escala de 0 a 100
            volume = int(new_volume * 100) 
            
            # Exibe uma mensagem com o volume atual
            mensage_volume(volume)
            
        except UnboundLocalError:
            pass

            
    def diminui_volume():
        # Variáveis globais
        global mensage_d, mensage_a
        
        try:
            # Obtém todas as sessões de áudio ativas
            sessions = AudioUtilities.GetAllSessions()
            
            # Define o novo volume desejado como 0.0 (volume mínimo)
            new_volume = 0.0
            
            # Itera sobre cada sessão de áudio
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                current_volume = volume.GetMasterVolume()
                
                # Verifica se o volume atual é maior que 0.0
                if current_volume > 0.0:
                    # Decrementa o volume atual em 0.01, limitado a 0.0
                    new_volume = max(current_volume - 0.01, 0.0)
                    volume.SetMasterVolume(new_volume, None)
                    mensage_a = True
                else:
                    # Se o volume atual já for 0.0, exibe uma mensagem de aviso apenas uma vez
                    if mensage_d:
                        pbx.alert('Volume Mínimo Atingido!', 'AVISO')
                        mensage_d = False
                        
            # Converte o novo volume para uma escala de 0 a 100
            volume = int(new_volume * 100) 
            
            # Exibe uma mensagem com o volume atual
            mensage_volume(volume)
            
        except UnboundLocalError:
            pass

                   
                   
                   
    def mudo_on_off():
        # Variável global
        global volume_atual 
        
        try:
            # Obtém todas as sessões de áudio ativas
            sessions = AudioUtilities.GetAllSessions()
            
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                new_volume = volume.GetMasterVolume()
                
                # Insere o novo volume no início da lista volume_atual
                volume_atual.insert(0, new_volume)
                
                # Remove o último elemento da lista se houver mais de 3 elementos
                if len(volume_atual) > 3:
                    volume_atual.pop() 
                    
                # Verifica se o novo volume é diferente de 0.0
                if new_volume != 0.0:
                    # Define o volume como 0.0 (mudo)
                    volume.SetMasterVolume(0, None)
                    msm = True
                else:
                    # Restaura o volume anteriormente armazenado em volume_atual[2]
                    volume.SetMasterVolume(volume_atual[2], None)
                    msm = False
            
            # Converte o volume atual para uma escala de 0 a 100
            volume_msm = int(volume_atual[2] * 100)
            
            if msm:
                # Exibe uma mensagem indicando que o áudio está mudo
                mensage_volume('MUDO')
            else:
                # Exibe uma mensagem com o volume atual
                mensage_volume(volume_msm)
        
        except UnboundLocalError:
            pass

        
                
    def atalhos(event):
        # Variável global
        global loop
        
        # Verifica se a combinação de teclas Alt + - foi pressionada
        if kb.is_pressed('alt') and kb.is_pressed('-'):
            # Chama a função para diminuir o volume
            diminui_volume()
        
        # Verifica se a combinação de teclas Alt + = ou Alt + + foi pressionada
        elif kb.is_pressed('alt') and (kb.is_pressed('=') or kb.is_pressed('+')):
            # Chama a função para aumentar o volume
            aumenta_volume()
        
        # Verifica se a combinação de teclas Alt + m foi pressionada
        elif kb.is_pressed('alt') and kb.is_pressed('m'):
            # Chama a função para alternar entre mudo e som
            mudo_on_off()
        
        # Verifica se a combinação de teclas Alt + z foi pressionada
        if kb.is_pressed('alt') and kb.is_pressed('z'):
            # Chama a função para exibir o menu
            menu()


    if __name__ == "__main__": 
        # Instala o programa
        ic.instalar()
        
        # Exibe o menu
        menu()
        
        # Monitora a pressão de teclas para atalhos
        kb.on_press(atalhos)
        
        # Aguarda o término da execução
        kb.wait()

except IOError as erro:
    # Exibe uma mensagem de erro caso ocorra um erro de E/S (Input/Output)
    msb.showerror('Erro ao Executar', erro)
