import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

ctk.CTkLabel(janela, text="Aula 11", font=("arial bold", 20)).pack(pady= 5, padx = 5)



entry = ctk.CTkEntry(janela, width=200, placeholder_text="Digite seu nome...", text_color="yellow", corner_radius= 20, border_width=5, placeholder_text_color="blue",state="normal")
entry.pack(pady = 50)
entry2 = ctk.CTkEntry(janela,width=200, placeholder_text="Digite seu nome...", text_color="yellow", corner_radius= 20, border_width=5, placeholder_text_color="blue",state="normal").pack(pady=10)

def enviar():
    print(entry.get())
    entry.delete(0, END)
    pass

ctk.CTkButton(janela, text="Enviar", width=200, command=enviar).pack(pady=24)

janela.mainloop()