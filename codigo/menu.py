from tkinter import messagebox as msb 
from PIL import Image , ImageTk
import tkinter as tk
import pymsgbox as pbx
import sys
import os

class JanelaPrincipal:
    
    def __init__(self) -> None:
        
        self.janela = tk.Tk()
        self.inicio = True
        # Atribuindo o nome na janela
        self.janela.title('V-Audio')
        
        
    def menu(self):
        
        # Defina o ícone da janela
        #self.janela.iconbitmap(self.__image_caminho('va.ico'))
        
        #Define a imagem de fundo
        #self.__image_fundo(self.janela)
        
        # Configura o fundo da janela com a cor 'dodger blue'
        self.janela.configure(bg='DeepSkyBlue3' , bd= 15 , relief= 'ridge' )

        # Posiciona a janela no centro da tela usando a função 'posicao' e define o tamanho como [240, 300]
        self.__posicao([240, 340])
        
        self.__botoes()
        
        self.janela.mainloop()
        
        
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
        tela.geometry(f'{tamanho[0]}x{tamanho[1]}+{posi_x}+{posi_y}')
    
    
    def __botoes(self):
        tela = self.janela
        # Todos são botões do menu 
        botao_instru = tk.Button(tela , text='INSTRUÇÕES' , command=self.__menssage_instrucao , width=20 , height=2 , bg='SpringGreen3')
        botao_instru.pack(padx=10 , pady=10 )
        
        botao_comando = tk.Button(tela , text='COMANDOS' , command=self.__menssage_comando , width=20 , height=2 , bg='SpringGreen3')
        botao_comando.pack(padx=10 , pady=10 )
        
        botao_sair = tk.Button(tela , text='SAIR' , command=self.__fechar_app , width=7 , height=1 , bg='gold')
        botao_sair.pack(padx=10 , pady=30 )
        
        # Dicionando a versão 
        versao = tk.Label(tela, text='Versão 1.5' , background='DeepSkyBlue3')
        versao.pack(padx=10 , side='bottom' ,pady=10)
        
        # Loop do Tkinter 
        tela.mainloop()
        
    
    def exist(self):  
        if self.janela.winfo_exists() :
            self.inicio = False
        return self.inicio
            
    
    def __menssage_instrucao(self):
        
        # exibe a mensagem das instrções , para melhor visualização tive que dixar desse jeito      
        msb.showinfo('INSTRUÇÕES :' , 
                    '''Para execução correta da aplicação leia os comandos .
        \nAntes do primeiro uso dos altalhos de aumentar e diminuir o volume , use o atalho de MUDO para igualhar os volumes dos apps , e ao repetir o mesmo atalho o volume voltara ao de antes e configurado .
        \nSuas funções so entram em vigor quando o menu estiver fechado . 
        \nAs teclas de atalho para aumentar/diminuir em 5 e o '0 ou )' do teclado principal e o '*' do teclado numerico . 
        \nPor favor não excluir o atalho do app , em caso de fechamento o atalho e a opção para abrir o app novamente .  
        \nPara sair do menu aperte no 'X', assim o app ficara em execução em segundo plano .
        \nPara fechar o app , clique no botão SAIR no menu .''')
        
        
    def __menssage_comando(self):
        
        # Exibe a mensagem dos comandos usados 
        msb.showwarning('COMANDOS :' , '''Alt + ' + ' , para Almentar em 1
                                    \nAlt + ' - ' , para Diminuir em 1
                                    \nAlt + ' + ' + ' ) ' ou ' * ' , para Aumentar em 5 
                                    \nAlt + ' - ' + ' ) ' ou ' * ' , para Diminuir em 5
                                    \nAlt + m  , para o Mudo
                                    \nAlt + z , para acessar o menu''')
        

    def __fechar_app(self):
        
        # Exibe uma mensagem que tem 'yes' ou 'no' 
        resposta = msb.askyesno('FECHAR ?' , 'Quer fechar a aplicação ?')
        
        # Se a resposta for 'yes'
        if resposta :
            
            # Manda uma mensagem de despedida
            pbx.alert('Ate a proxima !', 'AVISO')
            # Fecha o programa
            os._exit(1)
            
    
    def __image_caminho(self , nome_imagem:str):
        # Obtenha o caminho absoluto do diretório do script em execução
        caminho = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Caminho absoluto do arquivo de ícone
        imagem_pasta = os.path.join(caminho, nome_imagem) 
    
        return imagem_pasta
        
    
    def __image_fundo(self):
        
        tela = self.janela
        # Carregar a imagem
        imagem = Image.open(self.__image_caminho(''))

        # Redimensionar a imagem para se ajustar à janela
        largura = tela.winfo_width()
        altura = tela.winfo_height()
        imagem_ajustada = imagem.resize((largura, altura), Image.ANTIALIAS)

        # Converter a imagem para o formato suportado pelo tkinter
        imagem_tk = ImageTk.PhotoImage(imagem_ajustada)

        # Criar um widget de tela de fundo
        canvas = tk.Canvas(tela, width=largura, height=altura)
        canvas.pack()

        # Exibir a imagem no widget de tela de fundo
        canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk)
