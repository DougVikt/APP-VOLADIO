import tkinter as tk
from tkinter import messagebox as msb 
import pymsgbox as pbx

def posicao(tela , tamanho=[int] , alterar= [0 , 0]):
                    
        tela_vert = tela.winfo_screenheight()
        tela_hori = tela.winfo_screenwidth()
        posi_x = (( tela_hori - tamanho[0])//2) + alterar[0]
        posi_y = (( tela_vert - tamanho[1])//2) + alterar[1]
        print(posi_x , posi_y)
        return tela.geometry(f'{tamanho[0]}x{tamanho[1]}+{posi_x}+{posi_y}')     
    
        
def menu():
    
    janela = tk.Tk()
    janela.attributes('-topmost' , True)
    janela.title('V-Audio')
    janela.configure(bg='dodger blue')
    posicao(janela , [240,260])
    
    def msn_instrucao():
        
        msb.showinfo('INSTRUÇÕES :' , 
                     '''Para execução correta da aplicação leia os comandos . 
        \nPara sair do menu aperte no botão ESCONDER , assim o app ficara em execução em segundo plano , mas se apertar no 'X' , a aplicação sera fechada .
        \nPara fechar o app pode se pelo 'X' ou clicando no botão SAIR ambos no menu .''')
        
        
    def msn_comando():
    
        msb.showwarning('COMANDOS :' , '''Alt + ' + ' , para Almentar
                                    \nAlt + ' - ' , para Diminuir
                                    \nAlt + m  , para o Mudo
                                    \nAlt + n , para acessar o menu''')
        
    def comd_escond():
        janela.withdraw()
    
    def comd_sair():
        
        resposta = msb.askyesno('FECHAR ?' , 'Quer fechar a aplicação ?')
        if resposta :
            pbx.alert('Ate a proxima !', 'AVISO')
            janela.destroy()
        
        
    
    bt_instru = tk.Button(janela , text='INSTRUÇÕES' , command=msn_instrucao , width=20 , height=2)
    bt_instru.pack(padx=10 , pady=10 )
    
    bt_comando = tk.Button(janela , text='COMANDOS' , command=msn_comando , width=20 , height=2)
    bt_comando.pack(padx=10 , pady=10 )
    
    bt_susp = tk.Button(janela , text='ESCONDER' , command=comd_escond , width=15 , height=1)
    bt_susp.pack(padx=10 , pady=15)
    
    bt_sair = tk.Button(janela , text='SAIR' , command=comd_sair , width=7 , height=1)
    bt_sair.pack(padx=10 , pady=30 )
    
    janela.mainloop()
    
        

menu()
