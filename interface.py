""" Usando Tkinter
from tkinter import * #importando
janela = Tk() #Criando a nossa janela principal
janela.mainloop() #Executando a janela"""

"""CustomTkinter"""
import customtkinter as ctk
janela = ctk.CTk() #cria a nossa janela
#janela._set_appearance_mode("light") #janela no modo branco
button = ctk.CTkButton(janela, text="Aperte aqui!")
button.pack()
janela.mainloop()