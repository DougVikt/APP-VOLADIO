from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import pymsgbox as pbx
import tkinter as tk


class VolumeControle :
    def __init__(self) -> None:
        
       
        self.mensage_d = True
        self.mensage_a = True
        self.volume_inicial = []
        self.sessions = AudioUtilities.GetAllSessions()

    # função para simplificar o uso do geometry 
    def __posicao(self, tamanho=[20, 20], alterar=[0, 0]):
        
        tela = self.janela
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

            

    def __mensage_volume(self , volume : float | str):
        
        self.janela = tk.Tk()
        tela = self.janela
        # Configurações da janela
        tela.attributes("-topmost", True)  # Mantém a janela sobre outros apps
        tela.overrideredirect(True)  # Remove as bordas da janela
        tela.configure(bg="white")  # Define o fundo da janela como branco

        # Cria um rótulo para exibir o volume na janela
        label = tk.Label(tela, text=f'Volume : {str(volume)}', font=("Arial", 16), bg="white")
        label.pack(padx=10, pady=10)

        # Define a posição da janela usando a função posicao
        self.__posicao([185, 55], [-15, 415])

        # Define um atraso de 200 milissegundos antes de destruir a janela
        tela.after(200, lambda: tela.destroy())

        # Inicia o loop principal da janela
        tela.mainloop()



    def aumenta_volume(self ,valor : float):

        try:            
            # Define o novo volume desejado como 1.0 (volume máximo)
            new_volume = 1.0
            
            # Itera sobre cada sessão de áudio
            for session in self.sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                current_volume = volume.GetMasterVolume()
                
                # Verifica se o volume atual é menor que 1.0
                if current_volume < 1.0:
                    # Incrementa o volume atual em 0.01, limitado a 1.0
                    new_volume = min(current_volume + valor, 1.0)
                    volume.SetMasterVolume(new_volume, None)
                    self.mensage_d = True
                else:
                    # Se o volume atual já for 1.0, exibe uma mensagem de aviso apenas uma vez
                    if self.mensage_a:
                        pbx.alert('Volume Máximo Atingido!', 'AVISO')
                        self.mensage_a = False
                        
            # Converte o novo volume para uma escala de 0 a 100
            volume = int(new_volume * 100) 
            
            # Exibe uma mensagem com o volume atual
            self.__mensage_volume(volume)
            
        except UnboundLocalError:
            pass

            
    def diminui_volume(self , valor :float):

        try:
           
            # Define o novo volume desejado como 0.0 (volume mínimo)
            new_volume = 0.0
            
            # Itera sobre cada sessão de áudio
            for session in self.sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                current_volume = volume.GetMasterVolume()
                
                # Verifica se o volume atual é maior que 0.0
                if current_volume > 0.0:
                    # Decrementa o volume atual em 0.01, limitado a 0.0
                    new_volume = max(current_volume - valor, 0.0)
                    volume.SetMasterVolume(new_volume, None)
                    self.mensage_a = True
                else:
                    # Se o volume atual já for 0.0, exibe uma mensagem de aviso apenas uma vez
                    if self.mensage_d:
                        pbx.alert('Volume Mínimo Atingido!', 'AVISO')
                        self.mensage_d = False
                        
            # Converte o novo volume para uma escala de 0 a 100
            volume = int(new_volume * 100) 
            
            # Exibe uma mensagem com o volume atual
            self.__mensage_volume(volume)
            
        except UnboundLocalError:
            pass

                    
                            
    def mudo_on_off(self):
        
        volume_atual = self.volume_inicial
        try:
            quant_session = 1
            for session in self.sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                quant_session += 1
                new_volume = volume.GetMasterVolume()
                
                # Insere o novo volume no início da lista volume_atual e volume_final
                volume_atual.insert(0, new_volume)
                volume_final = list(set(volume_atual))
                
                # Remove o último elemento da lista se houver mais que os elementos de som
                if len(volume_atual) > quant_session:
                    volume_atual.pop() 
                    
                # Verifica se o novo volume é diferente de 0.0
                if new_volume != 0.0:
                    # Define o volume como 0.0 (mudo)
                    volume.SetMasterVolume(0, None)
                    msm = True
                else:
                    # Restaura o volume anteriormente armazenado em volume_atual[2]
                    volume.SetMasterVolume(volume_final[1], None)
                    msm = False
                    
            if len(volume_final) < 2 :
                # Converte o volume atual para uma escala de 0 a 100
                volume_msm = int(volume_final[0] * 100)
            else :
                volume_msm = int(volume_final[1] * 100)
            
            if msm:
                # Exibe uma mensagem indicando que o áudio está mudo
                self.__mensage_volume('MUDO')
            else:
                # Exibe uma mensagem com o volume atual
                self.__mensage_volume(volume_msm)

        except UnboundLocalError:
            pass