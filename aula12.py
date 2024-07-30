import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 12", font=("arial bold", 20)).pack(pady= 5)

def nova_janela():
    imagem = ctk.CTkImage(Image.open("c:\\Users\\Usuário\\Downloads\\carta_natal.png"), size=(1053, 421))
    nova_tela = ctk.CTkToplevel()
    nova_tela.geometry("1000x500")
    nova_tela.attributes("-topmost", True)
    nova_tela.title("Olááááá")
    label_imagem = ctk.CTkLabel(nova_tela, text="", image=imagem)
    label_imagem.pack(pady=100)
    pass

ctk.CTkButton(janela, width= 200, text="Clique aqui!!", command = nova_janela).pack(pady=20)

janela.mainloop()