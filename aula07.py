import customtkinter as ctk

janela = ctk.CTk()
#configurando a janela
janela.title("Testando a Interface") #título da janela
janela.geometry("700x400") #definindo o tamanho da janela
janela.maxsize(width=900, height= 550) #tamanho máximo que a janela pode ir
janela.minsize(width=350, height=200) #tamanho mínimo

#Textbox
textbox = ctk.CTkTextbox(janela, width= 250, height=350, scrollbar_button_color="white", scrollbar_button_hover_color="violet", border_color="red", border_width=2, corner_radius=20, fg_color="black")
textbox.pack()

textbox.insert("0.0", "Digite qualquer coisa aqui!" + "Pindamonhagaba e Xique-Xique\n\n" * 27)

janela.mainloop()